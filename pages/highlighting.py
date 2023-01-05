import inspect
from enum import Enum

import streamlit as st

import helper
import styler
from styler import PINLEFT, PRECISION_TWO

st.set_page_config(layout='wide')


class Color(Enum):
    RED_LIGHT = "#fcccbb"
    RED_DARK = "#8b0000"
    YELLOW_LIGHT = "#fff0ce"
    YELLOW_DARK = "#ffcc00"
    GREEN_LIGHT = "#abf7b1"
    GREEN_DARK = "#008631"


df = helper.get_data(filtered=True).sort_values('raptor_total', ascending=False)

_, col_center, _ = st.columns((1, 2, 1), gap='large')
col_center.code(inspect.getsource(styler.highlight))

col_left, col_right = st.columns(2, gap='large')

with col_left:
    with st.echo():
        condition_one_value = "params.value < 2000"
        condition_other_values = \
            "params.node.data.raptor_offense < params.node.data.raptor_defense"
        formatter_cells = {
            'player_name': ('Player', PINLEFT),
            'team': ('Team', {'width': 80}),
            'poss': (
                'Possessions',
                {'width': 110,
                 'cellStyle': styler.highlight(Color.RED_LIGHT.value, condition_one_value)}
            ),
            'raptor_offense': ('RAPTOR Off', {**PRECISION_TWO, 'width': 110}),
            'raptor_defense': (
                'RAPTOR Def',
                {**PRECISION_TWO,
                 'width': 110,
                 'cellStyle': styler.highlight(Color.GREEN_LIGHT.value, condition_other_values)
                 }
            ),
        }

with col_right:
    with st.echo():
        condition_for_row = \
            """params.data.poss > 2000 && 
               params.data.raptor_defense > params.data.raptor_offense"""
        formatter_rows = {
            'player_name': ('Player', PINLEFT),
            'team': ('Team', {'width': 80}),
            'poss': ('Possessions', {'width': 110}),
            'raptor_offense': ('RAPTOR Off', {**PRECISION_TWO, 'width': 110}),
            'raptor_defense': ('RAPTOR Def', {**PRECISION_TWO, 'width': 110}),
        }

        # preferred
        go = {
            'rowClassRules': {'high-defense': 'data.poss > 2000 && data.raptor_defense > data.raptor_offense'}
        }
        css = {
            '.high-defense': {'background-color': f'{Color.GREEN_LIGHT.value} !important'}
        }

        # also possible, no custom CSS
        # go = {'getRowStyle': styler.highlight(Color.GREEN_LIGHT.value, condition_for_row)}


col_left, col_right = st.columns(2, gap='large')
with col_left:
    with st.echo():
        styler.draw_grid(
            df.head(20), formatter_cells, fit_columns=True
        )

with col_right:
    with st.echo():
        styler.draw_grid(
            df.head(20), formatter_rows, fit_columns=True, grid_options=go, css=css
        )
