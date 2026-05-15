"""
Configuration settings for Personal Weight Tracker application.
Centralized configuration to avoid magic numbers and repeated values.
"""

# Application Settings
APP_TITLE = "Personal Weight Tracker"
PAGE_LAYOUT = "wide"
FOOTER_TEXT = "© 2025 Prashant Jeswani Tejwani"

# Data Processing Settings
MOVING_AVERAGE_WINDOW = 7  # Days for moving average calculation
DEFAULT_WEIGHT_MIN = 30.0  # kg
DEFAULT_WEIGHT_MAX = 300.0  # kg
DEFAULT_HEIGHT_MIN = 120.0  # cm
DEFAULT_HEIGHT_MAX = 250.0  # cm
DEFAULT_AGE_MIN = 10
DEFAULT_AGE_MAX = 100

# Activity Level Multipliers for TDEE calculation
ACTIVITY_MULTIPLIERS = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
    "Very active (hard exercise/sports 6-7 days/week)": 1.725,
    "Extra active (very hard exercise & physical job)": 1.9,
}

# Calorie Adjustments (kcal)
CALORIE_ADJUSTMENTS = [-1000, -500, -250, -200, 0, 200, 250, 500, 1000]

# Weight Change Rates (kg/week)
MILD_WEIGHT_CHANGE = 0.25
MODERATE_WEIGHT_CHANGE = 0.5

# Macro Nutrient Calories per Gram
PROTEIN_CALORIES_PER_GRAM = 4
CARB_CALORIES_PER_GRAM = 4
FAT_CALORIES_PER_GRAM = 9

# Chart Settings
CHART_HEIGHT = 600
CHART_WIDTH = 1200
TABLE_HEIGHT = 1200
TABLE_WIDTH = 800

# Color Schemes
DARK_GREEN_START = 0.3  # For weight loss color gradient
DEFAULT_CELL_COLOR = '#2D333B'
HEADER_COLOR = '#22272B'
WEIGHT_GAIN_COLOR = 'rgb(178,34,34)'

# File Upload Settings
MAX_FILE_SIZE_MB = 10
ALLOWED_CSV_EXTENSIONS = ['csv']
ALLOWED_JSON_EXTENSIONS = ['json']

# Required CSV Columns
WEIGHT_DATA_COLUMNS = ['date', 'weight']
FITNOTES_COLUMNS = ['Date', 'Exercise', 'Weight', 'Reps']

# Days of Week (for ordering)
DAYS_OF_WEEK = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
    'Friday', 'Saturday', 'Sunday'
]

# Months (for ordering)
MONTHS_ORDER = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Made with Bob
