#generate_soil_data
import os
import pandas as pd
import numpy as np
from faker import Faker

# 初始化Faker生成器
fake = Faker()

# 检查目录是否存在，不存在则创建
save_dir = r"E:\VCOAD\Data"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 生成2000条以上的土壤养分数据
data_size = 2000  # 设置数据量为2000条
data = {
    "longitude": [fake.longitude() for _ in range(data_size)],  # 经度
    "latitude": [fake.latitude() for _ in range(data_size)],   # 纬度
    "pH": np.round(np.random.uniform(4.0, 8.5, data_size), 2),  # pH值，合理范围4.0-8.5
    "N": np.round(np.random.normal(100, 30, data_size), 2),    # 氮含量，正态分布，均值100，标准差30
    "P": np.round(np.random.uniform(10, 60, data_size), 2),    # 磷含量，均匀分布，范围10-60
    "K": np.round(np.random.uniform(50, 350, data_size), 2),   # 钾含量，均匀分布，范围50-350
    "organic_matter": np.round(np.random.uniform(1.0, 10.0, data_size), 2),  # 有机质含量，均匀分布，范围1.0-10.0
    "land_use": np.random.choice(["农田", "林地", "草地", "城市用地", "水域"], data_size)  # 土地利用类型
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 保存为CSV文件
save_path = os.path.join(save_dir, "soil_data.csv")
df.to_csv(save_path, index=False, encoding="utf-8-sig")

print(f"土壤养分数据已成功生成并保存至：{save_path}")