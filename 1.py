import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json

csv = pd.read_csv("./datasets/sales_data_sample.csv", encoding="cp1252")

ed = pd.read_excel("./datasets/Sample-Sales-Data.xlsx")

with open("./datasets/customers.json", "r") as json_file:
    json_data = json.load(json_file)

csv.tail()

csv.info()

csv.describe()

csv.dropna()

csv.drop_duplicates()

ed.head()

ed.tail()

ed.info()

ed.describe()

unified_data = pd.concat([csv, ed], ignore_index=True)

total_sales = unified_data['SALES'].sum()
print("Total Sales:", total_sales)

category_sales = unified_data.groupby('ORDERNUMBER')['SALES'].mean()

category_counts = unified_data['SALES'].value_counts()
category_counts.plot(kind='bar')
plt.title('Product Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()