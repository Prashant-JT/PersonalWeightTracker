"""
Footer component for the Personal Weight Tracker application.
"""
import streamlit as st


def show_footer() -> None:
    """
    Display the application footer with copyright information.
    """
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #22272B;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        font-size: 15px;
        z-index: 100;
    }
    </style>
    <div class="footer">
        <p>© 2025 Prashant Jeswani Tejwani</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

# Made with Bob
