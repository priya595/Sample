#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os

def extract(fullpath):

    try:
        file_name = os.path.basename(fullpath)      
        df = pd.read_excel(fullpath,engine="openpyxl")
        print(f'{file_name} File extracted succeefully')
        return df                 

    except FileNotFoundError:
        print(f" Error: The file at '{fullpath}' was not found.")
    except Exception as e:
        print(f" An error occurred: {e}")

