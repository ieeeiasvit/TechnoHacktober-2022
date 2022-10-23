#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


# In[2]:


#Loading Dataset
dataset = pd.read_csv("C:\\Users\\Harsha\\Desktop\\Machine Learning\\20BCE0295\\processed.cleveland.data.csv", names=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'output'])
dataset_mean = dataset


# In[3]:


#Data Preprocessing

#Filling missing values Statistics measures
print("*****Before Filling Missing values Row 166, 192, 287, 302*****")
print(dataset_mean.loc[287])
dataset1 = dataset_mean
df1 = pd.DataFrame(dataset1)

print("----- Mean of Column 11 'ca' -----")
print(df1['ca'].mean())
df1.fillna(df1.mean(), inplace=True)
print("*****After Filling Missing values Row 166, 192, 287, 302*****")
print(df1.loc[[166, 192, 287, 302]])

print("----- Mean of Column 12 'thal' -----")
print(df1['thal'].mean())
df1.fillna(df1.mean(), inplace=True)
print("*****After Filling Missing values Row 87, 266*****")
print(df1.loc[[87, 266]])


# In[4]:


#Dataset Description

#Number of patients
n_patients = dataset.shape[0]

#Number of features
n_features = dataset.shape[1]-1

dataset["output"].replace(to_replace=[1, 2, 3, 4], value=1, inplace=True)

#With Heart Disease
heart_disease = dataset[dataset['output'] == 1].shape[0]

#Without Heart Disease
no_heart_disease = dataset[dataset['output'] == 0].shape[0]

#Printing Results
print("Total number of patients: {}".format(n_patients))
print("Number of features: {}".format(n_features))
print("Number of patients with Heart Disease: {}".format(heart_disease))
print("Number of patients without Heart Disease: {}".format(no_heart_disease))


# In[5]:


#Extracting feature columns
feature_cols = list(dataset.columns[0:13])

#Showing the list of columns
print("Feature columns: \n{}".format(feature_cols))


# In[6]:


#Separate the data into feature data and target data (X_all and y_all, respectively)
X = dataset[feature_cols]
y = dataset['output'].values

#Showing the feature information by printing the first five rows
print("\nFeature values:")
X.head()


# In[7]:


#Splitting the Dataset into Training and Testing data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)
print(X_train)


# In[8]:


#The dimension of Training and Testing Data

print(X_train.shape)
print(X_test.shape)


# In[9]:


#Normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X_train)
X_train = scaler.transform(X_train)
print("----- After Z-score Normalization on X_train -----")
print(X_train)

scaler.fit(X_test)
X_test = scaler.transform(X_test)
print("----- After Z-score Normalization on X_test -----")
print(X_test)


# In[10]:


#K-Means Algorithm
print("K-Means")
print("Enter the number of clusters:")
k = int(input())
model = KMeans(n_clusters=k, random_state=0).fit(X)
ypredictions = model.predict(X_test)
print("Accuracy =", accuracy_score(ypredictions, y_test))


# In[11]:


#K-Medoids Algorithm
print("K-Medoids")
print("Enter the number of clusters:")
k = int(input())
model = KMedoids(n_clusters=k, random_state=0).fit(X)
ypredictions = model.predict(X_test)
print("Accuracy =", accuracy_score(ypredictions, y_test))

