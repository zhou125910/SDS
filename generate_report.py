import os
import pandas as pd
from datetime import datetime

def generate_quarto_report(cleaned_data_path, output_dir):
    df = pd.read_csv(cleaned_data_path)
    report_content = f"""---
title: "Soil Nutrient Analysis Report"
author: "Data Analysis Team"
date: "{datetime.now().strftime('%Y-%m-%d')}"
format: 
  html:
    code-fold: true
    toc: true
    toc-depth: 4
jupyter: python3
---

# Soil Nutrient Analysis Report

## Data Overview

- Number of samples: {{ df.shape[0] }}
- Mean pH: {{ df['pH'].mean().round(2) }}
- Mean Nitrogen Content: {{ df['N'].mean().round(2) }} mg/kg
- Mean Phosphorus Content: {{ df['P'].mean().round(2) }} mg/kg
- Mean Potassium Content: {{ df['K'].mean().round(2) }} mg/kg
- Mean Organic Matter: {{ df['organic_matter'].mean().round(2) }}%

## Spatial Distribution

### Scatter Map
![Scatter Map](../Outputs/scatter_map.png)

### Contour Map
![Contour Map](../Outputs/contour_map.png)

## Multivariable Relationship Analysis

### Parallel Coordinates Plot
![Parallel Coordinates Plot](../Outputs/parallel_coordinates.png)

### Pair Plot
![Pair Plot](../Outputs/pair_plot.png)

## Data Distribution Details

### Violin Plot
![Violin Plot](../Outputs/violin_plot.png)

## Interactive Exploration

Please [click here to view the interactive map](../Outputs/interactive_map.html)
"""
    report_path = os.path.join(output_dir, "soil_analysis_report.qmd")
    with open(report_path, "w", encoding="utf-8-sig") as f:
        f.write(report_content)
    print(f"Dynamic report generated, path: {report_path}")
    print("Run the following command in the terminal to render the HTML report:")
    print(f"quarto render \"{report_path}\"")

if __name__ == "__main__":
    import sys
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    generate_quarto_report(cleaned_data_path, output_dir)