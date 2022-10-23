#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib.pyplot

# Use Matplotlib in jupyter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Input data - [X coordinate, Y coordinate]
X = np.array([[1.6,0.3], [1.8,0.5], [2.0,0.7], [2.2,0.4], [2.4,0.6], [2.3,0.5], [2.1,0.5],
              [1.7,1.7], [2.5,1.0], [1.0,3.0], [2.0,1.5], [1.5,1.5], [1.5,2.0], [1.0,2.5],
              [1.6,1.6], [2.4,0.9], [0.9,2.9], [1.9,1.4], [1.0,1.4], [1.4,1.9], [0.9,2.4],
              [1.5,1.7], [2.3,1.1], [0.4,1.0], [1.0,0.7], [1.2,1.5], [1.2,1.0], [1.0,1.1],
              [1.0,1.7], [1.3,1.1], [0.7,1.0], [0.4,0.7], [0.2,1.5], [0.2,1.0], [0.4,1.1],
              [1.0,0.5], [1.3,0.1], [0.7,0.3], [0.4,0.4], [0.2,0.5], [0.2,0.1], [0.4,0.1],
              [1.0,2.4], [1.3,2.1], [0.7,2.0], [0.4,2.7], [0.2,2.5], [0.2,2.0], [0.4,2.1],
              [3.4,2.0], [3.5,2.1], [3.6,2.3], [3.4,2.4], [3.5,2.5], [3.1,2.6], [3.3,2.7],
              [2.0,3.1], [3.5,1.0], [4.0,1.5], [3.0,3.0], [3.0,2.0], [2.5,2.5], [3.3,1.5],
              [3.9,2.5], [3.9,2.0], [3.8,3.0], [3.8,2.9], [3.9,2.7], [3.9,2.5], [3.9,2.7],
              [2.1,3.1], [3.6,1.1], [3.8,1.7], [3.2,3.1], [2.9,2.1], [2.6,2.4], [3.2,1.4],
              [4.0,0.1], [3.9,0.2], [3.9,0.3], [3.7,0.5], [3.9,0.7], [3.9,0.4], [3.7,0.4]])

# Labels (1 or -1)
Y = np.array([-1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1])


# In[3]:


# For every point mark point with '-' if label is '-1' and mark with '+' if label is '1'
for i in range(len(X)): #for loop
    if Y[i] == -1: #if statement to check the required condition
        plt.scatter(X[i][0], X[i][1], s=120, marker='_', linewidths=2)
    else: #else statement
        plt.scatter(X[i][0], X[i][1], s=120, marker='+', linewidths=2) 
        
# Red line is how it will look like...
plt.plot([3.6,1.5],[0.0,3.0],'r') #plt.plot() to plot the graph


# In[4]:


def train_svm(X, Y, epochs=10000): #define train_svm
    #Initialize our SVMs weight vector with zeros (3 values)
    w = np.zeros(len(X[0]))

    # The learning rate
    learning_rate = 1
    
    # See the change
    w0_per_epoch = []
    w1_per_epoch = []
    
    # Training
    print("starts training")
    for epoch in range(1, epochs): #outer for loop
        error = 0
        for i, x in enumerate(X): #inner for loop
            # It there is an error
            if (Y[i] * np.dot(X[i], w)) < 1: #if statement to check the required condition
                w = w + learning_rate * ((X[i] * Y[i]) + (-2 * (1/epochs) * w))
            else: #else statement
                w = w + learning_rate * (-2 * (1/epochs) * w)
                
        w0_per_epoch.append(w[0])
        w1_per_epoch.append(w[1])
    
    return w, w0_per_epoch, w1_per_epoch #to return the required values


# In[5]:


w, w0array, w1array = train_svm(X, Y, epochs=10000)
print(w) #print w


# In[6]:


# You cannot see anything in the graph of 10000 numbers!
epochs = len(w0array)

# It will divide epochs to this number
number_of_weights_to_graph = 100

num_per_epoch = epochs/number_of_weights_to_graph

w0_to_graph = [] 
w1_to_graph = []
epoch_to_graph = []

for i in range(number_of_weights_to_graph): #for loop to do the processing
    epoch_to_graph.append(int(num_per_epoch*i))
    w0_to_graph.append(w0array[int(num_per_epoch*i)])
    w1_to_graph.append(w1array[int(num_per_epoch*i)])
    
plt.plot(epoch_to_graph, w0_to_graph, 'r',epoch_to_graph, w1_to_graph,'b') #plt.plot() to plot the graph


# In[7]:


# Input data - [X coordinate, Y coordinate]
X = np.array([[1.6,0.3], [1.8,0.5], [2.0,0.7], [2.2,0.4], [2.4,0.6], [2.3,0.5], [2.1,0.5],
              [1.7,1.7], [2.5,1.0], [1.0,3.0], [2.0,1.5], [1.5,1.5], [1.5,2.0], [1.0,2.5],
              [1.6,1.6], [2.4,0.9], [0.9,2.9], [1.9,1.4], [1.0,1.4], [1.4,1.9], [0.9,2.4],
              [1.5,1.7], [2.3,1.1], [0.4,1.0], [1.0,0.7], [1.2,1.5], [1.2,1.0], [1.0,1.1],
              [1.0,1.7], [1.3,1.1], [0.7,1.0], [0.4,0.7], [0.2,1.5], [0.2,1.0], [0.4,1.1],
              [1.0,0.5], [1.3,0.1], [0.7,0.3], [0.4,0.4], [0.2,0.5], [0.2,0.1], [0.4,0.1],
              [1.0,2.4], [1.3,2.1], [0.7,2.0], [0.4,2.7], [0.2,2.5], [0.2,2.0], [0.4,2.1],
              [3.4,2.0], [3.5,2.1], [3.6,2.3], [3.4,2.4], [3.5,2.5], [3.1,2.6], [3.3,2.7],
              [2.0,3.1], [3.5,1.0], [4.0,1.5], [3.0,3.0], [3.0,2.0], [2.5,2.5], [3.3,1.5],
              [3.9,2.5], [3.9,2.0], [3.8,3.0], [3.8,2.9], [3.9,2.7], [3.9,2.5], [3.9,2.7],
              [2.1,3.1], [3.6,1.1], [3.8,1.7], [3.2,3.1], [2.9,2.1], [2.6,2.4], [3.2,1.4],
              [4.0,0.1], [3.9,0.2], [3.9,0.3], [3.7,0.5], [3.9,0.7], [3.9,0.4], [3.7,0.4]])

# Labels (1 or -1)
Y = np.array([-1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1])


# For every point mark point with '-' if label is '-1' and mark with '+' if label is '1'
for i in range(len(X)): #for loop
    if Y[i] == -1: #if statement to check the required condition
        plt.scatter(X[i][0], X[i][1], s=120, marker='_', linewidths=2)
    else: #else statement
        plt.scatter(X[i][0], X[i][1], s=120, marker='+', linewidths=2)

# Print the hyperplane calculated by svm_sgd()
x2=[w[0]*0.65,w[1],-w[1],w[0]]
x3=[w[0]*0.65,w[1],w[1],-w[0]]

#final graph with the required "optimal hyperplane" seperating the positive and negative samples
x2x3 =np.array([x2,x3])
X,Y,U,V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X,Y,U,V,scale=1, color='blue')


# In[ ]:




