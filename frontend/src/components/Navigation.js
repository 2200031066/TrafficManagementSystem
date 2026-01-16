import React, { useState, useEffect } from 'react';
import styles, { m3 } from '../styles';

const tabs = [
    { id: 'home', label: 'Home', icon: '' },
    { id: 'analytics', label: 'Analytics', icon: '' },
    { id: 'how it works', label: 'Architecture', icon: '' },
    { id: 'about', label: 'About', icon: '' }
];

function Navigation({ activeTab, setActiveTab }) {
    const [health, setHealth] = useState({ status: 'checking', components: {} });

    useEffect(() => {
        checkHealth();
        // Check health every 30 seconds
        const interval = setInterval(checkHealth, 30000);
        return () => clearInterval(interval);
    }, []);

    const checkHealth = async () => {
        try {
            const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
            const response = await fetch(`${apiUrl}/health`, {
                method: 'GET',
                signal: AbortSignal.timeout(5000) // 5 second timeout
            });
            const data = await response.json();
            setHealth(data);
        } catch (err) {
            setHealth({ status: 'offline', components: {} });
        }
    };

    const getStatusColor = () => {
        switch (health.status) {
            case 'healthy': return '#4CAF50';
            case 'degraded': return '#FF9800';
            case 'offline': return '#F44336';
            default: return m3.outline;
        }
    };

    const getStatusLabel = () => {
        switch (health.status) {
            case 'healthy': return 'Backend Online';
            case 'degraded': return 'Degraded';
            case 'offline': return 'Offline';
            default: return 'Checking...';
        }
    };

    return (
        <header style={styles.nav}>
            <div style={styles.navInner}>
                <div style={styles.logo}>
                    <span style={styles.logoIcon}></span>
                    <span style={styles.logoText}>
                        Traffic<span style={{ color: m3.primary }}>AI</span>
                    </span>
                </div>

                <div style={styles.navTabs}>
                    {tabs.map(tab => (
                        <button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            style={{
                                ...styles.navTab,
                                ...(activeTab === tab.id ? styles.navTabActive : {})
                            }}
                        >
                            <span style={{ fontSize: '1.2rem' }}>{tab.icon}</span>
                            {tab.label}
                        </button>
                    ))}
                </div>

                {/* Health Status Indicator */}
                <div
                    onClick={checkHealth}
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '8px',
                        padding: '8px 16px',
                        borderRadius: '100px',
                        background: getStatusColor() + '15',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease'
                    }}
                    title={health.status === 'healthy' ?
                        `API: ${health.components?.api || 'ok'}, GA: ${health.components?.ga_binary || 'ok'}` :
                        'Click to refresh'
                    }
                >
                    <div style={{
                        width: '10px',
                        height: '10px',
                        borderRadius: '50%',
                        background: getStatusColor(),
                        boxShadow: `0 0 8px ${getStatusColor()}`,
                        animation: health.status === 'checking' ? 'pulse 1.5s infinite' : 'none'
                    }} />
                    <span style={{
                        fontSize: '0.8rem',
                        fontWeight: '600',
                        color: getStatusColor(),
                        letterSpacing: '0.5px'
                    }}>
                        {getStatusLabel()}
                    </span>
                </div>
            </div>
        </header>
    );
}

export default Navigation;
