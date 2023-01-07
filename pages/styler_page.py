import inspect

import streamlit as st
from st_pages import add_page_title

from src import agstyler

add_page_title()

code = inspect.getsource(agstyler)
st.code(code)
