import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

Grouped = df.groupby("Company")["Salary (INR)"].sum()
# print(Grouped)

# print(df.count()) # gives count of all the data with specific col