# """Binary,Octal,Hexadecimal conversions"""

# print(bin(55))#in binary
# print(hex(55))#in hexadecimal
# print(oct(55))#in octal

# print(oct(22)+oct(32))
# print(bin(22)+bin(99))
# print(hex(67)+hex(99))


# print("The octal representation of the binary"
# " of 23 is " + oct(0b10111))

# print("The hexadecimal form of 23 is"
# + hex(23))

# dec = 344
# print("The decimal value of", dec, "is:")
# print(bin(dec), "in binary.")
# print(oct(dec), "in octal.")
# print(hex(dec), "in hexadecimal.")

#Addition in binary
a=int(input("Enter the decimal number 1: "))
b=int(input("Enter the decimal number 2: "))
a=bin(a)#binary of number 1
b=bin(b)#binary of number2
sum=int(a,2)+int(b,2)#adding them
print(a,b,bin(sum))



#Addition in hexadecimal
num1=int(input("Enter the decimal number 1:"))
num2=int(input("Enter the decimal number 1:"))
c=hex(num1)#hexadecimal of number 1
d=hex(num2)#hexadecimal of number 2
mysum=int(c,16)+int(d,16)
print(hex(mysum))

#Addition in Octal

num3=int(input("Enter the decimal number 1: "))
num4=int(input("Enter the decimal number 2: "))
x=oct(num3)#octal of number 1
y=oct(num4)#octal of number 2
mysum=int(x,8)+int(y,8)
print(oct(mysum))
