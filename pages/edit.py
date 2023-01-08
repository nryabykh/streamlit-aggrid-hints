import inspect

import streamlit as st
from st_pages import add_page_title

from src import helper, agstyler
from src.helper import dataframe_to_excel, get_download_link
from src.agstyler import PINLEFT, PRECISION_TWO

st.set_page_config(layout='wide')

add_page_title()

col_left, _ = st.columns((2, 1), gap='large')
col_left.caption("""It's easy to make cells editable. With some customization, it's also possible to allow to select a 
value from a dropdown list, rather than entering arbitrary text. Select your best starting 5 for the All-Star Game 
based in RAPTOR metrics!""")

df = helper.get_data(filtered=True).sort_values('raptor_total', ascending=False)
df['pos'] = ''

st.subheader('Select a starting 5 for the All-Star Game')

with st.echo():
    positions = ['PG', 'SG', 'SF', 'PF', 'C']
    formatter = {
        'player_name': ('Player', PINLEFT),
        'team': ('Team', {'width': 80}),
        'poss': ('Possessions', {'width': 110}),
        'raptor_offense': ('RAPTOR Off', {**PRECISION_TWO, 'width': 110}),
        'raptor_defense': ('RAPTOR Def', {**PRECISION_TWO, 'width': 110}),
        'raptor_total': ('RAPTOR', {**PRECISION_TWO, 'width': 110}),
        'pos': ('Position', {
            'editable': True,
            'cellEditor': 'agSelectCellEditor',
            'cellEditorParams': {
                'values': [''] + positions,
            },
            'width': 100
        }),
        'note': ('Note', {'editable': True})
    }

    data = agstyler.draw_grid(df.head(100), formatter)
    df_selected = data['data'].query('pos.isin(@positions)')
    if df_selected.empty:
        st.info('No players selected')
    elif len(df_selected.index) > 5:
        st.warning('Select no more than 5 players')
    else:
        tr = df_selected['raptor_total'].sum()
        st.info(f"""Squad: {', '.join(df_selected['player_name'].values)}.
            \n\nTotal RAPTOR is {round(tr, 2)}.""")

# From future
# btn = st.button("📥 Download table as XLSX")
# if btn:
#     download_data = dataframe_to_excel(
#         df=data['data'],
#         formatter=formatter,
#     )
#     download_link = get_download_link(
#         download_data,
#         filename="download.xlsx",
#         caption="Download file"
#     )
#     st.markdown(download_link, unsafe_allow_html=True)
#
# with st.expander('Code for downloading routine'):
#     st.code(inspect.getsource(dataframe_to_excel))
#     st.code(inspect.getsource(helper.prepare_df))
#     st.code(inspect.getsource(helper.safe_round))
#     st.code(inspect.getsource(helper.adjust_column_widths))
#     st.code(inspect.getsource(helper.get_download_link))
