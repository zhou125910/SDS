import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_violin_plot(cleaned_data_path, output_dir):
    df = pd.read_csv(cleaned_data_path)
    plt.figure(figsize=(12, 8))
    sns.violinplot(x="land_use", y="N", data=df, palette="viridis")
    plt.title("Violin Plot of Nitrogen Content for Different Land Use Types")
    plt.xlabel("Land Use Type")
    plt.ylabel("Nitrogen Content")
    plt.xticks(rotation=45)
    save_path = os.path.join(output_dir, "violin_plot.png")
    plt.savefig(save_path)
    plt.show()
    print(f"Violin plot saved to: {save_path}")

if __name__ == "__main__":
    import sys
    cleaned_data_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_violin_plot(cleaned_data_path, output_dir)