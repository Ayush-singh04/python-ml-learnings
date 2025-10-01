import pandas as pd

df = pd.read_csv("customer_data_final.csv", encoding="latin1")

# print(df)

# print("Display 10 rows from Start :")
# print(df.head(10))

# print("Display 10 rows from Last :")
# print(df.tail(10))

# print("Displaying the Info of Data :")
# print(df.info())

# print("Describing the Data :")
# print(df.describe())



# print(f'Shape: {df.shape}')
# print(f'Columns: {df.columns}')


#-#-# Filtering Data Using Pandas #-#-# 

# print(df['PRODUCTLINE']) # Using Column name getting it's data.