import json
import pandas as pd
from collections import Counter


file = 'News_Category_Dataset_v2.json'

data = []

# load data using Python JSON module
with open(file, 'r') as f:
    for line in f:
        data.append(json.loads(line))

data = pd.DataFrame(data)

category_list = data["category"].tolist()

counter = Counter(category_list)

print(counter)

train_categories = ['TECH', 'SCIENCE', 'CRIME', 'SPORTS']

print(train_categories)

train_data = data[data['category'].isin(train_categories)]

train_data.to_csv("train_data.csv")

new_categories = ["RELIGION"]

new_data = data[data['category'].isin(new_categories)]

new_data.to_csv("new_data.csv")


