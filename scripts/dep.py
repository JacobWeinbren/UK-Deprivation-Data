import pandas as pd

# Load data
final_df = pd.read_csv("output/elections.csv")
deprivation_df = pd.read_csv("data/constituency_imd.csv")

# Define the years of interest
years = [2010, 2015, 2017, 2019]

for year in years:
    # Filter for the specific year and merge with deprivation data
    merged_df = pd.merge(
        final_df[final_df["Year"] == year],
        deprivation_df,
        left_on="id",
        right_on="gss-code",
    )

    # Convert vote columns to numeric
    parties = [
        "Conservative",
        "Liberal Democrat",
        "Labour",
        "UKIP / Brexit",
        "Green",
        "SNP",
        "Plaid Cymru",
        "DUP",
        "Sinn Fein",
        "SDLP",
        "UUP",
        "Alliance",
        "Other",
    ]
    merged_df[parties] = (
        merged_df[parties].apply(pd.to_numeric, errors="coerce").fillna(0)
    )

    # Calculate percentage of votes for each party by deprivation decile
    grouped = merged_df.groupby("pcon-imd-pop-decile")[parties].sum()
    total_votes_by_decile = grouped.sum(axis=1)
    percentages = grouped.divide(total_votes_by_decile, axis=0) * 100

    # Save the percentages dataframe to a CSV file
    output_path = f"output/{year}_percentages.csv"
    percentages.to_csv(output_path)

    print(f"Saved percentages for {year} to {output_path}")
