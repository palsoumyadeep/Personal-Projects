# -*- coding: utf-8 -*-
"""AMC Gen AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UsDgGOctEh656SoKIk1_ANuQmH6BVj2x
"""

import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/AI GEN CASE/Copy of AMC_health_and_safety_data.xlsx - Sheet1.csv")
df.drop(["Industry"], axis = 1, inplace = True)

df.head()

# Create a new column 'Output' that contains the desired format
df['Output'] = df.apply(lambda row: '\n'.join([f"{col} is {row[col]}" for col in df.columns if col != 'NARRATIVE']), axis=1)

# Select the 'NARRATIVE' and 'Output' columns
df_processed = df[['NARRATIVE', 'Output']]

# Save the preprocessed dataframe to a new CSV file
df_processed.to_csv('preprocessed_data.csv', index=False)

df_processed["Output"][0]

df_processed.head()

# Combine 'NARRATIVE' with 'Output' in the desired format

df_processed = pd.read_csv("/content/preprocessed_data.csv")
df_processed = df_processed[:1000]
df_processed["Narrative"] = "Narrative : " + df_processed['NARRATIVE']
df_processed['Combined'] = df_processed['Narrative'] + '\n' + df_processed['Output']

# Save the combined data to a .txt file
with open('combined_data_short.txt', 'w') as file:
    for item in df_processed['Combined']:
        file.write(f"{item}\n\n")
