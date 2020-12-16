import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statistics

tracker = pd.read_csv('activity.csv')
tracker["steps"].fillna(0)
dates = []
steps = []
for i in tracker['date'].unique():
    dates.append(i)
    steps.append(tracker.loc[tracker['date']==i, 'steps'].sum())

#Using bar graph as the dates corresponds with specific values of steps which is more reasonable to use a bar graph over a histogram.
plt.bar(dates, steps)
plt.xticks(rotation = 45, size=11)
plt.yticks(rotation = 45, size=11)
plt.xlabel('Dates')
plt.ylabel('Steps')
plt.title('Total Number of Steps Per Day')
plt.show()

steps_mean = statistics.mean(steps)
steps_median = statistics.median(steps)
print(f"Mean: {steps_mean}")
print(f"Median: {steps_median}")