import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

# print(df.head())

# Updating Data at a particular Row and Col
# df.loc[0,"Age"] = 22
# print(df.head())
print(df.columns)

# Updating Data of a complete Row or Col

    # Decreasing Everyone's Salary by 10%
# df['Salary (INR)'] = df['Salary (INR)'] / 10

# print(df.head(5))

# Deleting a particular column

df.drop(columns=['Country'], inplace=True)

print(df.columns)