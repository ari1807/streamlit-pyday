import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge

streamlit = Image.open(Path(Path(__file__).parent, "public", "images",
    f"streamlit-logo-primary-light-text.png"))

pyday_logo_path = Path(Path(__file__).parent, "public", "images",
    "pyday-logo.png")

st.set_page_config(layout="centered", 
                   menu_items=
                   {
                       'Report a bug': "https://www.github.com/ari1807/streamlit-pyday/issues",
                       'About': "Hecho por Ariadna Aspitia para el PyDay La Plata 2023"
                    },
                    page_icon=Image.open(pyday_logo_path))

logo = add_logo(pyday_logo_path)

st.image(streamlit)

badge(type="github", name="ari1807/streamlit-pyday", url="https://github.com/ari1807/streamlit-pyday")