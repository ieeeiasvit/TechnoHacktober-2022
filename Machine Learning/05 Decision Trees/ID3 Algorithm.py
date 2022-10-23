#!/usr/bin/env python
# coding: utf-8

# In[1]:


#20BCE0295
#Importing the libraries

import pandas as pd
import numpy as np


# In[2]:


#Reading the Dataset

Outlook = 'sunny,sunny,overcast,rain,rain,rain,overcast,sunny,sunny,rain,sunny,overcast,overcast,rain'.split(',')
Temperature = 'hot,hot,hot,mild,cool,cool,cool,mild,cool,mild,mild,mild,hot,mild'.split(',')
Humidity = 'high,high,high,high,normal,normal,normal,high,normal,normal,normal,high,normal,high'.split(',')
Wind = 'weak,strong,weak,weak,weak,strong,strong,weak,weak,weak,strong,strong,weak,strong'.split(',')
Label = 'no,no,yes,yes,yes,no,yes,no,yes,yes,yes,yes,yes,no'.split(',')
dataset ={'Outlook':Outlook,'Temperature':Temperature,'Humidity':Humidity,'Wind':Wind,'Label':Label}
dataset = pd.DataFrame(dataset,columns=['Outlook','Temperature','Humidity','Wind','Label'])
prediction = 'yes'
li = ['Outlook', 'sunny', 'Humidity', 'normal', 'overcast', 'rain', 'Wind', 'weak', 'yes']


# In[3]:


#Calculating the entropy of the whole dataset

def entropycalculation(dataset, label, classes):
    rows = dataset.shape[0]
    entropy = 0
    
    for counter in classes :
        count = dataset[dataset[label] == counter].shape[0]
        entropytemp = -(count/rows)*np.log2(count/rows)
        entropy += entropytemp
            
    return entropy


# In[4]:


#Calculating the entropy of the filtered dataset

def entropycalc(data, label, classes):
    entropy = 0
    count = data.shape[0]
    
    for counter in classes : 
        labelcount = data[data[label] == counter].shape[0]
        entropytemp = 0
        if labelcount != 0:
            probclass = labelcount/count
            #probability of the class
            entropytemp = -(probclass)*np.log2(probclass)
            #entropy 
        entropy += entropytemp
        
    return entropy


# In[5]:


#Calculating information gain for a feature

def infogaincalc(feature, dataset, label, classes):    
    infogain = 0.0
    rows = dataset.shape[0]
    examples = dataset[feature].unique() 
        
    for value in examples:
        data = dataset[dataset[feature] == value] 
        count = data.shape[0]
        probability = count/rows
        entropy = entropycalc(data, label, classes)         
        infogain =  infogain + entropy * probability
    
    gain = entropycalculation(dataset, label, classes) - infogain
    print("Information Gain of", feature, ":", gain )
    return gain


# In[6]:


#Finding the attribute with the max information gain

def maxgainfeature(dataset, label, classes, depth):
    maxfeature = None
    maxgain = -1
    features = dataset.columns.drop(label)       
    
    print("Depth", depth)
    depth = depth + 1
    for feature in features:
        infogain = infogaincalc(feature, dataset, label, classes)
        if maxgain < infogain:
            maxfeature = feature
            maxgain = infogain            
     
    print("Max gain at this depth is", maxfeature, "with gain =", maxgain, "\n")
    return maxfeature, depth


# In[7]:


#Adding a node to the tree

def subtree(feature, dataset, label, classes):
    dictfeature = dataset[feature].value_counts(sort=False) 
    tree = {}
    
    for value, count in dictfeature.iteritems():
        node = False 
        data = dataset[dataset[feature] == value]                 
        
        for counter in classes:
            classcount = data[data[label] == counter].shape[0] 
            if classcount == count: 
                node = True                
                dataset = dataset[dataset[feature] != value] 
                tree[value] = counter                 
                
        if not node:
            tree[value] = "?" 
            
    return tree, dataset


# In[8]:


#Decision Tree Generation

def decisiontree(root, prevalue, dataset, label, classes, depth):
    
    if dataset.shape[0] != 0: 
        maxfeature, depth = maxgainfeature(dataset, label, classes, depth) 
        tree, dataset = subtree(maxfeature, dataset, label, classes) 
        nextroot = None
        
        if prevalue != None: 
            root[prevalue] = dict()
            root[prevalue][maxfeature] = tree
        
        else: 
            root[maxfeature] = tree
        
        nextroot = tree        
        for node, branch in list(nextroot.items()): 
            if branch == "?":
                data = dataset[dataset[maxfeature] == node] 
                decisiontree(nextroot, node, data, label, classes, depth) 


# In[9]:


#ID3 Function

def id3algo(dataset_t, label):
    datasettemp = dataset.copy()
    tree = {}
    depth = 1
    classes = datasettemp[label].unique()
    decisiontree(tree, None, dataset, label, classes, depth)
    return tree


# In[10]:


#Printing the Tree

tree = id3algo(dataset, 'Label')
print("The Root node of the Decision Tree is", list(tree.keys())[0], "\n")
print("Inference Rule:")
print("({0} = {1} ^ {2} = {3}) V ({0} = {4}) V ({0} = {5} ^ {6} = {7}) for {8} \n".format(li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7], li[8]))
print("Decision Tree:")
print(tree)
print("\nThe output for Overcast, Hot, High, Weak is", prediction)


# In[ ]:




