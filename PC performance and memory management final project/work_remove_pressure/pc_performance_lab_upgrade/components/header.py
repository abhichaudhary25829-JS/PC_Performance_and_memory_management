import streamlit as st

def render_header(page, mode, live=False):
    dot = "● LIVE SYSTEM" if live else "● LEARNING LAB"
    st.markdown(
        f"<div class='topbar'><div><span class='eyebrow'>PC PERFORMANCE LAB</span><h1>{page}</h1></div>"
        f"<div class='status'><b>{dot}</b><br><small>{mode} · Session active</small></div></div>",
        unsafe_allow_html=True
    )
