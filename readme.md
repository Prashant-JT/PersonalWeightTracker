# Personal Weight & Gym Progress Tracker

A multipage Streamlit app for tracking your weight and visualizing your gym progress. Easily upload, edit, and analyze your weight data, and monitor your strength training progress with interactive charts grouped by your own custom workout routine.


> [!TIP]
> The [/data](https://github.com/Prashant-JT/PersonalWeightTracker/tree/main/data) folder have some .csv files as examples

## Features

- Upload your weight data as a CSV file
- Add or delete weight entries
- Download your updated CSV file
- Visualize daily and weekly trends with interactive charts
- **NEW:** Customizable gym progress tracker:
  - Upload your own workout routine as a JSON file (define your days and exercises)
  - Upload your FitNotes_Export.csv file (exported from the FitNotes app)
  - Filter your gym progress by any date range
  - View interactive charts for each exercise, grouped by your own routine days, to see how you are progressing and applying progressive overload
  - **Important:** Exercise names in your JSON must match exactly the names in your FitNotes CSV export
- All changes are session-based for privacy (no data is stored on the server)

---

## Demo

### Data Editor

See how easy it is to upload and edit your weight data:

![Data Editor Demo](assets/gifs/data-editor.gif)

---

### Analysis Page

Visualize your progress and trends:

![Analysis Demo](assets/gifs/analysis.gif)

---

### Gym Progress Tracker

Upload your workout routine and FitNotes CSV to track your gym progress and progressive overload:

![Gym Progress Tracker Demo](assets/gifs/gym-progress.gif)

---

## 🚀 Quick Start

### Installation

1. **Clone the repository** (or download the ZIP):
```bash
git clone https://github.com/Prashant-JT/PersonalWeightTracker.git
cd PersonalWeightTracker
```

2. **Run the setup script**:

**macOS/Linux:**
```bash
chmod +x setup_env.sh
./setup_env.sh
```

**Windows:**
```cmd
setup_env.bat
```

3. **Start the application**:
```bash
# Activate virtual environment first
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run the app
streamlit run Home.py
```

For detailed installation instructions, see [SETUP.md](SETUP.md)

## Usage

- Go to the **Data Editor** page to upload your CSV and manage your data.
- Use the **Analysis** page to view progress and trends.
- Visit the **Fit Notes** page to upload your workout plan and FitNotes data, filter by date, and analyze your gym progress.
- After making changes, always download your updated CSV to save your edits.

## 📁 Project Structure

```
PersonalWeightTracker/
├── Home.py                 # Main entry point
├── config/                 # Configuration settings
├── components/            # Reusable UI components
├── pages/                 # Streamlit pages
├── utils/                 # Utility functions
├── data/                  # Sample data
└── requirements.txt       # Dependencies
```

## License

MIT License

---

> [!NOTE]
> This app does not store your data. Download your CSV after editing to keep your latest records!
