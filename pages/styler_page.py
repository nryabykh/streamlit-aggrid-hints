import inspect

import streamlit as st
from st_pages import add_page_title

from src import agstyler

add_page_title()

st.caption("""This is a code for AgStyler module. With `agstyler`, you can create a dictionary containing the 
formatting for each column and call the `draw_grid` function. The `gridOptions` parameter is constructed behind the 
scenes in `agstyler`. You can also specify some other parameters when calling `draw_grid`. You can find examples 
in this application.""")
code = inspect.getsource(agstyler)
st.code(code)
