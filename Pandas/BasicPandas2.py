import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

# Getting data of particular col

print(df['Salary (INR)'].mean())
print(df['Age'].sum())