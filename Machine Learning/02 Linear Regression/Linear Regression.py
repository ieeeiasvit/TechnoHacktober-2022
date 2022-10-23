#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The first step is to import the package numpy and the class Linear Regression from sklearn

import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


# Linear Regression with scikit learn (With Dataset - 1)

# Training Dataset
x_new1 = np.array([3, 8, 9, 13, 3, 6, 11, 21, 1, 16]).reshape((-1, 1))
y_new1 = np.array([30, 57, 64, 72, 36, 43, 59, 90, 20, 83])

new_model1 = LinearRegression().fit(x_new1, y_new1)

# Intercept, Slope and Equation
print("Intercept:", new_model1.intercept_)
print("Slope:", new_model1.coef_)
print("Equation: y = {0} + {1}x".format(new_model1.intercept_, new_model1.coef_))

# Model Testing
x = np.array([10])
y_pred = new_model1.predict(x.reshape((-1, 1)))
print("Salary of college graduate with 10 years of experience:", y_pred*1000)


# In[3]:


# Linear Regression with scikit learn (With Dataset - 2)

# Training Dataset
x_new2 = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]).reshape((-1, 1))
y_new2 = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])

new_model2 = LinearRegression().fit(x_new2, y_new2)

# Intercept, Slope and Equation
print("Intercept:", new_model2.intercept_)
print("Slope:", new_model2.coef_)
print("Equation: y = {0} + {1}x".format(new_model2.intercept_, new_model2.coef_))

# Model Testing
x = np.array([2000])
y_pred = new_model2.predict(x.reshape((-1, 1)))
print("A House with 2000 square feet costs $", y_pred*1000)


# In[4]:


# Linear Regression without scikit learn (With Dataset - 1)

# Training Dataset
x = np.array([3, 8, 9, 13, 3, 6, 11, 21, 1, 16])
y = np.array([30, 57, 64, 72, 36, 43, 59, 90, 20, 83])

# Calculating Mean of X and Y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Finding the Slope of the Linear Line
w1 = np.sum((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2)

# Finding the Intercept Value
w0 = y_mean - w1*x_mean

# Intercept, Slope and Equation
print("Intercept:", w0)
print("Slope:", w1)
print("Equation: y = {0} + {1}x".format(w0, w1))

# Model Testing
y_pred = w0 + w1*10
print("Salary of college graduate with 10 years of experience:", y_pred*1000)


# In[5]:


# Linear Regression without scikit learn (With Dataset - 2)

# Training Dataset
x = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
y = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])

# Calculating Mean of X and Y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Finding the Slope of the Linear Line
w1 = np.sum((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2)

# Finding the Intercept Value
w0 = y_mean - w1*x_mean

# Intercept, Slope and Equation
print("Intercept:", w0)
print("Slope:", w1)
print("Equation: y = {0} + {1}x".format(w0, w1))

# Model Testing
y_pred = w0 + w1*2000
print("A House with 2000 square feet costs $", y_pred*1000)

