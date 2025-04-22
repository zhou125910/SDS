import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def get_project_dir():
    root = tk.Tk()
    root.withdraw()  
    project_dir = filedialog.askdirectory(title="Select Project Directory")
    if not project_dir:
        raise ValueError("No project directory selected!")
    return project_dir

project_dir = get_project_dir()

DATA_DIR = os.path.join(project_dir, "Data")
OUTPUTS_DIR = os.path.join(project_dir, "Outputs")
REPORTS_DIR = os.path.join(project_dir, "Reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_script(script_name, cleaned_data_path, output_dir):
    try:
        subprocess.check_call([sys.executable, script_name, cleaned_data_path, output_dir])
        print(f"Script '{script_name}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Script '{script_name}' execution failed: {e}")
        sys.exit(1)

def main():
    from data_loading import load_data
    from data_cleaning import clean_data

    soil_data, data_path = load_data()
    cleaned_data_path = clean_data(soil_data, data_path)

    output_dir = filedialog.askdirectory(title="Select Output Directory for Visualizations")
    if not output_dir:
        output_dir = os.path.dirname(cleaned_data_path)

    visualization_scripts = [
        "visualization_scatter_map.py",
        "visualization_contour_map.py",
        "visualization_parallel_coordinates.py",
        "visualization_pair_plot.py",
        "visualization_violin_plot.py",
        "visualization_interactive_map.py"
    ]

    for script in visualization_scripts:
        run_script(script, cleaned_data_path, output_dir)

    run_script("generate_report.py", cleaned_data_path, output_dir)

    print("All scripts executed successfully.")

if __name__ == "__main__":
    main()