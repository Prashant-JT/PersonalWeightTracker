# AI Agent Instructions for Personal Weight Tracker

This file contains mandatory instructions for AI coding assistants (Bob, Copilot, Claude, ChatGPT, etc.) working on this project.

**IMPORTANT**: All AI agents MUST follow these guidelines when proposing or generating code for this project.

---

## Core Requirements

### 1. Language
- **ALL code, comments, docstrings, and variable names MUST be in English**
- No Spanish or other languages in code
- Documentation files can be bilingual if needed

### 2. Code Style
- Follow PEP 8 strictly
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black default)
- Use snake_case for functions and variables
- Use PascalCase for classes
- Use UPPER_CASE for constants

### 3. Type Hints
- **MANDATORY** for all function parameters and return values
- Use `typing` module for complex types
- Example:
```python
from typing import List, Dict, Optional, Tuple

def process_data(
    data: pd.DataFrame,
    start_date: datetime,
    end_date: Optional[datetime] = None
) -> Tuple[pd.DataFrame, int]:
    """Process weight data."""
    pass
```

### 4. Docstrings
- **MANDATORY** for all functions, classes, and modules
- Use Google style docstrings
- Include: description, Args, Returns, Raises, Example
- Example:
```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index.
    
    Args:
        weight: Weight in kilograms
        height: Height in meters
        
    Returns:
        BMI value as float
        
    Raises:
        ValueError: If weight or height is negative or zero
        
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    return weight / (height ** 2)
```

---

## Project Structure

### File Organization
```
PersonalWeightTracker/
├── Home.py                 # Main Streamlit entry point
├── components/            # Reusable UI components
│   ├── __init__.py
│   ├── footer.py
│   ├── info_display.py
│   └── predictive_goal.py
├── pages/                 # Streamlit pages (numbered)
│   ├── 1_Data_Editor.py
│   ├── 2_Analysis.py
│   ├── 3_Fit_Notes.py
│   ├── 4_Tools.py
│   └── 5_Chat.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── charts.py
│   ├── data_utils.py
│   ├── database.py
│   ├── file_utils.py
│   ├── gym_charts.py
│   ├── logger.py
│   └── validation.py
├── config/                # Configuration
│   ├── __init__.py
│   └── settings.py
├── tests/                 # Test files
│   ├── __init__.py
│   └── test_*.py
└── docs/                  # Documentation
```

### Import Order
Always organize imports in this order:
```python
# 1. Standard library imports
import os
import sys
from datetime import datetime
from typing import List, Optional

# 2. Third-party imports
import pandas as pd
import streamlit as st
from supabase import create_client

# 3. Local application imports
from config.settings import MAX_WEIGHT
from utils.validation import validate_weight_data
from components.footer import show_footer
```

---

## Mandatory Practices

### 1. Error Handling
Always include proper error handling:
```python
def load_data(file_path: str) -> pd.DataFrame:
    """Load data from CSV file."""
    try:
        df = pd.read_csv(file_path, parse_dates=['date'])
        
        # Validate data
        if 'date' not in df.columns or 'weight' not in df.columns:
            raise ValueError("CSV must contain 'date' and 'weight' columns")
        
        if df.empty:
            raise ValueError("CSV file is empty")
        
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty or corrupted")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
```

### 2. Logging
Use the project's logging system:
```python
from utils.logger import get_logger

logger = get_logger(__name__)

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Process weight data."""
    logger.info("Starting data processing")
    try:
        result = data.sort_values('date')
        logger.info(f"Processed {len(result)} records")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}", exc_info=True)
        raise
```

### 3. Configuration
Use centralized configuration from `config/settings.py`:
```python
# CORRECT
from config.settings import MAX_WEIGHT, MIN_WEIGHT, CHART_HEIGHT

# INCORRECT
MAX_WEIGHT = 300  # Don't hardcode values
```

### 4. Validation
Always validate input data:
```python
from utils.validation import validate_weight_data, validate_number_range

def add_weight_entry(date: datetime, weight: float) -> None:
    """Add new weight entry."""
    # Validate input
    validate_number_range(weight, 30.0, 300.0, "weight")
    
    # Process data
    # ...
```

### 5. Testing
When creating new functions, also create tests:
```python
# In utils/data_utils.py
def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI."""
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    return weight / (height ** 2)

# In tests/test_data_utils.py
import pytest
from utils.data_utils import calculate_bmi

def test_calculate_bmi_normal():
    """Test BMI calculation with normal values."""
    assert abs(calculate_bmi(70, 1.75) - 22.86) < 0.01

def test_calculate_bmi_zero_height():
    """Test BMI calculation with zero height."""
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)

def test_calculate_bmi_negative_weight():
    """Test BMI calculation with negative weight."""
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)
```

---

## Code Generation Rules

### When Creating New Functions

1. **Always include**:
   - Type hints for all parameters and return value
   - Google-style docstring
   - Input validation
   - Error handling
   - Logging (if appropriate)

