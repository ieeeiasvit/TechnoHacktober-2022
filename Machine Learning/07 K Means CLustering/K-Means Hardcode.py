#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the Libraries

import pandas as pd
import numpy as np
import math 


# In[2]:


# Defining the dataset

X = list(map(int, '2, 2, 8, 5, 7, 6, 1, 4'.split(',')))
Y = list(map(int, '10, 5, 4, 8, 5, 4, 2, 9'.split(',')))
dataset = {'X': X, 'Y': Y}
data = pd.DataFrame(dataset,columns=['X','Y'])
print(data)


# In[3]:


# K-Means Algorithm with k = 2
def kmeans():
    global x_a1, x_a2, y_a1, y_a2, k
    x_a1_c, y_a1_c = 0, 0
    x_a2_c, y_a2_c = 0, 0
    k = 0
    rows = data.shape[0]
    row_list = []
    for counter in range(0, rows):
        dis1 = abs(data['X'][counter] - x_a1) + abs(data['Y'][counter] - y_a1)
        dis2 = abs(data['X'][counter] - x_a2) + abs(data['Y'][counter] - y_a2)
        min_dis = min(dis1, dis2)
        point = (data['X'][counter], data['Y'][counter])
        clustering = ""
        if (min_dis != dis1):
            clustering = 'A2'
            x_a2_c += data['X'][counter]
            y_a2_c += data['Y'][counter] 
        else:
            clustering = 'A1'
            x_a1_c += data['X'][counter]
            y_a1_c += data['Y'][counter]
        
        new_data = {}
        l.append(clustering)
        new_data.update({'Point':point,'Distance from V1':round(dis1, 2),'Distance from V2':round(dis2, 2),'Cluster':clustering})
        row_list.append(new_data)

    kdata = pd.DataFrame(row_list)  
    print(kdata)
    x_a1_c = x_a1_c/list(kdata.Cluster).count('A1')
    y_a1_c = y_a1_c/list(kdata.Cluster).count('A1')
    x_a2_c = x_a2_c/list(kdata.Cluster).count('A2')
    y_a2_c = y_a2_c/list(kdata.Cluster).count('A2')
    x_a1 = x_a1_c
    y_a1 = y_a1_c
    x_a2 = x_a2_c
    y_a2 = y_a2_c
    print("New Cluster Center A1 : (",round(x_a1_c, 2),",",round(x_a2_c, 2), ")")
    print("New Cluster Center A2 : (",round(x_a2_c, 2),",",round(y_a2_c, 2), ")\n")

    if(len(l) != rows):
        for counter in range(rows):
            if l[counter + k] != l[counter + rows + k]:
                k = rows
                kmeans();
                break        
    else:
        kmeans();


# In[4]:


# Declaring initial clusters

x_a1, y_a1 = data['X'][1], data['Y'][1]
x_a2, y_a2 = data['X'][2], data['Y'][2]
l = []

# Printing the Clusters

print("Initial Cluster Center A1 : (",x_a1,",",y_a1, ")")
print("Initial Cluster Center A2 : (",x_a2,",",y_a2, ")\n")
kmeans()

