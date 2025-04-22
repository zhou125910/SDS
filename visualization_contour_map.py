import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import sys

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_contour_map_for_variable(df, variable, output_dir):
    # Prepare data
    x = df["longitude"]
    y = df["latitude"]
    z = df[variable]
    
    # Create grid
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)
    
    # Interpolate
    zi = griddata((x, y), z, (xi, yi), method="linear")
    
    # Plot contour map
    plt.figure(figsize=(12, 8))
    contour = plt.contourf(xi, yi, zi, cmap="YlOrRd", levels=15)
    plt.colorbar(contour)
    plt.title(f"Soil {variable} Content Contour Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    # Save plot
    save_path = os.path.join(output_dir, f"contour_map_{variable}.png")
    plt.savefig(save_path)
    plt.show()
    print(f"Contour map for {variable} saved to: {save_path}")

def plot_contour_maps(cleaned_data_path, output_dir):
    df = pd.read_csv(cleaned_data_path)
    
    variables = ["N", "P", "K", "organic_matter"]
    for variable in variables:
        plot_contour_map_for_variable(df, variable, output_dir)

if __name__ == "__main__":
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_contour_maps(cleaned_data_path, output_dir)