2. **Example template**:
```python
from typing import Optional
from utils.logger import get_logger

logger = get_logger(__name__)

def function_name(
    param1: str,
    param2: int,
    param3: Optional[float] = None
) -> Dict[str, Any]:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        param3: Description of param3 (optional)
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When validation fails
        TypeError: When wrong type is provided
        
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        {'status': 'success'}
    """
    logger.debug(f"function_name called with param1={param1}, param2={param2}")
    
    # Input validation
    if not param1:
        raise ValueError("param1 cannot be empty")
    if param2 < 0:
        raise ValueError("param2 must be non-negative")
    
    try:
        # Function logic here
        result = {"status": "success"}
        logger.info("Function completed successfully")
        return result
    except Exception as e:
        logger.error(f"Error in function_name: {e}", exc_info=True)
        raise
```

### When Creating New Classes

```python
from typing import List, Optional
from utils.logger import get_logger

logger = get_logger(__name__)

class ClassName:
    """
    Brief description of the class.
    
    Attributes:
        attribute1: Description of attribute1
        attribute2: Description of attribute2
        
    Example:
        >>> obj = ClassName("value")
        >>> obj.method()
        'result'
    """
    
    def __init__(self, param: str) -> None:
        """
        Initialize ClassName.
        
        Args:
            param: Description of param
            
        Raises:
            ValueError: If param is invalid
        """
        if not param:
            raise ValueError("param cannot be empty")
        
        self.attribute1 = param
        self.attribute2: List[str] = []
        logger.info(f"ClassName initialized with param={param}")
    
    def method(self) -> str:
        """
        Description of what the method does.
        
        Returns:
            Description of return value
        """
        logger.debug("method called")
        return "result"
```

### When Modifying Existing Code

1. **Maintain backward compatibility** unless explicitly told otherwise
2. **Update existing tests** to reflect changes
3. **Add new tests** for new functionality
4. **Update docstrings** if behavior changes
5. **Update CHANGELOG.md** with changes

---

## Database Operations

### Using Supabase
```python
from utils.database import get_database_manager
from utils.logger import get_logger

logger = get_logger(__name__)

def save_weight_to_db(date: datetime, weight: float) -> bool:
    """
    Save weight entry to database.
    
    Args:
        date: Date of measurement
        weight: Weight value in kg
        
    Returns:
        True if successful, False otherwise
        
    Raises:
        ValueError: If weight is invalid
        Exception: If database operation fails
    """
    # Validate input
    if weight <= 0:
        raise ValueError("Weight must be positive")
    
    try:
        db = get_database_manager()
        if db is None:
            logger.warning("Database not configured, skipping save")
            return False
        
        db.insert_weight(date, weight)
        logger.info(f"Weight saved: {weight}kg on {date}")
        return True
    except Exception as e:
        logger.error(f"Failed to save weight: {e}", exc_info=True)
        raise
```

---

## Streamlit-Specific Guidelines

### Page Structure
```python
import streamlit as st
from components.footer import show_footer
from utils.logger import get_logger

logger = get_logger(__name__)

# Page configuration (only in Home.py)
# st.set_page_config(layout="wide")

st.title("Page Title")

# Main content
try:
    # Your page logic here
    pass
except Exception as e:
    logger.error(f"Error in page: {e}", exc_info=True)
    st.error(f"An error occurred: {str(e)}")

# Footer (always at the end)
show_footer()
```

### Session State
```python
# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = None

# Use session state
data = st.session_state['user_data']

# Update session state
st.session_state['user_data'] = new_data
```

---

## Testing Requirements

### Test File Structure
```python
# tests/test_module_name.py
import pytest
from datetime import datetime
from utils.module_name import function_to_test

class TestFunctionName:
    """Tests for function_name."""
    
    def test_normal_case(self):
        """Test with normal input."""
        result = function_to_test("input")
        assert result == "expected"
    
    def test_edge_case(self):
        """Test with edge case input."""
        result = function_to_test("")
        assert result is None
    
    def test_error_case(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            function_to_test(None)
    
    @pytest.fixture
    def sample_data(self):
        """Fixture for test data."""
        return {"key": "value"}
    
    def test_with_fixture(self, sample_data):
        """Test using fixture."""
        result = function_to_test(sample_data)
        assert result is not None
```

### Coverage Requirements
- Aim for >80% code coverage
- Test happy path, edge cases, and error cases
- Mock external dependencies (database, APIs)

---

## Security Guidelines

### Input Validation
```python
def process_user_input(user_input: str) -> str:
    """Process user input safely."""
    # Validate and sanitize
    if not user_input or len(user_input) > 1000:
        raise ValueError("Invalid input length")
    
    # Remove potentially dangerous characters
    sanitized = user_input.strip()
    
    return sanitized
```

### Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()

# CORRECT
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in environment")

# INCORRECT
API_KEY = "hardcoded_key_here"  # Never hardcode secrets
```

---

## Performance Guidelines

### Efficient Data Processing
```python
# CORRECT - Use vectorized operations
df['bmi'] = df['weight'] / (df['height'] ** 2)

