#!/usr/bin/env python
# coding: utf-8

# In[1]:


#20BCE0295

from random import randrange, seed
from math import sqrt

def knn(training, testing, neighbors):
    y_pred = list()
    for counter in testing:
        dist = list()
        for counter1 in training:
            temp = 0.0
            for counter2 in range(len(counter)-1):
                temp += (counter[counter2] - counter1[counter2])**2
            temp = sqrt(temp)
            dist.append((counter1, temp))
        dist.sort(key=lambda tup: tup[1])
        buffer = list()
        for counter in range(neighbors):
            buffer.append(dist[counter][0])
        temp = [counter[-1] for counter in buffer]
        temp = max(set(temp), key=temp.count)
        y_pred.append(temp)
    return(y_pred)

def knnalgo(dataset, algo, n, *args):
    subs = list()
    copy = list(dataset)
    t = int(len(dataset) / n)
    for counter in range(n):
        sub = list()
        while len(sub) < t:
            i = randrange(len(copy))
            sub.append(copy.pop(i))
        subs.append(sub)
    a = list()
    for sub in subs:
        training = list(subs)
        training.remove(sub)
        training = sum(training, [])
        testing = list()
        for counter in sub:
            copy = list(counter)
            testing.append(copy)
            copy[-1] = None
        y_pred = knn(training, testing, *args)
        y_data = [counter[-1] for counter in sub]
        temp = 0
        for counter in range(len(y_data)):
            if y_data[counter] == y_pred[counter]:
                temp += 1
        b = temp / float(len(y_data)) * 100.0
        a.append(b)
    return a

def prediction(training, testing, neighbors):
    y_pred = list()
    dist = list()
    for counter1 in training:
        temp = 0.0
        for counter2 in range(len(testing)-1):
            temp += (testing[counter2] - counter1[counter2])**2
        temp = sqrt(temp)
        dist.append((counter1, temp))
    dist.sort(key=lambda tup: tup[1])
    buffer = list()
    for counter in range(neighbors):
        buffer.append(dist[counter][0])
    temp = [counter[-1] for counter in buffer]
    y_pred = max(set(temp), key=temp.count)
    if y_pred==0:
        return 'Sentosa'
    elif y_pred==1:
        return 'Versicolor'
    if y_pred==2:
        return 'Virginica'
    

print('KNN')
dataset = [['5.1', '3.5', '1.4', '0.2', 'Setosa'], 
            ['4.9', '3', '1.4', '0.2', 'Setosa'], 
            ['5.4', '3.4', '1.7', '0.2', 'Setosa'], 
            ['5.1', '3.7', '1.5', '0.4', 'Setosa'],
            ['6.3', '2.3', '4.4', '1.3', 'Versicolor'], 
            ['5.6', '3', '4.1', '1.3', 'Versicolor'],
            ['6.9', '3.1', '4.9', '1.5', 'Versicolor'], 
            ['5.5', '2.3', '4', '1.3', 'Versicolor'], 
            ['7.7', '3.8', '6.7', '2.2', 'Virginica'], 
            ['7.7', '2.6', '6.9', '2.3', 'Virginica'],
            ['6.3', '2.7', '4.9', '1.8', 'Virginica'], 
            ['6.7', '3.3', '5.7', '2.1', 'Virginica']]
for counter in range(len(dataset[0])-1):
    for temp in dataset:
        temp[counter] = float(temp[counter].strip())
z = len(dataset[0])-1
classes = [counter[z] for counter in dataset]
diff = set(classes)
check = dict()
for counter1, counter2 in enumerate(diff):
    check[counter2] = counter1
for counter in dataset:
    counter[z] = check[counter[z]]
n = 3
seed(1)
neighbors = 3
a = knnalgo(dataset, knn, n, neighbors)
testingdata = [5.8, 2.1, 4.6, 1.8, None]
print('Accuracy:', (sum(a)/float(len(a))))
print("The prediction for", testingdata[0:len(testingdata)-1], "is", prediction(dataset, testingdata, neighbors))

