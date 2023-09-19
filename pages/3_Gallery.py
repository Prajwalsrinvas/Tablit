import streamlit as st
from streamlit_carousel import carousel

from utils import read_config

st.set_page_config(
    page_title="Gallery",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.session_state["gallery_viewed"] = True
st.subheader("🖼️ Gallery")
config = read_config()
gallery = config["gallery"]
images = []
for index, image_link in enumerate(gallery, start=1):
    image = {"title": "", "text": "", "interval": None, "img": image_link}
    images.append(image)


carousel(items=images, width=1)
