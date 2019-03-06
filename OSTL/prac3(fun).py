import random
import calendar
print("--------Powers of 2----------")
List1 = [1,2,3]
List2 = list(map(lambda x : x**2,List1))
print(List2)

print("------No divisible by another no-------")
n = int(input("Enter a number :"))
my_list = [12, 65, 54, 39, 102, 339, 221]
result = list(filter(lambda x: (x % n ==0),my_list))
print(result)

print("----Convert decimal to binary ,octal ,hexadecimal-------")
no = int(input("Enter a decimal no :"))
print(f"Binary :{bin(no)}")
print(f"Octal :{oct(no)}")
print(f"Hexadecimal :{hex(no)}")

print("-----Shuffle a deck of cards--------")
cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,'Jack', 'King', 'Queen']
pac = ['Hearts', 'Spades', 'Clubs' , 'Diamonds']
print(f"The card is a {random.choice(cards)} of {random.choice(pac)}")

print("-------Calender--------")
year = int(input("Enter year :"))
month = int(input("Enter month :"))
print(calendar.month(year,month))
 
print("------Fibonacci--------")
def Fib(n):
	if n == 1 or n == 0:
		return 1
	else :
		return Fib(n - 1)+ Fib(n - 2)
num = int(input("Enter num :"))
for i in range(num):
	print(Fib(i))
 '''
 --------Powers of 2----------
[1, 4, 9]
------No divisible by another no-------
Enter a number :13
[65, 39, 221]
----Convert decimal to binary ,octal ,hexadecimal-------
Enter a decimal no :36
Binary :0b100100
Octal :0o44
Hexadecimal :0x24
-----Shuffle a deck of cards--------
The card is a 7 of Clubs
-------Calender--------
Enter year :1999
Enter month :11
   November 1999
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30

------Fibonacci--------
Enter num :6
1
1
2
3
5
8
 '''