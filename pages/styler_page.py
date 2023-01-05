import inspect

import streamlit as st

from src import styler

code = inspect.getsource(styler)
st.code(code)
