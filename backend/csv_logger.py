"""
CSV Logger for Traffic Optimization Results
Stores results and analytics in CSV files for historical analysis.
"""

import csv
import os
from datetime import datetime

# CSV file paths
RESULTS_CSV = os.path.join(os.path.dirname(__file__), 'data', 'results.csv')
ANALYTICS_CSV = os.path.join(os.path.dirname(__file__), 'data', 'analytics.csv')

# Headers for CSV files
RESULTS_HEADERS = [
    'timestamp', 'north_cars', 'south_cars', 'west_cars', 'east_cars',
    'north_time', 'south_time', 'west_time', 'east_time',
    'rl_direction', 'rl_timer', 'rl_confidence', 'delay', 'elapsed_seconds'
]

ANALYTICS_HEADERS = [
    'timestamp', 'total_cars', 'avg_green_time', 'max_congestion_direction',
    'congestion_level', 'optimization_status'
]


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def init_csv(filepath, headers):
    """Initialize CSV file with headers if it doesn't exist."""
    ensure_data_dir()
    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)


def log_result(car_counts, timings, rl_rec, delay, elapsed):
    """
    Log optimization result to CSV.
    
    Args:
        car_counts: List of [north, south, west, east] car counts
        timings: Dict with 'north', 'south', 'west', 'east' green times
        rl_rec: RL recommendation dict with 'direction', 'timer', 'confidence'
        delay: Total delay value
        elapsed: Processing time in seconds
    """
    init_csv(RESULTS_CSV, RESULTS_HEADERS)
    
    row = [
        datetime.now().isoformat(),
        car_counts[0], car_counts[1], car_counts[2], car_counts[3],
        timings.get('north', 0), timings.get('south', 0),
        timings.get('west', 0), timings.get('east', 0),
        rl_rec.get('direction', ''), rl_rec.get('timer', 0),
        rl_rec.get('confidence', 0), delay, elapsed
    ]
    
    with open(RESULTS_CSV, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    
    return True


def log_analytics(car_counts, timings, status='success'):
    """
    Log analytics data to CSV.
    
    Args:
        car_counts: List of car counts
        timings: Dict with green times
        status: 'success' or 'error'
    """
    init_csv(ANALYTICS_CSV, ANALYTICS_HEADERS)
    
    total_cars = sum(car_counts)
    times = [timings.get('north', 0), timings.get('south', 0),
             timings.get('west', 0), timings.get('east', 0)]
    avg_time = sum(times) / len(times) if times else 0
    
    directions = ['North', 'South', 'West', 'East']
    max_idx = car_counts.index(max(car_counts))
    max_direction = directions[max_idx]
    
    # Congestion level: low, medium, high based on max car count
    max_cars = max(car_counts)
    if max_cars < 10:
        congestion = 'low'
    elif max_cars < 25:
        congestion = 'medium'
    else:
        congestion = 'high'
    
    row = [
        datetime.now().isoformat(),
        total_cars,
        round(avg_time, 2),
        max_direction,
        congestion,
        status
    ]
    
    with open(ANALYTICS_CSV, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    
    return True


def get_results_summary():
    """Get summary statistics from results CSV."""
    if not os.path.exists(RESULTS_CSV):
        return {'total_runs': 0, 'avg_delay': 0, 'avg_elapsed': 0}
    
    total_runs = 0
    total_delay = 0
    total_elapsed = 0
    
    with open(RESULTS_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_runs += 1
            total_delay += float(row.get('delay', 0) or 0)
            total_elapsed += float(row.get('elapsed_seconds', 0) or 0)
    
    return {
        'total_runs': total_runs,
        'avg_delay': round(total_delay / total_runs, 2) if total_runs else 0,
        'avg_elapsed': round(total_elapsed / total_runs, 2) if total_runs else 0
    }


def get_analytics_summary():
    """Get summary from analytics CSV."""
    if not os.path.exists(ANALYTICS_CSV):
        return {'total_cars_processed': 0, 'success_rate': 0}
    
    total_cars = 0
    success_count = 0
    total_count = 0
    
    with open(ANALYTICS_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_count += 1
            total_cars += int(row.get('total_cars', 0) or 0)
            if row.get('optimization_status') == 'success':
                success_count += 1
    
    return {
        'total_cars_processed': total_cars,
        'success_rate': round((success_count / total_count) * 100, 1) if total_count else 0,
        'total_optimizations': total_count
    }


def get_recent_data(n=20):
    """Get the last n records for charting."""
    if not os.path.exists(RESULTS_CSV):
        return []
    
    data = []
    with open(RESULTS_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'timestamp': row['timestamp'],
                'delay': float(row['delay'] or 0),
                'total_cars': int(row['north_cars'] or 0) + int(row['south_cars'] or 0) + 
                            int(row['west_cars'] or 0) + int(row['east_cars'] or 0),
                'cars': [int(row['north_cars'] or 0), int(row['south_cars'] or 0), 
                         int(row['west_cars'] or 0), int(row['east_cars'] or 0)]
            })
    
    return data[-n:]