# INCORRECT - Avoid loops when possible
for i in range(len(df)):
    df.loc[i, 'bmi'] = df.loc[i, 'weight'] / (df.loc[i, 'height'] ** 2)
```

### Caching
```python
import streamlit as st

@st.cache_data
def load_expensive_data(file_path: str) -> pd.DataFrame:
    """Load and cache data."""
    return pd.read_csv(file_path)
```

---

## Documentation Updates

When adding new features, update:
1. **Function docstrings** - Always
2. **README.md** - If user-facing feature
3. **CHANGELOG.md** - Always
4. **SETUP.md** - If setup process changes
5. **This file (AGENTS.md)** - If new patterns emerge

---

## Commit Message Format

```
type(scope): brief description

Detailed description if needed

- Change 1
- Change 2

Closes #issue_number
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(database): add Supabase integration

- Implement SupabaseManager class
- Add connection pooling
- Add error handling and logging
- Include unit tests

Closes #42
```

---

## Checklist for AI Agents

Before proposing code, ensure:
- [ ] All code is in English
- [ ] Type hints are present
- [ ] Docstrings follow Google style
- [ ] Error handling is implemented
- [ ] Logging is added where appropriate
- [ ] Input validation is included
- [ ] Tests are provided (if new function)
- [ ] Configuration uses config/settings.py
- [ ] Imports are properly organized
- [ ] Code follows PEP 8
- [ ] No hardcoded values (use constants)
- [ ] No security vulnerabilities

---

## Examples of Good vs Bad Code

### Good Example
```python
from typing import Optional
from datetime import datetime
from utils.logger import get_logger
from config.settings import MAX_WEIGHT, MIN_WEIGHT

logger = get_logger(__name__)

def validate_weight_entry(
    weight: float,
    date: datetime,
    notes: Optional[str] = None
) -> bool:
    """
    Validate weight entry data.
    
    Args:
        weight: Weight value in kg
        date: Date of measurement
        notes: Optional notes about the measurement
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If validation fails
        
    Example:
        >>> validate_weight_entry(75.5, datetime.now())
        True
    """
    logger.debug(f"Validating weight entry: {weight}kg on {date}")
    
    if not MIN_WEIGHT <= weight <= MAX_WEIGHT:
        raise ValueError(
            f"Weight must be between {MIN_WEIGHT} and {MAX_WEIGHT}kg"
        )
    
    if date > datetime.now():
        raise ValueError("Date cannot be in the future")
    
    if notes and len(notes) > 500:
        raise ValueError("Notes too long (max 500 characters)")
    
    logger.info("Weight entry validated successfully")
    return True
```

### Bad Example
```python
# Missing type hints, docstring, validation, logging
def validateWeight(w, d, n=None):
    if w < 30 or w > 300:  # Magic numbers
        return False
    return True
```

---

## Git Workflow

### Branch Strategy

This project uses **feature branches** for all significant changes to demonstrate professional development practices.

#### Branch Naming Convention
```
feat/feature-name       # New features
fix/bug-name           # Bug fixes
docs/doc-name          # Documentation
refactor/module-name   # Code refactoring
test/test-name         # Test additions
chore/task-name        # Maintenance tasks
```

#### Workflow for New Features

1. **Create feature branch from main:**
```bash
git checkout main
git pull origin main
git checkout -b feat/feature-name
```

2. **Make changes and commit:**
```bash
git add .
git commit -m "feat(scope): descriptive message

- Detailed change 1
- Detailed change 2

Closes #issue_number"
```

3. **Push branch:**
```bash
git push origin feat/feature-name
```

4. **Create Pull Request on GitHub:**
   - Add description
   - Link related issues
   - Wait for CI/CD checks
   - Review changes
   - Merge to main

5. **Clean up:**
```bash
git checkout main
git pull origin main
git branch -d feat/feature-name
```

#### When to Use Branches

**Use feature branches for:**
- New features (feat/)
- Bug fixes (fix/)
- Refactoring (refactor/)
- Major documentation (docs/)

**Direct commits to main for:**
- Typo fixes
- Minor documentation updates
- Small formatting changes

#### Example Workflow

```bash
# Starting new Supabase integration
git checkout -b feat/supabase-integration

# Make changes
git add utils/database.py docs/SUPABASE_SETUP.md
git commit -m "feat(database): add Supabase integration

- Implement SupabaseManager class
- Add connection pooling
- Add comprehensive error handling
- Include migration utilities"

# Push and create PR
git push origin feat/supabase-integration
# Then create PR on GitHub
```

---

## Final Notes

- **Always prioritize code quality over speed**
- **When in doubt, ask for clarification**
- **Test your code before proposing it**
- **Follow these guidelines strictly**
- **Use feature branches for significant changes**
- **Update this file if you discover new patterns**

---

**Version**: 1.0.1
**Last Updated**: 2025-05-17
**Maintained by**: Project maintainers