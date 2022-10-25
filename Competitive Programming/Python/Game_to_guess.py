import random#importing random To get access to the random module

guessesTaken = 0#initializing values of guesses



myName = input("Hello! What is your name:")#asking user to enter name
x=(random.randint(0,25))#giving range to random variablt
print('Well, ' + myName + ', I am thinking of a number between 1 and 25.')
prime=[2, 3, 5, 7, 11, 13, 17, 19, 23]#creating a prime number set
if x in prime:
    print("The number is a prime number")#checking for prme number
elif x%2==0:
    print("The number is a even number")#checking for even number
else:
    print("The number is a odd number")#if not een then for odd number


while guessesTaken < 25: #using while loop for guess<26
    
    guess=int(input("Enter your guess number:"))#asking user to enter his/her guess

    guessesTaken = guessesTaken+1#incrementing number of guesses each time
    if guess < x:#if guess id smaller than the value
        print('Your guess is too low.')
    if guess > x:#when guess is higher than the value
        print('Your guess is too high.')
    if guess == x:#when he gusses correct value
        break#break the while loop
if guess == x:
    guessesTaken = str(guessesTaken)#the number of guesses to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')




