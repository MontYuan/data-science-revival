import numpy as np
import pandas as pd

# === NumPy 部分 ===
print("=== NumPy ===")

# 创建一个 NumPy 数组
arr = np.array([1,2,3,4,5])
print(f"原始数组: {arr}")
print(f"数组形状: {arr.shape}")
print(f"数据类型: {arr.dtype}")

# 向量化操作（对比 Python 循环）
arr_squared = arr ** 2
print(f"平方后: {arr_squared}")

# 2D 数组
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D 数组:\n{matrix}")
print(f"转置:\n{matrix.T}")

# 广播机制
row = np.array([10, 20, 30])
broadcasted = matrix + row
print(f"\n广播相加:\n{broadcasted}")

# === Pandas 部分 ===
print("\n=== Pandas ===")

# 创建 DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Beijing', 'Shanghai', 'Guangzhou'],
    'salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)

# 基本查看
print(f"\n前2行:\n{df.head(2)}")
print(f"列名: {df.columns.tolist()}")
print(f"统计摘要:\n{df.describe()}")

# 筛选
high_salary = df[df['salary'] > 55000]
print(f"\n薪资>55000:\n{high_salary}")

# 新增列
df['tax'] = df['salary'] * 0.1
print(f"\n加税后:\n{df}")

# 分组聚合
city_avg = df.groupby('city')['salary'].mean()
print(f"\n各城市平均薪资:\n{city_avg}")

# 缺失值处理
df2 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
print(f"\n缺失值统计:\n{df2.isnull().sum()}")
df2_filled = df2.fillna(df2.mean())
print(f"填充后:\n{df2_filled}")