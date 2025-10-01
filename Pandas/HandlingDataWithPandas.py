import numpy as np
import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

# print(df)
# print(df.columns)


# If we want to add a new column

# print("Old salary: ")
print(df['Salary (INR)'].head(5))

# Adding New Column
# df["Bonus"] = df['Salary (INR)'] +5000
# print("new Bonus salary: ")
# print(df['Bonus'].head(5))

# Adding New Column using insert function

# df.insert(0, "Bonus" , df['Salary (INR)'] +5000) # we have to give the desired location at first place

# print(df.head(5))

