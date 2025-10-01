import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

# InterPolation Helps to fill up the Estimated Data in the Missing Place

df['Age'] = df["Age"].interpolate(method="linear")
df['Salary (INR)'] = df["Salary (INR)"].interpolate(method="linear")
print(df.head(20))

