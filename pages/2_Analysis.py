import streamlit as st
import pandas as pd
import numpy as np
from components.footer import show_footer
from components.predictive_goal import predictive_goal_date
from utils.data_utils import compute_trend, compute_weekly_averages, compute_moving_average, compute_moving_average_dates
from utils.charts import plot_day_of_week_bar, plot_month_bar, plot_weight_progression, plot_weekly_average_weight, plot_weekly_table
from components.info_display import show_avg_weekly_loss, show_day_of_week_summary, show_month_summary, show_total_weight_loss


# st.set_page_config(layout="wide")
st.title("📈 Weight Analysis")

# --- Use session_state to get user data ---
if 'user_data' not in st.session_state:
    st.info("Please upload your CSV file in the Data Editor page first.")
else:
    # Get user data
    df = st.session_state['user_data']
    dates = df['date'].values
    weights = df['weight'].values
    days = np.arange(1, len(weights) + 1)
    
    # Compute weekly averages and differences
    week_labels, weekly_means, weekly_diffs = compute_weekly_averages(df)
    moving_avg = compute_moving_average(weights)
    moving_avg_dates = compute_moving_average_dates(dates)
    trend = compute_trend(dates, weights)
    total_loss = weights[0] - weights[-1] if len(weights) > 0 else 0

    # --- TABS ---
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Weight Progression", "📅 Weekly Average", "📋 Weekly Table", "📊 Seasonality Analysis"])
    
    with tab1:
        # st.subheader("Weight Progression")
        show_total_weight_loss(total_loss)
        fig = plot_weight_progression(dates, weights, moving_avg_dates, moving_avg, trend, days)
        st.plotly_chart(fig, use_container_width=True)
        predictive_goal_date(weights, weekly_diffs)
        
    with tab2:
        st.subheader("Weekly Average Weight (Monday to Sunday)")
        fig2 = plot_weekly_average_weight(week_labels, weekly_means)
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        fig3, avg_weekly_loss = plot_weekly_table(week_labels, weekly_means, weekly_diffs)
        show_avg_weekly_loss(avg_weekly_loss)
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab4:
        st.info("Negative values mean weight loss on average; positive means weight gain. Use these insights to spot patterns and adjust your habits!")
        
        # Date column should be datetime
        df['date'] = pd.to_datetime(df['date'])

        fig_dow, day_avg = plot_day_of_week_bar(df)
        st.plotly_chart(fig_dow, use_container_width=True)
        show_day_of_week_summary(day_avg)
        st.markdown("---")
        fig_month, month_avg = plot_month_bar(df)
        st.plotly_chart(fig_month, use_container_width=True)
        show_month_summary(month_avg)

show_footer()