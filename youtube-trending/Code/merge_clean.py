import pandas as pd
import os
import re
from datetime import datetime as dt

# Merging the Data to a single DF
def find_all_files(path, ty='csv', Name='Merged_DF.csv'):
    #Iteratively appends all files with ty extention to list_of_files
    for root,dirs,files in os.walk(path):
        [list_of_files.append(file) for file in files if (file.endswith(f".{ty}") and (file!=Name))]

Name = 'Merged_DF.csv' #Name of Final DF
list_of_files = []
data_path = os.path.join('..', 'Data')
find_all_files(data_path, Name=Name)

Total_DF = pd.DataFrame()
for file in list_of_files:
    try:
        DF = pd.read_csv(os.path.join('..', 'Data', file), encoding='utf-8')
    except:
        DF = pd.read_csv(os.path.join('..', 'Data', file), encoding='latin1')
    Total_DF = (DF if Total_DF.empty else pd.concat([Total_DF, DF]))


# Total DF Cleaning
#Convert the 'trending_date' to date format
Total_DF['trending_date'] = Total_DF['trending_date'].map(lambda x: dt.strptime(x, "%y.%d.%m"))
#Convert the 'publish_time' to date format
Total_DF['publish_time'] = pd.to_datetime(Total_DF['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ') #%f means microsecond which means 6 digits. This works here as it is always 0 microseconds
#Convert NaN values in 'description' to ''
Total_DF['description'].fillna(value='', inplace=True)

# Removing for duplicate rows
#Drop the duplicate rows
Dup_Rem_DF = Total_DF.drop_duplicates(subset=['video_id', 'trending_date'], keep='last')
Dup_Rem_DF = Dup_Rem_DF.iloc[Dup_Rem_DF[(Dup_Rem_DF['video_id']!='#NAME?')].index, :]

# Save the DataFrame as pickle 
Dup_Rem_DF.to_pickle("../Data/VideoDF.pkl")