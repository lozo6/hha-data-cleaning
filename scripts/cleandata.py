import pandas as pd
import datetime as dt
import uuid
import numpy as np

# sets a variable to read csv file in data folder
learningModels = pd.read_csv('data/School_Learning_Modalities.csv')
df_learningModels = pd.DataFrame(learningModels)
print(df_learningModels)
print('\n')

# sets a variable to count the number of rows and columns (rows, columns)
rc_counter = learningModels.shape
print(f'The number of columns are {rc_counter[0]}.\nThe number of columns are {rc_counter[1]}.\n')

# print the names of each column in a nice format
columnNames = list(learningModels)
for name in columnNames:
    print(f'"{name}" is in Column {columnNames.index(name) + 1}.')
print('\n')

# cleans up column names
learningModels.columns = learningModels.columns.str.replace('[^A-Za-z0-9]+', '_')

types = learningModels.dtypes

print(types)

# cleans up white spaces and special characters
for name in columnNames:
    learningModels[name] = learningModels[name].str.strip()
    learningModels[name] = learningModels[name].str.replace('[^A-Za-z0-9]+', '_')