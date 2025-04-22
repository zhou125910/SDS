import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_interactive_map(cleaned_data_path, output_dir):
    df = pd.read_csv(cleaned_data_path)
    fig = px.scatter_mapbox(
        df, lat="latitude", lon="longitude", color="N", size="organic_matter",
        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
        hover_name="land_use", hover_data={"N": True, "P": True, "K": True, "organic_matter": True}
    )
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        title="Interactive Soil Nutrient Map"
    )
    save_path = os.path.join(output_dir, "interactive_map.html")
    fig.write_html(save_path)
    fig.show()
    print(f"Interactive map saved to: {save_path}")

if __name__ == "__main__":
    import sys
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_interactive_map(cleaned_data_path, output_dir)