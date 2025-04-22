import pandas as pd
import tkinter as tk
from tkinter import filedialog

def load_data():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select Soil Data File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not file_path:
        raise ValueError("No file selected!")
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully with {len(df)} records.")
    return df, file_path 

if __name__ == "__main__":
    soil_data, data_path = load_data()