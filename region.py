import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./datasets/customer_shopping_data.csv") 
df.head()

	
df.tail()

df.groupby("shopping_mall").count()

df.groupby("category").count()

branch_sales = df.groupby("shopping_mall").sum()
branch_sales

category_sales = df.groupby("category").sum()
category_sales

branch_sales.sort_values(by = "price", ascending = False)

category_sales.sort_values(by = "price", ascending = False)

mbined_branch_category_sales = df.groupby(["shopping_mall", "category"]).sum()
combined_branch_category_sales

plt.pie(branch_sales["price"], labels = branch_sales.index) 
plt.show()

plt.pie(category_sales["price"], labels = category_sales.index) 
plt.show()

combined_pivot = df.pivot_table(index="shopping_mall", columns="category", values="price", aggfunc="sum") 

combined_pivot.plot(kind="bar", figsize=(10, 6)) 
plt.show()