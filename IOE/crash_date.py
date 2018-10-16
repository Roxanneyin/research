import numpy as np
import pandas as pd

data = pd.read_csv("NDAQ02-08.csv")
adj_close = data.ix[:,5]; date = data.ix[:,0]
diff = [(adj_close[i+1]-adj_close[i]) for i in range(len(adj_close)-1)]
# the length of diff should be len(adj_close)-1 then the crash date should be i+1 with i in diff
for i in range(len(diff)):
    if (- diff[i]/adj_close[i]) >= 0.15:
        print(date[i+1])