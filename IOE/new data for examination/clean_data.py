import pandas as pd
import numpy as np

my_data = pd.read_excel("C:/Users/Roxanne/Documents/GitHub/research/IOE/new data for examination/Data_BrexitProject.xlsx")
my_data = my_data.dropna(axis=1)