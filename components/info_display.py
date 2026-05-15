"""
Display components for weight tracking information.
Functions to show weight loss statistics and summaries.
"""
import streamlit as st


def show_total_weight_loss(total_loss: float) -> None:
    """
    Display total weight loss or gain with appropriate styling.
    
    Args:
        total_loss: Total weight change (positive = loss, negative = gain)
    """
    if total_loss > 0:
        st.success(f"**Total weight lost:** `{total_loss:.1f} kg`")
    elif total_loss < 0:
        st.warning(f"**Total weight gained:** `{abs(total_loss):.1f} kg`")
    else:
        st.info("No net weight change.")
        
def show_avg_weekly_loss(avg_weekly_loss):
    if avg_weekly_loss is not None:
        st.markdown(f"### Average weekly weight loss rate: `{avg_weekly_loss:.3f} kg/week`")
    else:
        st.markdown("### No weeks with weight loss recorded.")

def show_day_of_week_summary(day_avg):
    max_gain_day = day_avg.idxmax()
    max_gain = day_avg.max()
    max_loss_day = day_avg.idxmin()
    max_loss = day_avg.min()
    if max_gain > 0:
        st.info(f"**You tend to gain the most weight on {max_gain_day} (+{max_gain:.2f} kg on average).**")
    if max_loss < 0:
        st.success(f"**You tend to lose the most weight on {max_loss_day} ({max_loss:.2f} kg on average).**")
    if all(abs(day_avg.fillna(0).values) < 0.05):
        st.write("Your weight changes are very consistent across the week, with no strong daily patterns.")

def show_month_summary(month_avg):
    max_month_gain = month_avg.idxmax()
    max_month_gain_val = month_avg.max()
    max_month_loss = month_avg.idxmin()
    max_month_loss_val = month_avg.min()
    if max_month_gain_val > 0:
        st.info(f"**You tend to gain the most weight in {max_month_gain} (+{max_month_gain_val:.2f} kg on average).**")
    if max_month_loss_val < 0:
        st.success(f"**You tend to lose the most weight in {max_month_loss} ({max_month_loss_val:.2f} kg on average).**")
    if all(abs(month_avg.dropna().values) < 0.05):
        st.write("Your weight changes are very consistent across months, with no strong seasonal patterns.")