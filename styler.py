import streamlit as st

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode, JsCode

MAX_TABLE_HEIGHT = 500


def get_numeric_style_with_precision(precision: int) -> dict:
    return {"type": ["numericColumn", "customNumericFormat"], "precision": precision}


PRECISION_ZERO = get_numeric_style_with_precision(0)
PRECISION_ONE = get_numeric_style_with_precision(1)
PRECISION_TWO = get_numeric_style_with_precision(2)
PINLEFT = {"pinned": "left"}


def get_current_streamlit_theme() -> str:
    return "streamlit" if not st.get_option("theme.base") else st.get_option("theme.base")


def draw_grid(
        df,
        formatter: dict = None,
        selection="multiple",
        use_checkbox=False,
        fit_columns=False,
        theme="streamlit",
        max_height: int = MAX_TABLE_HEIGHT,
        wrap_text: bool = False,
        auto_height: bool = False,
        grid_options: dict = None,
        key=None,
        css: dict = None
):
    if formatter is None:
        formatter = {}
    cols = (
        [col for col in list(formatter.keys()) if col in df.columns]
        if formatter
        else df.columns
    )
    gb = GridOptionsBuilder.from_dataframe(df[cols])
    gb.configure_selection(selection_mode=selection, use_checkbox=use_checkbox)
    gb.configure_default_column(
        filterable=True,
        groupable=False,
        editable=False,
        wrapText=wrap_text,
        autoHeight=auto_height
    )

    if grid_options is not None:
        gb.configure_grid_options(**grid_options)

    for latin_name, (cyr_name, style_dict) in formatter.items():
        gb.configure_column(latin_name, header_name=cyr_name, **style_dict)

    return AgGrid(
        df[cols],
        gridOptions=gb.build(),
        update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=fit_columns,
        height=min(max_height, (1 + len(df.index)) * 29),
        theme=theme if theme is not None else get_current_streamlit_theme(),
        key=key,
        custom_css=css
    )


def highlight(color, condition):
    code = f"""
        function(params) {{
            color = "{color}";
            if ({condition}) {{
                return {{
                    'backgroundColor': color
                }}
            }}
        }};
    """
    return JsCode(code)
