# 1. 列表操作
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # 添加
fruits.remove("banana")  # 删除
print(fruits[1:3])       # 切片

# 2. 字典操作
person = {"name": "Alice", "age": 25, "city": "Beijing"}
person["job"] = "Data Scientist"  # 新增
print(person.get("name"))         # 获取
print(person.keys())              # 所有键

# 3. 循环与条件
numbers = [1, 2, 3, 4, 5]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n * 2)
print(evens)

# 4. 列表推导式（重点）
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)

# 5. 函数定义
def predict_income(age, education_years, experience):
    """简单收入预测公式"""
    base = 30000
    return base + education_years * 5000 + experience * 2000 - age * 200

print(predict_income(30, 16, 5))