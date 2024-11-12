import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./datasets/Telcom_Customer_Churn.csv")
print(data.index)

print(data)

data.shape 

print(data.head())

data.nunique()

data.isna().sum()

data.isnull().sum()

print("Number of rows before removing duplicates:", len(data))

data_cleaned = data.drop_duplicates()

data_cleaned = data.drop_duplicates()

data.describe()

unique, counts = np.unique(data['tenure'], return_counts=True) 
print(unique, counts)

unique, counts = np.unique(data['MonthlyCharges'], return_counts=True) 
print(unique, counts)

unique, counts = np.unique(data['TotalCharges'], return_counts=True) 
print(unique, counts)

sns.pairplot(data)

plt.boxplot(data['tenure'])
plt.show()

plt.boxplot(data['MonthlyCharges']) 
plt.show()

X = data.drop("Churn", axis=1) 
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.shape 

y_train.shape 

X_test.shape 

y_test.shape 

data.to_csv("./datasets/Cleaned_Telecom_Customer_Churn.csv", index=False)