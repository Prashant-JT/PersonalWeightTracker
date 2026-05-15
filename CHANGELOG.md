# Changelog

All notable changes to the Personal Weight Tracker project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Configuration Management**: Created centralized configuration in `config/settings.py`
  - All magic numbers and constants now in one place
  - Activity multipliers, chart dimensions, color schemes
  - Easy to modify application-wide settings

- **Data Validation**: Implemented comprehensive validation in `utils/validation.py`
  - `validate_weight_data()`: Validates weight CSV format and data
  - `validate_fitnotes_data()`: Validates FitNotes CSV format
  - `validate_workout_plan()`: Validates workout plan JSON structure
  - `validate_number_range()`: Generic number range validation

- **Error Handling**: Added try-catch blocks in critical sections
  - CSV file upload with validation
  - JSON parsing with error messages
  - User-friendly error messages in Streamlit UI

- **Logging System**: Created logging utility in `utils/logger.py`
  - Configurable log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - File and console output options
  - Function call decorator for debugging
  - Helper functions for common logging tasks

- **Documentation**:
  - `SETUP.md`: Comprehensive setup and installation guide
  - `.env.example`: Environment variables template
  - `setup_env.sh`: Automated setup script for macOS/Linux
  - `setup_env.bat`: Automated setup script for Windows
  - Enhanced README with quick start instructions

- **Type Hints**: Added type hints to utility functions
  - Better IDE support and code completion
  - Improved code documentation
  - Easier to catch type-related bugs

- **Docstrings**: Added comprehensive docstrings to functions
  - Clear parameter descriptions
  - Return value documentation
  - Usage examples where applicable

### Changed
- **Code Organization**: Improved project structure
  - Created `config/` directory for settings
  - Better separation of concerns

- **Import Cleanup**: Removed duplicate and unused imports
  - `Home.py`: Removed numpy, plotly, pandas, defaultdict (not used)
  - `pages/2_Analysis.py`: Removed duplicate streamlit import
  - `pages/3_Fit_Notes.py`: Removed duplicate session_state access

### Fixed
- **Duplicate Code**: Removed redundant code in `pages/3_Fit_Notes.py`
  - Eliminated duplicate `plan_file` and `fitnotes_file` retrieval
  - Cleaner session state management

### Security
- **Environment Variables**: Added `.env` support
  - Sensitive configuration moved to environment variables
  - `.env` added to `.gitignore`
  - `.env.example` provided as template

- **Gitignore Updates**: Enhanced `.gitignore`
  - Added virtual environment directories
  - Added log files
  - Added environment variable files

## [1.0.0] - 2025-01-XX

### Added
- Initial release of Personal Weight Tracker
- Weight data editor with CSV upload/download
- Weight analysis with charts and trends
- FitNotes integration for gym progress tracking
- TDEE and macro calculators
- Weekly and monthly trend analysis
- Predictive goal date calculator
- Interactive Plotly charts
- Session-based data storage (no server-side storage)

### Features
- **Data Editor**: Upload, edit, add, and delete weight entries
- **Analysis Page**: 
  - Daily weight progression with moving average
  - Weekly average trends
  - Seasonality analysis (day of week, monthly patterns)
  - Linear trend line
- **Fit Notes Integration**:
  - Custom workout routine upload (JSON)
  - FitNotes CSV import
  - Exercise progress tracking
  - Progressive overload visualization
- **Tools**:
  - TDEE calculator (Mifflin-St Jeor, Harris-Benedict, Katch-McArdle)
  - Macro calculator
  - Weight goal timeline calculator

---

## Notes

### Version Numbering
- **Major version** (X.0.0): Breaking changes or major feature additions
- **Minor version** (0.X.0): New features, backward compatible
- **Patch version** (0.0.X): Bug fixes and minor improvements

### Categories
- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed in future versions
- **Removed**: Features that have been removed
- **Fixed**: Bug fixes
- **Security**: Security-related changes