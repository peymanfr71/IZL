name = input("Waht's your name bro: ")
work = int(input('How many hours do you work a day? '))
per_hour = 100 #$
salary = work * 100
if salary < 200:
    print ('you earn $', salary, 'monthly, be careful!')
else:
    print ('you earn $', salary,  'monthly, good for you!')
# ##
# Q1: input a number from user, positive or negetive?
user = float(input('please enter the number: '))
if user > 0:
    print ("It's positive")
elif user < 0:
    print ("It's negetive")
elif user == 0:
    print ("ZERO")
else:
    print ("it is float")
# ##
user = int(input('please enter the number: '))
if user > 0:
    print ("It's positive")
elif user == 0:
    print ("ZERO")
else:
    print ("It's negetive")
# ##
number = int(input('Enter the number: '))
if number % 2 == 0:
    print (number, ": Is Even")
else:
    print (number, ": Is Odd")
# ##
score = int(input("Enter your score: "))
if score >= 90:
    print ("your score is equal to A.")
elif score >= 80:
    print ("your score is equal to B.")
elif score >= 70:
    print ("your score is equal to C.")
elif score >= 60:
    print ("youre score is equal to D.")
else:
    print ("your score is equal to E.")
# ##
score = int(input("Enter your score: "))
if score >= 90:
    print ("your score is equal to A.")
elif score >= 80:
    print ("your score is equal to B.")
elif score >= 70:
    print ("your score is equal to C.")
elif score >= 60:
    print ("youre score is equal to D.")
else:
    print ("your score is equal to E.")
# ##
grade = int(input("enter your score: "))
if grade >= 90:
    print ("your score is equal to A.")
elif 70 <= grade < 90:
    print ("your score is equal to B.")
elif 60 <= grade < 70:
    print ("your score is equal to C.")
elif 50 <= grade < 60:
    print ("youre score is equal to D.")
else:
    print ("your score is equal to E.")
