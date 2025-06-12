# %%
import pandas as pd 
import os

# List files in the directory
print(os.listdir(r'C:\Users\hp\Downloads\archive (1)'))
import os
print(os.getcwd())
import pandas as pd
import os

# List files to check if 'togo-dapaong_qc.csv' exists
print(os.listdir(r'C:\Users\hp\Downloads\archive (1)'))
#laod the dataset 
df = pd.read_csv(r'C:\Users\hp\Downloads\archive (1)\sentimentdataset.csv', encoding='latin-1')
# Display the first few rows of the dataset
print(df.head())



# %%
# Check the data types and null values
print(df.info())

# %%
# Check for and handle missing values
df.dropna(inplace=True) 
# Strip whitespace from text fields
df['Text'] = df['Text'].str.strip()


