import pandas as pd

data = pd.read_csv("customer_data_final.csv")

df = pd.DataFrame(data)

# print(df.head()).

# print(df.isnull()) # Gives True or False if value is missing
# print(df.isnull().sum()) # Gives the total number missing values in all the columns

# df.dropna(axis=0 , inplace=True) # Deletes the entire row which have missing values

# df.dropna(axis=1 , inplace=True) # Deletes the entire col which have missing values
# print(df)

# WE CAN FILL THE MISSING VALUES USING "fillna()" FUNCTION
df["Age"].fillna(df['Age'].mean(), inplace =True)
df["Salary (INR)"].fillna(df['Salary (INR)'].mean(), inplace =True)
# print(df.head(20))
