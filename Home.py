import streamlit as st
from components.footer import show_footer

st.set_page_config(layout="wide")
st.title('Personal weight loss tracker')
st.markdown("""
Welcome to your personal weight loss tracking app!
Track your progress, analyze your trends, and stay motivated on your fitness journey.

---

### 🚀 **How to get started**

1. **Go to the sidebar** and open the **Data Editor** page.
2. **Upload** your weight data (CSV) or start entering new entries.
3. **Edit, add, or delete** your weight records as needed.
4. **Download** your updated CSV to save your changes.
5. **Visit the Analysis page** to visualize your progress and weekly trends.
6. Explore the **Tools** page for extra utilities like calorie calculation and macro calculation.
7. **NEW:** Go to the **Fit Notes** page to:
    - Upload your custom workout routine as a JSON file (define your days and exercises).
    - Upload your FitNotes.csv file from the FitNotes app.
    - Filter your gym progress by any date range.
    - View interactive charts for each exercise, grouped by your own routine days—see at a glance how you're progressing and whether you're applying progressive overload.
    - Instantly spot trends, plateaus, and improvements to optimize your training plan.

---

### 📊 **Features**

- Easy data entry and editing
- Interactive charts and weekly summaries
- Download your updated data anytime
- Extra tools for calorie and macro tracking
- **NEW:** Customizable gym progress tracking with your own routine and FitNotes data
- All data stays private in your browser session
""")

show_footer()