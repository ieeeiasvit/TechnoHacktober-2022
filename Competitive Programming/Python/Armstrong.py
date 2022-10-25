
# Program to check Armstrong numbers in a certain interval
list1=[]
lower = int(input("Enter lower limit:"))#asking for lower interval
upper = int(input("Enter upper limit:"))#asking for upper interval

for num in range(lower, upper + 1):#for any number in range

   # order of number
   order = len(str(num))

   # initialize sum
   sum = 0

   temp = num
   while temp > 0:#when temp greater than 0
       digit=temp%10#reminder
       sum =sum+digit**order
       temp //= 10#temp=temp//10

   if num == sum:#if num is equal to sum
       list1.append(num)#appending to list1
print("the Armstrong number in the given range are:")
print(list1)




