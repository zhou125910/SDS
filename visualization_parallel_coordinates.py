import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import os

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_parallel_coordinates(cleaned_data_path, output_dir):
    df = pd.read_csv(cleaned_data_path)
    plt.figure(figsize=(12, 8))
    parallel_coordinates(df[["N", "P", "K", "organic_matter", "land_use"]], "land_use", colormap="viridis")
    plt.title("Parallel Coordinates Plot for Different Land Use Types")
    plt.xlabel("Indicators")
    plt.ylabel("Values")
    save_path = os.path.join(output_dir, "parallel_coordinates.png")
    plt.savefig(save_path)
    plt.show()
    print(f"Parallel coordinates plot saved to: {save_path}")

if __name__ == "__main__":
    import sys
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_parallel_coordinates(cleaned_data_path, output_dir)