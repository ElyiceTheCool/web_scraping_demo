import pandas as pd

# Last updated: 08/22/23
stats = pd.read_csv("data\my_coaster_data.csv", header=0)
# print(stats.head)

# Cleaning
# TODO: Remove columns for future years
headers = stats.columns
headers = stats.rename(columns={'NAME': 'Name'}).drop(columns='<-INSERT HERE')
print(headers)


# Trials
models = stats.Type.unique()
# print(models)

# print(stats.Park.value_counts())