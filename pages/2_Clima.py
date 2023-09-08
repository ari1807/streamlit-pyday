import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly.express as px
import json

st.set_page_config(layout="wide")

st.write("## [Dataset :rainbow[Global Data on Sustainable Energy] de Kaggle](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)")

df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "global-data-on-sustainable-energy.csv"))
df = df.drop(["Latitude","Longitude","Land Area(Km2)","gdp_per_capita","gdp_growth","Renewables (% equivalent primary energy)"], axis=1)

filtered_df = dataframe_explorer(df, case=False)

st.dataframe(filtered_df,  use_container_width=True)


col1, col2 = st.columns(2)

with col1:
    country_codes = json.load(open(Path(Path(__file__).parent.parent, "public", "datasets", "country_codes.json")))

    st.write("## Emisiones de CO2 por país a lo largo del tiempo :earth_americas:")
    
    df_map = df[["Entity", "Year", "Value_co2_emissions_kt_by_country"]].sort_values(by=['Year'])
    df_map["NOC"] = [country_codes[ent] for ent in df_map["Entity"].to_list()]
    fig = px.choropleth(df_map, locations='NOC', color='Value_co2_emissions_kt_by_country', hover_name='Entity', color_continuous_scale="Blues",
                    projection="natural earth", animation_frame='Year',
                    title='CO2 Emissions by Country')
    st.plotly_chart(fig)

with col2:
    pass