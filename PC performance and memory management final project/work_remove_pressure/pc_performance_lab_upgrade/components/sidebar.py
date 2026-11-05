import streamlit as st
from config import PAGES

def render_sidebar():
    with st.sidebar:
        st.markdown("<div class='brand'>◈ PC PERFORMANCE<br><span>LABORATORY</span></div>", unsafe_allow_html=True)
        page = st.radio("Navigation", PAGES, label_visibility="collapsed")
        st.divider()
        mode = st.selectbox("Dashboard mode", ["Learning Mode", "Live System Mode"], help="Controls the Performance Dashboard. The Live System Monitor always displays actual read-only telemetry.")
        st.caption("Live System Monitor reads actual laptop telemetry through psutil. Learning labs use isolated simulations and never consume real RAM or CPU.")
    return page, mode
