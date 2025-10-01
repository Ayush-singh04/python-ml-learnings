import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'product_id': [f'P{str(i).zfill(3)}' for i in range(1, 11)],
    'product_name': [
        'Laptop', 'Headphones',
        'Smartphone', 'Tablet',
        'Bluetooth Speaker', 'Case', 'Watch', 'Data cable', 'Pen Drive' ,'Adapter'
    ],
    'category': np.random.choice(['Electronics', 'Accessories', 'Components'], 10),
    'price': np.random.uniform(50, 55500, 10).round(2),
    'performance_score': np.random.uniform(1.0, 10.0, 10).round(1),
    'rating': np.random.uniform(3.0, 5.0, 10).round(1),
    'in_stock': np.random.choice([True, False], 10),
    'discount_percent': np.random.randint(0, 50, 10)
    
})

df2 = pd.DataFrame({
    'employee_id': range(1001, 1011),
    'name': [
        'Alice Johnson','Eva Davis',
        'Grace Lee', 'Ivy Martinez',
        'Karen Green','Mia Rodriguez','Olivia Young',
        'Quinn Adams', 'Ruby Scott','Tina Cooper'
    ],
    'department': np.random.choice(['HR', 'Engineering', 'Marketing', 'Sales', 'Finance'], 10),
    'age': np.random.randint(22, 65, 10),
    'salary': np.random.randint(30000, 120000, 10),
    'experience_years': np.random.randint(0, 8, 10),
    'performance_score': np.random.uniform(1.0, 10.0, 10).round(1),
    'remote_work': np.random.choice([True, False], 10)
})

# print(df1.head(5))
# print(df2.head(5))

df_merged = pd.merge(df1 , df2 , on="performance_score",how="inner")

print("Inner join")
# print("Outer join")
# print("left join")
# print("reft join")
print(df_merged)

# THERE IS ALSO A CROSS JOIN
