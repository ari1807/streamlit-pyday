import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.dataframe_explorer import dataframe_explorer

import json
from pathlib import Path
from PIL import Image

import pandas as pd
import plotly.express as px

pyday_logo_path = Path(Path(__file__).parent.parent, "public", "images",
    "pyday-logo.png")

st.set_page_config(layout="wide",
                   menu_items=
                   {
                       'Report a bug': "https://www.github.com/ari1807/streamlit-pyday/issues",
                       'About': "Hecho por Ariadna Aspitia para el PyDay La Plata 2023"
                    },
                    page_icon=Image.open(pyday_logo_path))

logo = add_logo(pyday_logo_path)

st.write("## [Dataset :rainbow[Olympic Data] de Kaggle](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data)")
df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "dataset_olympics.csv"))


filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df,  use_container_width=True)

tab1, tab2 = st.tabs(["Medallas ganas por país", "Porcentaje de participación"])

with tab1:
    st.write("## Medallas ganadas por país a lo largo del tiempo :medal:")
    
    df_map = df.drop(["Age","Height","Weight"], axis=1)
    df_map['Team'] = df['Team'].replace(['Denmark/Sweden'], 'Denmark')
    df_map = df.dropna().groupby(["NOC", "Team","Year"])["Medal"].aggregate("count").reset_index().sort_values(by=['Year'])

    fig = px.choropleth(df_map, locations='NOC', color='Medal', hover_name='Team', color_continuous_scale="Reds",
                    projection="natural earth", animation_frame='Year',
                    width=900, height=550)
    st.plotly_chart(fig)

with tab2:
    st.write("## Porcentaje de participación por sexo por año :woman-swimming: :man-swimming:")

    df_gender = df[["Year","Sex","ID"]].groupby(["Year","Sex"])["ID"].aggregate("count").reset_index()
    years = df_gender["Year"].unique().tolist()
    if ("year_selected" not in st.session_state):
        st.session_state["year_selected"] = years[0]
    
    df_gender_sel = df_gender[df_gender["Year"] == st.session_state["year_selected"]]
    
    st.selectbox("Seleccione un año:",options=years,key="year_selected")
    fig2 = px.pie(df_gender_sel, values="ID", names="Sex", color_discrete_sequence=px.colors.sequential.Agsunset,
                  width=900, height=550)
    fig2.update_layout(
        margin=dict(t=30,l=10,b=10,r=10))
    st.plotly_chart(fig2)

with st.expander("View code", expanded=False):
    st.code("""import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.dataframe_explorer import dataframe_explorer

import json
from pathlib import Path
from PIL import Image

import pandas as pd
import plotly.express as px

pyday_logo_path = Path(Path(__file__).parent.parent, "public", "images",
    "pyday-logo.png")

st.set_page_config(layout="wide",
                   menu_items=
                   {
                       'Report a bug': "https://www.github.com/ari1807/streamlit-pyday/issues",
                       'About': "Hecho por Ariadna Aspitia para el PyDay La Plata 2023"
                    },
                    page_icon=Image.open(pyday_logo_path))

logo = add_logo(pyday_logo_path)

st.write("## [Dataset :rainbow[Olympic Data] de Kaggle](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data)")
df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "dataset_olympics.csv"))


filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df,  use_container_width=True)

tab1, tab2 = st.tabs(["Medallas ganas por país", "Porcentaje de participación"])

with tab1:
    st.write("## Medallas ganadas por país a lo largo del tiempo :medal:")
    
    df_map = df.drop(["Age","Height","Weight"], axis=1)
    df_map['Team'] = df['Team'].replace(['Denmark/Sweden'], 'Denmark')
    df_map = df.dropna().groupby(["NOC", "Team","Year"])["Medal"].aggregate("count").reset_index().sort_values(by=['Year'])

    fig = px.choropleth(df_map, locations='NOC', color='Medal', hover_name='Team', color_continuous_scale="Reds",
                    projection="natural earth", animation_frame='Year',
                    width=900, height=550)
    st.plotly_chart(fig)

with tab2:
    st.write("## Porcentaje de participación por sexo por año :woman-swimming: :man-swimming:")

    df_gender = df[["Year","Sex","ID"]].groupby(["Year","Sex"])["ID"].aggregate("count").reset_index()
    years = df_gender["Year"].unique().tolist()
    if ("year_selected" not in st.session_state):
        st.session_state["year_selected"] = years[0]
    
    df_gender_sel = df_gender[df_gender["Year"] == st.session_state["year_selected"]]
    
    st.selectbox("Seleccione un año:",options=years,key="year_selected")
    fig2 = px.pie(df_gender_sel, values="ID", names="Sex", color_discrete_sequence=px.colors.sequential.Agsunset,
                  width=900, height=550)
    fig2.update_layout(
        margin=dict(t=30,l=10,b=10,r=10))
    st.plotly_chart(fig2)
    """)