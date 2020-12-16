import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

tracker = pd.read_csv('activity.csv')
tracker["steps"].fillna(0) 
intervals = []
steps = []
for i in tracker['interval'].unique():
    intervals.append(i)
    steps.append(tracker.loc[tracker['interval']==i, 'steps'].mean())

plt.plot(intervals, steps)
plt.xlabel('Intervals')
plt.ylabel('Steps')
plt.title('Average Steps Every 5 Minutes')
plt.show()

print(f"The Inverval with the max average steps: .")