import pandas as pd
import os

def clean_data(df, data_path):
    data_dir = os.path.dirname(data_path)
    df_cleaned = df[(df["pH"] > 0) & (df["N"] > 0) & (df["P"] > 0) & (df["K"] > 0) & (df["organic_matter"] > 0)]
    df_cleaned = df_cleaned.dropna()
    print(f"Data cleaning completed. Original data: {len(df)} records. Cleaned data: {len(df_cleaned)} records.")
    cleaned_data_path = os.path.join(data_dir, "cleaned_soil_data.csv")
    df_cleaned.to_csv(cleaned_data_path, index=False, encoding="utf-8-sig")
    print(f"Cleaned data saved to: {cleaned_data_path}")
    return cleaned_data_path 

if __name__ == "__main__":
    from data_loading import load_data
    soil_data, data_path = load_data()
    cleaned_data_path = clean_data(soil_data, data_path)