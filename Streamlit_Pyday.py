import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge

streamlit = Image.open(Path(Path(__file__).parent, "public", "images",
    "streamlit-logo-primary.png"))

logo = add_logo(Path(Path(__file__).parent, "public", "images",
    "streamlit-logo.png"))

st.image(streamlit)

badge(type="github", name="ari1807/streamlit-pyday", url="https://github.com/ari1807/streamlit-pyday")

