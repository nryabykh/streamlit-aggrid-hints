import pandas as pd
import streamlit as st


@st.experimental_memo()
def get_data(filename='latest_RAPTOR_by_team.csv'):
    return pd.read_csv(filename)
