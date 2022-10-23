import pandas as pd
import numpy as np
import math 

dataset = pd.read_csv('medoid.csv')
X = pd.DataFrame(dataset,columns=['X','Y'])

p= X.shape[0]/2
q= p+1
r=q+1
k=0

v1_x = X['X'][p]
v1_y = X['Y'][p]
v2_x = X['X'][q]
v2_y = X['Y'][q]
v3_x = X['X'][r]
v3_y = X['Y'][r]

l = []
def distance():
  row_list = []
  global v1_x
  global v1_y
  global v2_x
  global v2_y
  global v3_x
  global v3_y
  global k
  c_v1 = 0
  for i in range(X.shape[0]):
      dict1 = {}
      dis_v1 = abs(v1_x - X['X'][i]) + abs(v1_y - X['Y'][i])
      dis_v2 = abs(v2_x - X['X'][i]) + abs(v2_y - X['Y'][i])
      dis_v3 = abs(v3_x - X['X'][i]) + abs(v3_y - X['Y'][i])
      minimum = min(dis_v1,dis_v2)
      tup = (X['X'][i],X['Y'][i])
      cl = ""
      if(minimum == dis_v1):
        cl = 'v1'
        c_v1 = c_v1 + dis_v1
      elif(minimum == dis_v1):
        cl = 'v2'
        c_v1 = c_v1 + dis_v2
      else:
        cl = 'v3'
        c_v1 = c_v1 + dis_v3
      dict1.update({'point':tup,'V1':round(dis_v1,2),'V2':round(dis_v2,2),'V3':round(dis_v3,2),'cluster':cl})
      row_list.append(dict1)
  l.append(c_v1)
  data = pd.DataFrame(row_list)  
  print(data)
  print("Cost : ",c_v1)
  
  if(len(l) == 1):
    print("New V2 : ",X['X'][r+1],",",X['Y'][r+1])
    v2_x = X['X'][r+1]
    v2_y = X['Y'][r+1]
    distance()
  else:
    print("New V2 : ",X['X'][(r+k+2)%X.shape[0]],",",X['Y'][(r+k+2)%X.shape[0]])
    v2_x = X['X'][(r+k+2)%X.shape[0]]
    v2_y = X['Y'][(r+k+2)%X.shape[0]]
    if l[k] > l[1+k]:
      k=k+1
      distance()

print("Selected V1 : ",v1_x,",",v1_y)
print("Selected V2 : ",v2_x,",",v2_y)
print("Selected V3 : ",v3_x,",",v3_y)
distance()