# streamlit-aggrid-hints

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_red.svg)](https://share.streamlit.io/nryabykh/streamlit-aggrid-hints/app.py)


This repo contains a source code for a Streamlit application that illustrates some tips and tricks for using AgGrid in Streamlit apps, as well as some non-AgGrid related hints. 

Blog posts referenced this repo: 
- [Enhancing your Streamlit tables with AgGrid: advanced tips and tricks | Medium](https://medium.com/@nikolayryabykh/250d4b57903?source=friends_link&sk=e6ca868eb075fee7b4f76899e8ee2708)
- [Tracking and Displaying Changes in the Streamlit App | Medium](https://medium.com/@nikolayryabykh/tracking-and-displaying-changes-in-the-streamlit-app-8bf882f2b24f?source=friends_link&sk=ed403200724cf456d8dcdf3ba59b46b5)

Data source: https://data.fivethirtyeight.com/

## Example of usage of `agstyler`

```python
import agstyler
from agstyler import PINLEFT, PRECISION_TWO

formatter = {
    'player_name': ('Player', PINLEFT),
    'team': ('Team', {'width': 80}),
    'poss': ('Possessions', {'width': 110}),
    'mp': ('mp', {'width': 80}),
    'raptor_total': ('RAPTOR', {**PRECISION_TWO, 'width': 100}),
    'war_total': ('WAR', {**PRECISION_TWO, 'width': 80}),
    'pace_impact': ('Pace Impact', {**PRECISION_TWO, 'width': 120})
}

row_number = st.number_input('Number of rows', min_value=0, value=20)
data = agstyler.draw_grid(
    df.head(row_number),
    formatter=formatter,
    fit_columns=True,
    selection='multiple',  # or 'single', or None
    use_checkbox='True',  # or False by default
    max_height=300
)
```
