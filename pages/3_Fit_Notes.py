import streamlit as st
import pandas as pd
import json
from components.footer import show_footer
from utils.file_utils import is_valid_csv_file, is_valid_json_file
from utils.gym_charts import plot_exercise_progress

# st.set_page_config(layout="wide")
st.header("🏋️ Gym Progress Tracker (Custom Routine + FitNotes)")

# Persist file uploads in session state
if 'plan_file' not in st.session_state:
    st.session_state['plan_file'] = None
if 'fitnotes_file' not in st.session_state:
    st.session_state['fitnotes_file'] = None

plan_file = st.file_uploader("Upload your workout plan (JSON file)", type="json")
if plan_file is not None:
    st.session_state['plan_file'] = plan_file

fitnotes_file = st.file_uploader("Upload your FitNotes.csv file", type="csv")
if fitnotes_file is not None:
    st.session_state['fitnotes_file'] = fitnotes_file

# Use session_state for file persistence
plan_file = st.session_state['plan_file']
fitnotes_file = st.session_state['fitnotes_file']

# --- File Validation ---
if is_valid_json_file(plan_file) and is_valid_csv_file(fitnotes_file):
    routine = json.load(plan_file)
    days = list(routine.keys())
    plan_file.seek(0)  # Reset pointer after loading
    df = pd.read_csv(fitnotes_file)
    fitnotes_file.seek(0)
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Volume'] = df['Weight'] * df['Reps']

    min_date, max_date = df['Date'].min(), df['Date'].max()
    date_range = st.date_input(
        "Select date range to visualize",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    if isinstance(date_range, (tuple, list)):
        df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

    tabs = st.tabs(days)

    for day_index, day in enumerate(days):
        exercises = routine[day]
        with tabs[day_index]:
            st.subheader(f"{day} - Exercise Progress Details")
            for exercise in exercises:
                df_ex = df[df['Exercise'] == exercise]
                if not df_ex.empty:
                    grouped = df_ex.groupby('Date')
                    volume_total = grouped['Volume'].sum()
                    series_count = grouped.size()
                    max_weight = grouped['Weight'].max()
                    avg_volume_per_series = volume_total / series_count
                    avg_reps_per_series = grouped['Reps'].mean()

                    summary = pd.DataFrame({
                        'Avg_Volume_Per_Series': avg_volume_per_series,
                        'Max_Weight': max_weight,
                        'Series_Count': series_count,
                        'Avg_Reps_Per_Series': avg_reps_per_series
                    }).sort_index()

                    fig = plot_exercise_progress(summary, exercise)
                    st.plotly_chart(fig, use_container_width=True, key=f"{day}_{exercise}")
                else:
                    st.info(f"No data available for {exercise} in the selected range.")
else:
    st.info("Please upload both your workout plan (JSON) and FitNotes CSV files to view your progress.")

st.info(
    """
    **How should your FitNotes CSV be formatted?**

    - Export your workout data from the FitNotes app as a CSV file.
    - The CSV must include at least these columns (case sensitive):
      - `Date` (format: YYYY-MM-DD, e.g., 2025-04-17)
      - `Exercise` (name of the exercise)
      - `Weight` (weight used, in kg or lbs)
      - `Reps` (number of repetitions)
    - Each row represents a single set.
    - Example of the first few rows of a valid CSV:

    ```
    Date,Exercise,Weight,Reps
    2025-04-17,Flat Barbell Bench Press,60,8
    2025-04-17,Flat Barbell Bench Press,60,7
    2025-04-17,Standing Barbell Shoulder Press,30,10
    2025-04-18,Pull Up,0,8
    2025-04-18,Seated Cable Row,40,12
    ```

    - You can export your data via **Settings > Export > Export Workouts to CSV** in the FitNotes app.

    **How should your workout plan JSON be formatted?**
    
    - The exercise names you put in your JSON file **must match exactly** the names as they appear in your FitNotes CSV. 
    (Check for typos, extra spaces, or different capitalization.)

    - For example:
    ```
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
    """
)

show_footer()
