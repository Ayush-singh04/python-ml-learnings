import pandas as pd

#-#-# Filtering Data Using Pandas #-#-# 

df = pd.read_csv("customer_data_final.csv" , encoding ="latin1")
# print(df.head())
# print(df)

# print(df.columns)
# print(df['Country']) # Using Column name getting it's data.

# print("Printing two coulums using single command: ")
# print(df[["Full Name" , "Salary (INR)"]])

# print("Getting Data of With a Particular Condition: ")
# print(df[df['Salary (INR)'] > 1750000])

print("Getting Data Following Two Condition: ")
# print(df[(df['Salary (INR)'] > 1700000) & (df['Age'] >50)])
print(df[(df['Salary (INR)'] > 1800000) | (df['Age'] >60)])


