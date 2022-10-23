#!/usr/bin/env python
# coding: utf-8

# In[1]:


#20BCE0295

from math import sqrt
from math import exp
from math import pi

def standard_deviation(numbers):
    avg = sum(numbers)/float(len(numbers))
    var = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return sqrt(var)

def classification(dataset):
    sep = dict()
    temp = dict()
    for counter in range(len(dataset)):
        buffer = dataset[counter]
        classes = buffer[-1]
        if (classes not in sep):
            sep[classes] = list()
        sep[classes].append(buffer)
    for classes, counter1 in sep.items():
        buffer = [(sum(counter2)/float(len(counter2)), standard_deviation(counter2), len(counter2)) for counter2 in zip(*counter1)]
        del(buffer[-1])
        temp[classes] = buffer
    return temp

def predict(buffer, temp):
    probs = dict()
    rows = sum([buffer[counter][0][2] for counter in buffer])
    for classes, classbuff in buffer.items():
        probs[classes] = buffer[classes][0][2]/float(rows)
        for counter in range(len(classbuff)):
            mean, standard_deviation, _ = classbuff[counter]
            if standard_deviation != 0:
                exponent = exp(-((temp[counter]-mean)**2 / (2 * standard_deviation**2 )))
                probs[classes] *= (1 / (sqrt(2 * pi) * standard_deviation)) * exponent
            else:
                probs[classes] *= 1
    hprob = -1
    label = None
    for classes, prob in probs.items():
        if label is None or prob > hprob:
            label = classes
            hprob = prob
    if label == 1:
        label = "Virginica"
    elif label == 2:
        label = "Versicolor"
    elif label == 3:
        label = "Setosa"
    return label

print("Naive Bayes Classifier")
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
for counter1 in range(len(dataset[0])-1):
    for temp in dataset:
        temp[counter1] = float(temp[counter1].strip())
classes = [temp[len(dataset[0])-1] for temp in dataset]
diff = set(classes)
check = dict()
for counter1, counter2 in enumerate(diff):
    check[counter2] = counter1+1
for temp in dataset:
    temp[len(dataset[0])-1] = check[temp[len(dataset[0])-1]]
train = classification(dataset)

test = [5.7,2.9,4.2,1.3]
pred = predict(train, test)
print("The prediction for", test, "is", predict(train, test))

