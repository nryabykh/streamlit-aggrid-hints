import streamlit as st
from st_pages import show_pages_from_config

from src import helper
from src.helper import add_badges_to_sidebar

st.set_page_config(layout='wide')

st.title(':basketball: Enhancing Streamlit tables with AgGrid: advanced tips and tricks')
annotation = """This app demonstrates some advanced techniques for using Streamlit AgGrid.

I used a dataset from FiveThirtyEight.com containing NBA statistics for the 2022/23 season. In this dataset 
FiveThirtyEight.com team introduce and use a RAPTOR metric for ranking and scoring NBA players. This statistics "takes 
advantage of modern NBA data, specifically player tracking and play-by-play data that isn’t available in traditional 
box scores. Also, it better reflects how modern NBA teams actually evaluate players.".
 
You can find more information about the dataset and the RAPTOR metric at the following link: 
https://projects.fivethirtyeight.com/nba-player-ratings/ """

col_left, _ = st.columns((2, 1), gap='large')
col_left.caption(annotation)

df = helper.get_data()
col_df, col_aggrid = st.columns(2, gap='large')
with col_df:
    st.markdown('#### Dataset with st.dataframe')
    with st.echo():
        st.dataframe(df.head(50))
    st.info('End of table')

with col_aggrid:
    st.markdown('#### Dataset with st-aggrid')
    with st.echo():
        from st_aggrid import AgGrid, GridOptionsBuilder

        AgGrid(
            df.head(50),
            gridOptions=GridOptionsBuilder.from_dataframe(df).build(),
        )
    st.info('End of table')

show_pages_from_config(".streamlit/pages.toml")
add_badges_to_sidebar('linkedin', 'github')
