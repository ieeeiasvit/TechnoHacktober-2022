
list1=[]#empty list
i=0#initializing
a=100
while i<=a:#when i is less than 100
    print('Enter the string:')
    user_input=str(input())#asking user to input the string
    if user_input!='X':#when user input is not equal to X
        list1.append(user_input)#appending to list1
        print('Enter to continue or X to quit')
        i=i+1#incrementing
    else:
        print('You have chosen to quit')
        break
print(list1)
#using lambda function and filter
result = list(filter(lambda x: (x == "".join(reversed(x))),list1))#checking for pallindrom
print("\nList of palindromes:")
print(result)


