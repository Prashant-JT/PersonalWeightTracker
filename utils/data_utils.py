"""
Data utility functions for weight tracking calculations.
Handles weekly averages, moving averages, and trend calculations.
"""
import numpy as np
import pandas as pd
from collections import defaultdict
from typing import Tuple, List, Optional, Callable


def compute_weekly_averages(df: pd.DataFrame) -> Tuple[List[str], List[float], List[Optional[float]]]:
    """
    Compute weekly averages of weight data.
    
    Args:
        df: DataFrame with 'date' and 'weight' columns
        
    Returns:
        Tuple containing:
            - week_labels: List of week labels (e.g., "2025-W01")
            - weekly_means: List of average weights per week
            - weekly_diffs: List of week-to-week differences (first element is None)
    """
    dates = df['date'].values
    weights = df['weight'].values
    weeks = defaultdict(list)
    
    for date, weight in zip(dates, weights):
        py_date = pd.Timestamp(date).to_pydatetime()
        year, week, weekday = py_date.isocalendar()
        weeks[(year, week)].append(weight)
    
    sorted_weeks = sorted(weeks.items())
    weekly_means = [np.mean(week_weights) for _, week_weights in sorted_weeks]
    week_labels = [f"{year}-W{week}" for (year, week), _ in sorted_weeks]
    weekly_diffs = [None] + [weekly_means[i] - weekly_means[i-1] for i in range(1, len(weekly_means))]
    
    return week_labels, weekly_means, weekly_diffs


def compute_moving_average(weights: np.ndarray, window: int = 7) -> np.ndarray:
    """
    Compute a moving average for weight data.
    
    Args:
        weights: Array of weight values
        window: Number of days for the moving average window (default: 7)
        
    Returns:
        Array of moving average values, or empty array if insufficient data
    """
    weights = np.asarray(weights)
    if len(weights) >= window:
        moving_avg = np.convolve(weights, np.ones(window)/window, mode='valid')
        return moving_avg
    else:
        return np.array([])


def compute_moving_average_dates(dates: np.ndarray, window: int = 7) -> np.ndarray:
    """
    Get the dates that correspond to moving average values.
    
    Args:
        dates: Array of date values
        window: Number of days for the moving average window (default: 7)
        
    Returns:
        Array of dates corresponding to moving average values
    """
    if len(dates) >= window:
        return dates[window-1:]
    else:
        return np.array([])


def compute_trend(days: np.ndarray, weights: np.ndarray) -> Callable:
    """
    Compute a linear trend line for weight data.
    
    Args:
        days: Array of day numbers (not used, recalculated internally)
        weights: Array of weight values
        
    Returns:
        Function that computes trend values for given x values
    """
    days = np.arange(1, len(weights) + 1)
    if len(weights) > 1:
        z = np.polyfit(days, weights, 1)
        return np.poly1d(z)
    else:
        return lambda x: [weights[0]] * len(x)
