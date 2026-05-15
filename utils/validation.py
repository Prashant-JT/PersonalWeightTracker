"""
Data validation module for Personal Weight Tracker.
Contains functions to validate DataFrames and input files.
"""
import pandas as pd
from typing import List, Optional


def validate_weight_data(df: pd.DataFrame) -> bool:
    """
    Validates that the weight DataFrame has the correct columns and valid data.
    
    Args:
        df: DataFrame with weight data
        
    Returns:
        bool: True if validation is successful
        
    Raises:
        ValueError: If required columns are missing or data is invalid
    """
    required_columns = ['date', 'weight']
    
    # Check required columns
    if not all(col in df.columns for col in required_columns):
        missing = [col for col in required_columns if col not in df.columns]
        raise ValueError(f"Missing required columns: {missing}")
    
    # Check that it's not empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check that weights are positive
    if (df['weight'] <= 0).any():
        raise ValueError("Weight values must be positive")
    
    return True


def validate_fitnotes_data(df: pd.DataFrame) -> bool:
    """
    Validates that the FitNotes DataFrame has the correct columns.
    
    Args:
        df: DataFrame with FitNotes data
        
    Returns:
        bool: True if validation is successful
        
    Raises:
        ValueError: If required columns are missing
    """
    required_columns = ['Date', 'Exercise', 'Weight', 'Reps']
    
    if not all(col in df.columns for col in required_columns):
        missing = [col for col in required_columns if col not in df.columns]
        raise ValueError(f"Missing required columns in FitNotes CSV: {missing}")
    
    if df.empty:
        raise ValueError("FitNotes file is empty")
    
    return True


def validate_workout_plan(plan: dict) -> bool:
    """
    Validates that the workout plan has the correct format.
    
    Args:
        plan: Dictionary with the workout plan
        
    Returns:
        bool: True if validation is successful
        
    Raises:
        ValueError: If format is invalid
    """
    if not isinstance(plan, dict):
        raise ValueError("Workout plan must be a dictionary")
    
    if not plan:
        raise ValueError("Workout plan is empty")
    
    # Verify that each day has a list of exercises
    for day, exercises in plan.items():
        if not isinstance(exercises, list):
            raise ValueError(f"Exercises for day '{day}' must be a list")
        if not exercises:
            raise ValueError(f"Day '{day}' has no exercises")
        if not all(isinstance(ex, str) for ex in exercises):
            raise ValueError(f"All exercises for day '{day}' must be strings")
    
    return True


def validate_number_range(value: float, min_val: float, max_val: float, 
                         field_name: str = "value") -> bool:
    """
    Validates that a number is within a specific range.
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        field_name: Field name for error messages
        
    Returns:
        bool: True if validation is successful
        
    Raises:
        ValueError: If value is out of range
    """
    if value < min_val or value > max_val:
        raise ValueError(
            f"{field_name} must be between {min_val} and {max_val}. "
            f"Received value: {value}"
        )
    return True

# Made with Bob
