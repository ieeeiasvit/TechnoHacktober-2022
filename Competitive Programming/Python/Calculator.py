x=input("What's your name:")#asking for name
print("Hey! "+ x +" choose any one of the given data type")
list1=["decimal", "float", "binary", "octal", "Hexadecimal"]#creating list of data types
print(list1)
y=input("Enter the data type:")#asking user to choose any one data type
print("""Select operation.
1.add  2.subtract  3.multiplication  4. division""")
z=input("Enter the operation name:")#asking user for operation name
num1=(input("Enter number 1:"))#asking for number1
num2=(input("Enter number 2:"))#asking user for number2
if y==list1[0]:#if user enters decimal then
    if z=="add":
        print(int(num1) + int(num2))#adding two decinal numbers
    if z=="subtract":
        print(int(num1) - int(num2))#subtracting two decinal numbers
    if z=="multiplication":
        print(int(num1) * int(num2))#multiplying two decinal numbers
    if z=="division":
        print(int(num1) / int(num2))#dividing two decinal numbers
elif y==list1[1]:#if user enters float then
    if z=="add":
        print(float(num1) + float(num2))#adding two float numbers
    if z=="subtract":
        print(float(num1) - float(num2))#subtracting two float numbers
    if z=="multiplication":
        print(float(num1) * float(num2))#multiplying two float numbers
    if z=="division":
        print(float(num1) / float(num2))#dividing two float numbers
elif y==list1[2]:#if user enters binary then
    if z=="add":
        print(bin(int(num1,2) + int(num2,2)))#adding two binary numbers
    if z=="subtract":
        print(bin(int(num1,2) - int(num2,2)))#subtracting two binary numbers
    if z=="multiplication":
        print(bin(int(num1,2) * int(num2,2)))#multiplying two binary numbers
    if z=="division":
        print(bin(int(num1,2) / int(num2,2)))#dividing two binary numbers
elif y==list1[3]:#if user enters octal then
    if z=="add":
        print(oct(int(num1, 8) + int(num2, 8)))#adding two octal numbers
    if z=="subtract":
        print(oct(int(num1, 8) - int(num2, 8)))#subtracting two octal numbers
    if z=="multiplication":
        print(oct(int(num1, 8) * int(num2, 8)))#multiplying two octal numbers
    if z=="division":
        print(oct(int(num1, 8) / int(num2, 8)))#dividing two octal numbers
elif y==list1[4]:#if user enters hexadecimal then
    if z=="add":
        print(hex(int(num1, 8) + int(num2, 8)))#adding two hexadecimal numbers
    if z=="subtract":
        print(hex(int(num1, 8) - int(num2, 8)))#subtracting two hexadecimal numbers
    if z=="multiplication":
        print(hex(int(num1, 8) * int(num2, 8)))#multiplying two hexadecimal numbers
    if z=="division":
        print(hex(int(num1, 8) / int(num2, 8)))#dividing two hexadecimal numbers
else:
    print("Ivalid input!! please check your input,try again")























