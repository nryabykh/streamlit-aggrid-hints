import inspect

import streamlit as st

import styler

code = inspect.getsource(styler)
st.code(code)
