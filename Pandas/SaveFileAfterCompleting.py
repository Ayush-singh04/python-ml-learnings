import pandas as pd

data = {
    "Name": ['Rohan','Sohan','Mohan'],
    "Age": ['20','27','23'],
    "City": ['Bareli','Lucknow','Jaipur']
}

df = pd.DataFrame(data)

print(df)

# Saving this file as CSV 

# df.to_csv("output.csv" , index=False) # here "index=false" indicates that we don't have to write index

# Saving this file as Excel  

df.to_excel("output.xlsx" , index=False)

# Saving this file as Json  

# df.to_json("output.json" , index=False)