import streamlit as st
import pandas as pd
import datetime
from components.footer import show_footer

st.title("📋 Data Editor")

# Only show uploader if no data in session_state
if 'user_data' not in st.session_state:
    uploaded_file = st.file_uploader("Upload your weight data CSV", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, parse_dates=['date'])
            
            # Validate data
            if 'date' not in df.columns or 'weight' not in df.columns:
                st.error("CSV must contain 'date' and 'weight' columns")
                st.stop()
            
            if df.empty:
                st.error("CSV file is empty")
                st.stop()
            
            if (df['weight'] <= 0).any():
                st.error("Weight values must be positive")
                st.stop()
            
            st.session_state['user_data'] = df
            st.session_state['file_uploaded'] = True
            st.success("File uploaded! You can now edit your data.")
            st.rerun()
        except Exception as e:
            st.error(f"Error reading CSV file: {str(e)}")
            st.stop()
    else:
        st.info("No CSV? Start by adding your first entry below:")
        
        with st.form("first_entry_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_date = st.date_input("Date")
            with col2:
                first_weight = st.number_input("Weight", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Create CSV with first entry")
            if submitted:
                # Use same format as add data
                new_datetime = datetime.datetime.combine(first_date, datetime.time())
                df = pd.DataFrame([{'date': new_datetime, 'weight': first_weight}])
                st.session_state['user_data'] = df
                st.success("First entry added! You can now continue editing your data.")
                st.rerun()  # Only rerun after submit
                st.stop()   # Only stop after submit
        show_footer()
        st.stop()
else:
    df = st.session_state['user_data']
    st.dataframe(df)

    # --- ADD DATA FORM ---
    st.divider()
    st.subheader("Add new weight")
    with st.form("add_weight_form"):
        add_col1, add_col2 = st.columns(2)
        with add_col1:
            new_date = st.date_input('Date')
        with add_col2:
            new_weight = st.number_input('Weight', min_value=0.0, step=0.1)
        add_submitted = st.form_submit_button("Add")
        if add_submitted:
            new_datetime = datetime.datetime.combine(new_date, datetime.time())
            new_data = pd.DataFrame([{'date': new_datetime, 'weight': new_weight}])
            df = pd.concat([df, new_data], ignore_index=True)
            st.session_state['user_data'] = df  # Update session state
            st.session_state['add_success'] = True
            st.rerun()
    if st.session_state.get('add_success'):
        st.success("New data added successfully!")
        st.info("⚠️ Remember to download the updated CSV and replace your existing file to save changes permanently.")
        del st.session_state['add_success']

    # --- DELETE DATA FORM ---
    st.divider()
    st.subheader("Delete data")
    with st.form("delete_weight_form"):
        del_col1, del_col2 = st.columns(2)
        with del_col1:
            date_to_delete = st.date_input('Date to delete')
        with del_col2:
            delete_submitted = st.form_submit_button("Delete")
            if delete_submitted:
                mask = df['date'].dt.date != date_to_delete
                new_df = df[mask]
                if len(new_df) < len(df):
                    df = new_df
                    st.session_state['user_data'] = df # Update session state
                    st.session_state['delete_success'] = True
                    st.rerun()
                else:
                    st.session_state['delete_warning'] = True
                    st.rerun()
    if st.session_state.get('delete_success'):
        st.success("Data deleted successfully!")
        st.info("⚠️ Remember to download the updated CSV and replace your existing file to save changes permanently.")
        del st.session_state['delete_success']
    if st.session_state.get('delete_warning'):
        st.warning("No entry found for that date.")
        del st.session_state['delete_warning']

    # --- DOWNLOAD UPDATED CSV ---
    st.divider()
    csv = df.to_csv(index=False, date_format='%Y-%m-%d %H:%M:%S')
    st.download_button(
        label="Download updated CSV",
        data=csv,
        file_name="data.csv",
        mime="text/csv"
    )

show_footer()