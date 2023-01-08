import base64
import io
from typing import Any

import pandas as pd
import streamlit as st
from openpyxl.writer.excel import ExcelWriter

from src import badges


@st.experimental_memo()
def get_data(filename='data/latest_RAPTOR_by_team.csv', filtered: bool = True):
    df = pd.read_csv(filename)
    return df if not filtered else df.query('poss > 1000')


def dataframe_to_excel(df: pd.DataFrame, formatter=None, sheet_name: str = "Download"):
    output = io.BytesIO()

    df = prepare_df(df, formatter)
    writer = pd.ExcelWriter(output)
    sheet_name_cropped = sheet_name[:31]  # name of Excel sheet cannot be longer than 31 chars
    df.to_excel(writer, index=False, sheet_name=sheet_name_cropped)

    writer = adjust_column_widths(writer, sheet_name_cropped, df)
    writer.save()
    return output.getvalue()


def prepare_df(df: pd.DataFrame, formatter: dict) -> pd.DataFrame:
    """Rename and filter columns, round values"""

    if formatter is None:
        return df

    rename_dict = {}
    cols = []
    for k, (new_name, formats) in formatter.items():
        if k in df.columns:
            cols.append(k)
            if "precision" in formats:
                df[k] = df[k].apply(lambda x: safe_round(x, formats["precision"]))

        rename_dict[k] = new_name

    return df[cols].rename(rename_dict, axis=1)


def adjust_column_widths(writer: ExcelWriter, sheet_name_cropped: str, df: pd.DataFrame) -> ExcelWriter:
    """Autoadjust column widths
    Credits: https://stackoverflow.com/a/40535454"""

    worksheet = writer.sheets[sheet_name_cropped]
    for idx, col in enumerate(df.columns):
        series = df[col]
        max_len = max(
            series.astype(str).map(len).max(),  # len of the longest item
            len(str(series.name)),  # len of the column name
        ) + 2
        worksheet.set_column(idx, idx, max_len)  # 'xlsxwriter' lib required
    return writer


def safe_round(value: Any, precision: int = 0) -> Any:
    try:
        numeric_val = float(value)
        return round(numeric_val, precision)
    except ValueError as _:
        return value


def get_download_link(data, filename: str, caption: str) -> str:
    b64 = base64.b64encode(data).decode()
    return (
        f'<a href="data:application/vnd.openxmlformats-officedocuments.spreadsheetml.sheet;base64,{b64}" '
        f'download="{filename}">{caption}</a> '
    )


def add_badges_to_sidebar(*bs):
    all_badges: dict = badges.badges
    for i in range(0, len(bs), 2):
        line = all_badges[bs[i]].url + all_badges[bs[i + 1]].url
        st.sidebar.markdown(line)
