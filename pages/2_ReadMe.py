import streamlit as st

st.set_page_config(
    page_title="ReadMe", page_icon="📖", initial_sidebar_state="collapsed"
)

st.balloons()
st.session_state["readme_viewed"] = True
