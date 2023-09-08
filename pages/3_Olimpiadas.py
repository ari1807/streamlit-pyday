import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly.express as px

st.set_page_config(layout="wide")

st.write("## [Dataset :rainbow[Olympic Data] de Kaggle](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data)")
df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "dataset_olympics.csv"))


filtered_df = dataframe_explorer(df, case=False)

st.dataframe(filtered_df,  use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.write("## Medallas ganadas por país a lo largo del tiempo :medal:")
    
    df_map = df.drop(["Age","Height","Weight"], axis=1)
    df_map['Team'] = df['Team'].replace(['Denmark/Sweden'], 'Denmark')
    df_map = df.dropna().groupby(["NOC", "Team","Year"])["Medal"].aggregate("count").reset_index().sort_values(by=['Year'])


    fig = px.choropleth(df_map, locations='NOC', color='Medal', hover_name='Team', color_continuous_scale="Reds",
                    projection="natural earth", animation_frame='Year',
                    title='Medals won per country per year')
    st.plotly_chart(fig)

with col2:
    st.write("## Porcentaje de participación por sexo por año :woman-swimming: :man-swimming:")
    df_gender = df[["Year","Sex","ID"]].groupby(["Year","Sex"])["ID"].aggregate("count").reset_index()
    years = df_gender["Year"].unique().tolist()
    if ("year_selected" not in st.session_state):
        st.session_state["year_selected"] = years[0]
    
    df_gender_sel = df_gender[df_gender["Year"] == st.session_state["year_selected"]]
    
    st.selectbox("Seleccione un año:",options=years,key="year_selected")
    fig2 = px.pie(df_gender_sel, values="ID", names="Sex", color_discrete_sequence=px.colors.sequential.Agsunset)
    st.plotly_chart(fig2)