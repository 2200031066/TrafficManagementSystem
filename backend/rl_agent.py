"""
Traffic RL Agent with Time-of-Day Awareness
Features: Rush hour handling, adaptive priority weights, time-based optimization
"""

import numpy as np
from datetime import datetime


class TrafficRLAgent:
    def __init__(self):
        # Base priority weights for each direction
        self.base_weights = np.array([1.0, 1.0, 1.0, 1.0])  # N, S, W, E
        self.congestion_threshold = 15
        
        # Rush hour configurations (adjust based on your city's patterns)
        self.rush_hours = {
            'morning': {'start': 7, 'end': 10, 'boost': 1.3},   # 7 AM - 10 AM
            'evening': {'start': 17, 'end': 20, 'boost': 1.4},  # 5 PM - 8 PM
        }
        
        # Format: [N, S, W, E] - higher = more priority
        self.rush_patterns = {
            'morning': np.array([1.2, 1.0, 1.3, 1.1]),  # Morning: West/North heavy (incoming)
            'evening': np.array([1.0, 1.2, 1.1, 1.3]),  # Evening: East/South heavy (outgoing)
            'normal': np.array([1.0, 1.0, 1.0, 1.0]),   # Normal: balanced
        }
    
    def get_time_context(self, current_hour=None):
        """Determine current time context and return appropriate weights."""
        if current_hour is None:
            current_hour = datetime.now().hour
        
        time_info = {
            'hour': current_hour,
            'period': 'normal',
            'boost': 1.0,
            'weights': self.rush_patterns['normal']
        }
        
        # Check morning rush
        if self.rush_hours['morning']['start'] <= current_hour < self.rush_hours['morning']['end']:
            time_info['period'] = 'morning_rush'
            time_info['boost'] = self.rush_hours['morning']['boost']
            time_info['weights'] = self.rush_patterns['morning']
        
        # Check evening rush
        elif self.rush_hours['evening']['start'] <= current_hour < self.rush_hours['evening']['end']:
            time_info['period'] = 'evening_rush'
            time_info['boost'] = self.rush_hours['evening']['boost']
            time_info['weights'] = self.rush_patterns['evening']
        
        # Night hours (reduced traffic, shorter cycles)
        elif current_hour >= 22 or current_hour < 6:
            time_info['period'] = 'night'
            time_info['boost'] = 0.8  # Reduce green times at night
        
        return time_info
        
    def predict_best_timer(self, car_counts, ga_times):
        """
        Refines GA suggestions using an RL policy with time-of-day awareness.
        State: [N_cars, S_cars, W_cars, E_cars, GA_N, GA_S, GA_W, GA_E]
        Returns: { 'direction': str, 'timer': int, 'confidence': float, ... }
        """
        car_counts = np.array(car_counts)
        ga_times = np.array(ga_times)
        
        # Get time context
        time_info = self.get_time_context()
        
        # Apply time-based weights
        priority_weights = self.base_weights * time_info['weights']
        
        # Calculate scores for each direction
        mean_cars = np.mean(car_counts) if np.any(car_counts) else 1
        urgency_scores = (car_counts / mean_cars) * priority_weights
        
        # Boost scores during rush hour
        urgency_scores *= time_info['boost']
        
        # Action: Select the direction with the highest urgency score
        best_dir_idx = np.argmax(urgency_scores)
        directions = ['North', 'South', 'West', 'East']
        
        # Refine timer based on congestion and time of day
        base_time = ga_times[best_dir_idx]
        refinement_factor = 1.0 + (0.1 * (car_counts[best_dir_idx] / (mean_cars + 1)))
        
        # Apply time-based adjustment
        refinement_factor *= time_info['boost']
        
        # Night mode: shorter cycles
        if time_info['period'] == 'night':
            final_timer = int(np.clip(base_time * refinement_factor * 0.7, 10, 45))
        else:
            final_timer = int(np.clip(base_time * refinement_factor, 10, 60))
        
        confidence = float(np.max(urgency_scores) / np.sum(urgency_scores)) if np.sum(urgency_scores) > 0 else 0.25

        # Generate context-aware reason
        if time_info['period'] == 'morning_rush':
            reason = f"Morning rush hour detected. Prioritizing {directions[best_dir_idx]} lane for incoming traffic."
        elif time_info['period'] == 'evening_rush':
            reason = f"Evening rush hour detected. Prioritizing {directions[best_dir_idx]} lane for outgoing traffic."
        elif time_info['period'] == 'night':
            reason = f"Night mode active. Reduced cycle time for {directions[best_dir_idx]} lane."
        else:
            reason = f"Standard mode. High vehicle density in {directions[best_dir_idx]} lane."

        return {
            "direction": directions[best_dir_idx],
            "timer": final_timer,
            "confidence": round(confidence, 2),
            "reason": reason,
            "time_context": time_info['period'],
            "hour": time_info['hour']
        }


# Singleton instance
agent = TrafficRLAgent()


def get_rl_recommendation(car_counts, ga_results):
    """
    Get RL recommendation with time-of-day awareness.
    ga_results is expected to be a dict with 'north', 'south', 'west', 'east'
    """
    ga_list = [
        ga_results.get('north', 30),
        ga_results.get('south', 30),
        ga_results.get('west', 30),
        ga_results.get('east', 30)
    ]
    return agent.predict_best_timer(car_counts, ga_list)
