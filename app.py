import streamlit as st
from st_pages import show_pages_from_config

from src import helper

st.set_page_config(layout='wide')

st.title(':basketball: Extra Hints for Using Streamlit-AgGrid')
st.info('Annotation. Text about dataset')

df = helper.get_data()
col_df, col_aggrid = st.columns((1, 2), gap='large')
with col_df:
    st.markdown('#### Dataset with st.dataframe')
    with st.echo():
        st.dataframe(df.head(50))

with col_aggrid:
    st.markdown('#### Dataset with st-aggrid')
    with st.echo():
        from st_aggrid import AgGrid, GridOptionsBuilder

        AgGrid(
            df.head(50),
            gridOptions=GridOptionsBuilder.from_dataframe(df).build(),
        )

show_pages_from_config(".streamlit/pages.toml")
