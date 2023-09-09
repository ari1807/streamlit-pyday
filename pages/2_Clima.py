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

st.write("## [Dataset :rainbow[Global Data on Sustainable Energy] de Kaggle](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)")

df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "global-data-on-sustainable-energy.csv"))
df = df.drop(["Latitude","Longitude","Land Area(Km2)","gdp_per_capita","gdp_growth","Renewables (% equivalent primary energy)"], axis=1)

filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df,  use_container_width=True)

tab1, tab2 = st.tabs(["Emisión de CO2", "Energía de recursos renovables"])

with tab1:
    st.write("## Emisiones de CO2 por país a lo largo del tiempo :earth_americas:")
    
    country_codes = json.load(open(Path(Path(__file__).parent.parent, "public", "datasets", "country_codes.json")))
    
    df_map = df[["Entity", "Year", "Value_co2_emissions_kt_by_country"]].sort_values(by=['Year'])

    df_map.columns = ["Country", "Year", "CO2 Emissions (KT)"]
    df_map["NOC"] = [country_codes[ent] for ent in df_map["Country"].to_list()]
    
    fig = px.choropleth(df_map, locations="NOC", color="CO2 Emissions (KT)",
                        hover_name="Country", color_continuous_scale="Blues", projection="natural earth",
                        animation_frame="Year", width=900, height=550)
    st.plotly_chart(fig)

with tab2:
    st.write("## Energía eléctrica de recursos renovables por país :chart_with_upwards_trend:")

    df_line = df[["Entity", "Year", "Electricity from renewables (TWh)"]].dropna()
    
    all_countries = df["Entity"].unique()

    df_line.columns = ["Country", "Year", "Electricity from renewables (TWh)"]

    fig2 = px.line(df_line, x="Year", y="Electricity from renewables (TWh)",
                   color="Country", width=900, height=550)
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

st.write("## [Dataset :rainbow[Global Data on Sustainable Energy] de Kaggle](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)")

df = pd.read_csv(Path(Path(__file__).parent.parent, "public", "datasets",
    "global-data-on-sustainable-energy.csv"))
df = df.drop(["Latitude","Longitude","Land Area(Km2)","gdp_per_capita","gdp_growth","Renewables (% equivalent primary energy)"], axis=1)

filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df,  use_container_width=True)

tab1, tab2 = st.tabs(["Emisión de CO2", "Energía de recursos renovables"])

with tab1:
    st.write("## Emisiones de CO2 por país a lo largo del tiempo :earth_americas:")
    
    country_codes = json.load(open(Path(Path(__file__).parent.parent, "public", "datasets", "country_codes.json")))
    
    df_map = df[["Entity", "Year", "Value_co2_emissions_kt_by_country"]].sort_values(by=['Year'])

    df_map.columns = ["Country", "Year", "CO2 Emissions (KT)"]
    df_map["NOC"] = [country_codes[ent] for ent in df_map["Country"].to_list()]
    
    fig = px.choropleth(df_map, locations="NOC", color="CO2 Emissions (KT)",
                        hover_name="Country", color_continuous_scale="Blues", projection="natural earth",
                        animation_frame="Year", width=900, height=550)
    st.plotly_chart(fig)

with tab2:
    st.write("## Energía eléctrica de recursos renovables por país :chart_with_upwards_trend:")

    df_line = df[["Entity", "Year", "Electricity from renewables (TWh)"]].dropna()
    
    all_countries = df["Entity"].unique()

    df_line.columns = ["Country", "Year", "Electricity from renewables (TWh)"]

    fig2 = px.line(df_line, x="Year", y="Electricity from renewables (TWh)",
                   color="Country", width=900, height=550)
    fig2.update_layout(
        margin=dict(t=30,l=10,b=10,r=10))
    
    st.plotly_chart(fig2)
    """)