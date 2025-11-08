import pandas as pd
import numpy as np

#Step 1 - read CSV file
df = pd.read_csv(r"C:\Users\dusti\OneDrive\Desktop\python interview\Migration_Interview_Data (Python).csv")

#Step 2 - Perform Data Transformation Requirements

#Remove Duplicate Rows:
df = df.drop_duplicates().reset_index(drop=True)

#Prefix all column headers with "Contact:"
df.columns = [f"Contact: {col}" for col in df.columns]

#Convert all names to proper case
for col in df.columns:
    if "Name" in col:
        df[col] = df[col].astype(str).str.title()

#Reformat Dates - Change the format of the "Birthday" column from DD/MM/YYYY to MM/DD/YYYY
birthday_col = "Contact: Date of Birth"
if birthday_col in df.columns:
    df[birthday_col] = pd.to_datetime(df[birthday_col], format="%d/%m/%Y", errors="coerce")
    df[birthday_col] = df[birthday_col].dt.strftime("%m/%d/%Y")

#Generate Unique Numeric IDs
id_col = "Contact: ID"
if id_col in df.columns:
    df[id_col] = np.arange(1, len(df) + 1)

#Replace initials in the "Assigned" column with their full names using the given legend
assigned_col = "Contact: Assigned"
legend = {
    "GM": "Gabe Michel",
    "AA": "Aaron Artsen",
    "BL": "Bond Liver",
    "IC": "Individual Contributor",
    "TM": "Tim Mint"
}

if assigned_col in df.columns:
    # Normalize text and strip whitespace before replacement
    df[assigned_col] = df[assigned_col].astype(str).str.strip()

    #replace known initials
    df[assigned_col] = df[assigned_col].replace(legend)

    #handle blank, empty, or missing values (NaN, "", "nan")
    df[assigned_col] = df[assigned_col].replace(["", "nan", "NaN", None, np.nan], "Gabe Michel")


#Save to a new CSV file
df.to_csv("OutputFinal.csv", index =False)
