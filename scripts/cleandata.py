import pandas as pd
import datetime as dt
import uuid
import numpy as np
import re

# sets a variable to read csv file in data folder
learningModels = pd.read_csv('data/School_Learning_Modalities.csv')
# makes it cleaner and efficient to write/read code
df = learningModels

check = df.sample

# sets a variable to count the number of rows and columns (rows, columns)
rc_count = df.shape
print(f'The number of columns are {rc_count[0]}.\nThe number of columns are {rc_count[1]}.\n')

# print the names of each column
print(list(df))

# cleans up column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip()

# prints all dtypes to assess dtypes
print(df.dtypes)

# only 'Week' needs to be changed from object to datetime
df['week'] = pd.to_datetime(df['week'])

# only district_name, learning_modality, week, and city needs to be assessed which are all objects
# use select_dtypes and .columns to select the columns needed to be assessed
needsChange = df.select_dtypes(object).columns

# cleans up column values similar to line 22
df[needsChange] = df[needsChange].apply(lambda x : x.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip())

# finds duplicated rows
df.duplicated()
# removes duplicated rows
df.drop_duplicates()

# checks for empty values
missing = df.isnull().sum()
df.replace(to_replace='', value=np.nan, inplace=True) ## replacing empty cells with NaN with numpy
df.replace(to_replace=' ', value=np.nan, inplace=True) ## replacing cells with whitespace with NaN

df['learning_modality'] = df['learning_modality'].apply(lambda x : 'true' if x == 'in_person' else 'false')

# final check to ensure data has been assessed and cleaned up
print(check)

df.to_csv('data/clean_data/school_learning_modalities_mod.csv')