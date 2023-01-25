import streamlit as st
from st_aggrid import JsCode
from st_pages import add_page_title

from src import agstyler, helper
from src.agstyler import PINLEFT, PRECISION_TWO

st.set_page_config(layout='centered')

add_page_title()
st.caption("""Simple AgGrid table formatting. It covered here how to customize the appearance of the table by 
specifying which columns to display, formatting the column names and values, setting the column widths, 
and specifying additional properties.""")

with st.echo(code_location='above'):
    df = (
             helper.get_data()
             .query('poss>1000')
             .sort_values('raptor_total', ascending=False)
    )
    formatter = {
        'player_name': ('Player', PINLEFT),
        'team': ('Team', {'width': 80}),
        'poss': ('Possessions', {'width': 120}),
        'mp': ('mp', {'width': 80}),
        'pace_impact': ('Pace Impact', {**PRECISION_TWO, 'width': 120}),
        'raptor_total': ('RAPTOR', {**PRECISION_TWO, 'width': 100}),
        'war_total': ('WAR', {**PRECISION_TWO, 'width': 80}),
    }

    row_number = st.number_input('Number of rows', min_value=0, value=20)
    data = agstyler.draw_grid(
        df.head(row_number),
        formatter=formatter,
        fit_columns=True,
        selection='multiple',  # or 'single', or None
        use_checkbox='True',  # or False by default
        max_height=300,
    )

if data['selected_rows']:
    sd = data['selected_rows']
    st.info(
        'Selected players:\n\n' + '\n\n'.join(f"{p['player_name']} (RAPTOR {p['raptor_total']})" for p in sd)
    )
