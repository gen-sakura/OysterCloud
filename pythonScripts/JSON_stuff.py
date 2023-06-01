import json
import numpy as np
import pandas as pd
from pandas import DataFrame as df
import DB_Code as db

top_1000_rows = db.get_top_1000_rows()
print(top_1000_rows)

# obtain the pH readings as a pandas dataframe
def obtain_pH_readings(rows):
    # Check if all entries are pH
    if (np.all(top_1000_rows['label'] == 'pH')):
        print("All entries are pH")
    else:
        raise ValueError("Not all entries are pH")
    
    # Debug print
    print(top_1000_rows['entry'])
    return top_1000_rows['entry']

def create_dataset_JSON(dataframe, name='data.json', label='pH'):
    dataset = dataframe.values.tolist()
    data = {'label' : label, 'datasets' : dataset}
    with open(name, 'w') as file:
        json.dump(data, file)

def create_last_1000_pH_dataset_JSON():
    ph_data = obtain_pH_readings(top_1000_rows)
    create_dataset_JSON(ph_data, 'last_1000_pH_data.json', 'pH')
"""
data = {'label' : labels, 'datasets' : dataset}
with open('data.json', 'w') as f:
    json.dump(data, f)"""
