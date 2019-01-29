import calendar
import time
import random

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
print(calendar.month(year, month))
print(time.asctime(time.localtime(time.time())))



def shuffle():
    sign = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = ['Ace', 'Jack', 'King', 'Queen']
    for i in range(2,11):
        values.append(str(i))

    print(f"Your card is {random.choice(values)} of {random.choice(sign)}")

shuffle()
shuffle()
shuffle()
shuffle()
shuffle()
shuffle()

c = input("\nEnter a character: ")
print(f"ASCII value of {c} is {ord(c)}")
num = int(input("\nEnter a number: "))
print(f"Reverse ASCII value of {num} is {chr(num)}")


'''
Enter a year: 2185
Enter a month: 1
    January 2185
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

Thu Jan 24 13:59:09 2019

Your card is 10 of Clubs
Your card is Queen of Spades
Your card is 7 of Spades
Your card is 2 of Hearts
Your card is 3 of Clubs
Your card is 10 of Spades

Enter a character: e
ASCII value of e is 101

Enter a number: 69
Reverse ASCII value of 69 is E
'''
