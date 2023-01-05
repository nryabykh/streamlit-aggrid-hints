import pandas as pd
import streamlit as st


@st.experimental_memo()
def get_data(filename='data/latest_RAPTOR_by_team.csv', filtered: bool = True):
    df = pd.read_csv(filename)
    return df if not filtered else df.query('poss > 1000')
