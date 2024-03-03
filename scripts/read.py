import pandas as pd
from openpyxl.utils import column_index_from_string

# Load the specific sheets
file_path = "data/results.xlsx"
sheet_names = ["2010", "2015", "2017", "2019"]

# Define the columns to keep and their new names
columns_to_keep = {
    "B": "id",
    "C": "constituency",
    "I": "Conservative",
    "L": "Liberal Democrat",
    "O": "Labour",
    "R": "UKIP / Brexit",
    "U": "Green",
    "X": "SNP",
    "AA": "Plaid Cymru",
    "AD": "DUP",
    "AG": "Sinn Fein",
    "AJ": "SDLP",
    "AM": "UUP",
    "AP": "Alliance",
    "AS": "Other",
}

usecols_indices = [column_index_from_string(col) - 1 for col in columns_to_keep.keys()]

# Initialise an empty list to store DataFrames
dfs = []

for sheet_name in sheet_names:
    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        skiprows=3,
        usecols=usecols_indices,
        names=list(columns_to_keep.values()),
        nrows=649,
    )
    # Replace NaN with 0
    df.fillna(0, inplace=True)
    # Add a column to identify the year
    df["Year"] = sheet_name
    dfs.append(df)

# Concatenate all DataFrames
final_df = pd.concat(dfs, ignore_index=True)

print(final_df)
