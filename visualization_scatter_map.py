import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import os
import sys

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_scatter_map_for_variable(df, variable, output_dir):
    # 创建地理坐标系
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    
    # 绘制散点地图
    fig, ax = plt.subplots(figsize=(12, 8))
    gdf.plot(column=variable, markersize=30, cmap="YlOrRd", legend=True, ax=ax)
    plt.title(f"Soil {variable} Content Scatter Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    # 保存图像
    save_path = os.path.join(output_dir, f"scatter_map_{variable}.png")
    plt.savefig(save_path)
    plt.show()
    print(f"Scatter map for {variable} saved to: {save_path}")

def plot_scatter_maps(cleaned_data_path, output_dir):
    # 读取CSV文件
    df = pd.read_csv(cleaned_data_path)
    
    variables = ["N", "P", "K", "organic_matter"]
    for variable in variables:
        plot_scatter_map_for_variable(df, variable, output_dir)

if __name__ == "__main__":
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_scatter_maps(cleaned_data_path, output_dir)