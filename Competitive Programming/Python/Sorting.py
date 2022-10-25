# -*- coding: utf-8 -*-
"""
SORTING
"""
# list1=[1,3,5,7,96,6,33]
# list1.sort()#sort function
# print(list1)

# list1=[1,3,5,7,96,6,33]
# list1.sort(reverse=True)#reversing
# print(list1)

# def choice(value):#defining the function
#     return value[2]#using index value 2 to sort
# list1=[(1,99,88),(5,7,8),(14,55,66)]
# list1.sort(key=choice)
# print(list1)


"""sorting lists"""

# lst=["Shreya","Srishti","Om","rekha","kanhaiya"]
# lst.sort()#sorting 
# print(lst)

# lst=["Shreya","Srishti","Om","rekha","kanhaiya"]
# lst.sort(reverse=True)#in reverse order
# print(lst)

# for i in sorted(lst, reverse = True): #using for loop
#     print(i)

"""Sorting by lenght"""

# lst=["Shreya","Srishti","Om","rekha","kanhaiya"]
# lst.sort(key=len)#sorting through length
# print(lst)

# dict ={ 
#     "L1":[87, 34, 56, 12],
#     "L2":[23, 00, 30, 10],
#     "L3":[1, 6, 2, 9],
#     "L4":[40, 34, 21, 67]
# }

# for i,j in dict.items():#calling each item
#     sorted_dict={i:sorted(j)}#sorting each keys element 
#     print(sorted_dict)


# dict ={ 
# "L1":["Python","for","Freshers"], 
# "L2":["I","Love","Python"], 
# "L3":["VIT","Uniersity","Vellore"], 
# } 
# for i,j in dict.items():
#     chikki={i:sorted(j)}#sorting each element
#     print(chikki)

"""dictionary sorting from second element"""
# def sortchoice(value):#definingthe function
#     return value[1]#using index value 1 to sort
# sub_li=[['rishav',10],['akash',5],['ram',20],['gaurav',15]]
# sub_li.sort(key=sortchoice)
# print(sub_li)

"""OR"""

# def Sort(sub_li):
#     sub_li.sort(key=lambda x:x[1])#using lambda function to sort with inder 1
#     return sub_li
# sub_li=[['rishav',10],['akash',5],['ram',20],['gaurav',15]]
# print(Sort(sub_li))

# def myFunc(e):#defining the function
#   return len(e)#returning
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(reverse=True, key=myFunc)#reverse sorting
# print(cars)


def myFunc(e):
  return e['year']
cars=[
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

