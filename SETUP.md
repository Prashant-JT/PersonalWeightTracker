# Setup Guide - Personal Weight Tracker

This guide will help you set up and run the Personal Weight Tracker application on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation

### Option 1: Automatic Setup (Recommended)

#### On macOS/Linux:

```bash
# Make the setup script executable (if not already)
chmod +x setup_env.sh

# Run the setup script
./setup_env.sh
```

#### On Windows:

```cmd
# Run the setup script
setup_env.bat
```

The script will:
1. Create a virtual environment
2. Install all dependencies
3. Create a `.env` file from the example

### Option 2: Manual Setup

#### 1. Create a Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 3. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your preferred settings (optional)
```

## Running the Application

### 1. Activate the Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### 2. Start the Application

```bash
streamlit run Home.py
```

The application will open in your default web browser at `http://localhost:8501`

## Project Structure

```
PersonalWeightTracker/
├── Home.py                 # Main application entry point
├── config/                 # Configuration files
│   ├── __init__.py
│   └── settings.py        # Centralized settings
├── components/            # Reusable UI components
│   ├── info_display.py
│   └── predictive_goal.py
├── pages/                 # Streamlit pages
│   ├── 1_Data_Editor.py
│   ├── 2_Analysis.py
│   ├── 3_Fit_Notes.py
│   ├── 4_Tools.py
│   └── 5_Chat.py
├── utils/                 # Utility functions
│   ├── charts.py
│   ├── data_utils.py
│   ├── file_utils.py
│   ├── gym_charts.py
│   └── validation.py
├── data/                  # Sample data files
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── setup_env.sh/bat      # Setup scripts
```

## Usage

### 1. Data Editor Page
- Upload your weight data CSV or create a new one
- Add, edit, or delete weight entries
- Download your updated data

### 2. Analysis Page
- View weight progression charts
- Analyze weekly trends
- See seasonality patterns
- Set weight goals with predictions

### 3. Fit Notes Page
- Upload your workout routine (JSON format)
- Upload FitNotes CSV export
- Track gym progress and progressive overload
- Filter by date range

### 4. Tools Page
- Calculate TDEE (Total Daily Energy Expenditure)
- Calculate macronutrient targets
- Estimate weight goal timeline

## CSV Format Requirements

### Weight Data CSV
```csv
date,weight
2025-01-01 00:00:00,80.5
2025-01-02 00:00:00,80.3
```

### FitNotes CSV
```csv
Date,Exercise,Weight,Reps
2025-04-17,Flat Barbell Bench Press,60,8
2025-04-17,Flat Barbell Bench Press,60,7
```

### Workout Plan JSON
```json
{
  "Day 1": [
    "Flat Barbell Bench Press",
    "Standing Barbell Shoulder Press"
  ],
  "Day 2": [
    "Pull Up",
    "Seated Cable Row"
  ]
}
```

## Troubleshooting

### Virtual Environment Issues

If you have issues activating the virtual environment:

**macOS/Linux:**
```bash
# Try using the full path
source ./venv/bin/activate
```

**Windows:**
```cmd
# Try using the full path
.\venv\Scripts\activate
```

### Module Not Found Errors

If you get "Module not found" errors:
```bash
# Make sure you're in the virtual environment
# Then reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use

If port 8501 is already in use:
```bash
# Use a different port
streamlit run Home.py --server.port 8502
```

## Deactivating the Virtual Environment

When you're done using the application:
```bash
deactivate
```

## Updating Dependencies

To update all dependencies to their latest versions:
```bash
pip install --upgrade -r requirements.txt
```

## Support

For issues or questions:
1. Check the [README.md](readme.md) for general information
2. Review the troubleshooting section above
3. Check the GitHub issues page

## License

MIT License - See [LICENSE](LICENSE) file for details