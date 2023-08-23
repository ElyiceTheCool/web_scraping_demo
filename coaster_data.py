import pandas as pd

# Last updated: 08/22/23
stats = pd.read_csv("data\my_coaster_data.csv", header=0)
# print(stats.head)

headers = stats.columns
print(headers)

models = stats.Type.unique()
# print(models)

print(stats.Park.value_counts())