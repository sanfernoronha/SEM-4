print("----------No is positive ,negative or zero-----------\n")
def check(p):
	if p > 0:
		print(f"{p} is a positive no")
	elif p < 0:
		print(f"{p} is a negative no")
	else:
		print(f"{p} is zero")

check(10)
check(-19)
check(0)

print("------No is odd or even------\n")
def even_odd(p):
	if(p%2 == 0):
		print(f"{p} is a even no")
	else :
		print (f"{p} is a odd no")

p = int(input("Enter a no: "))
even_odd(p)


print("--------Check for leap year------------\n")
def check_leap(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
		print(f"{year} is a leap year\n")
	else:
		print(f"{year} not a leap year")

year = int(input("Enter a year :"))
check_leap(year)


print("------largest among 3 no------\n")
def largest(a,b,c):
	if a > b :
		if a > c:
			print (f"MAX = {a}")
		else :
			print (f"MAX = {c}")
	else :
		if b > c :
			print (f"MAX = {b}")
		else :
			print(f"MAX = {c}")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
largest(a,b,c)

print("---------check prime no---------")
def check_prime(n):
    check = False
    if n == 2:
        check = False
    else:
        for i in range(2,n):
            if n % i == 0:
                check = True
                break
    if check:
        print(f"{n} is not a prime no")
    else:
        print(f"{n} is a prime no")


check_prime(2)
check_prime(25)
check_prime(13)

print("-------Count vowels and consonants---------\n")
def count(string):
    countV = 0
    vowelList ='aeiou'
    string = string.lower()
    for letter in string:
        if letter in vowelList:
            countV = countV + 1
    countC = len(string) - countV
    print(f"Total no of vowels :{countV} and consonants :{countC}")

count('abcdifg')


print("-------Quadratic equ-------\n")
def quadratic(a,b,c):
	d = b*b - 4 *a*c
	x = (-b/(2.0*a))
	if (d >= 0):
		a1 = x + (pow(d,0.5)/(2.0*a))
		a2 = x -(pow(d,0.5)/(2.0*a))
		print (f"Roots are :{a1} & {a2}")
	else :
		print("There are no real solutions")


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
quadratic(a,b,c)

print("------Sorting a list-----------\n")
list1 = [3,4,9,1,7,6,0]
for i in range(len(list1)):
	for j in range(i):
		if list1[j] > list1[j+1]:
			temp =list1[j]
			list1[j] = list1[j+1]
			list1[j+1] = temp

print(list1)

print("----Searching in a list---------\n")
list1 = [3,4,9,1,7,6,0]
s = int(input("Enter ele to be searched :"))
if s in list1:
    print("Element present in list")
else :
    print("Element not present")

print("-----Search and return the index----------\n")
def search(list1, ele):
	for index,value in enumerate(list1):
		if(ele == value):
			return index
		else :
			pass
	return -1
list1 = [3,4,9,1,7,6,0]
s = int(input("Enter ele to be searched :"))
val = search(list1,s)
if(val != -1):
	print(f"{s} found at index {val}")
else:
	print("Element not found ")

'''
----------No is positive ,negative or zero-----------

10 is a positive no
-19 is a negative no
0 is zero
------No is odd or even------

Enter a no: 16
16 is a even no
--------Check for leap year------------

Enter a year :2025
2025 not a leap year
------largest among 3 no------

Enter a:12
Enter b:45
Enter c:89
MAX = 89
---------check prime no---------
2 is a prime no
25 is not a prime no
13 is a prime no
-------Count vowels and consonants---------

Total no of vowels :2 and consonants :5
-------Quadratic equ-------

Enter a:1
Enter b:2
Enter c:3
There are no real solutions
------Sorting a list-----------

[1, 3, 4, 6, 7, 0, 9]
----Searching in a list---------

Enter ele to be searched :5
Element not present
-----Search and return the index----------

Enter ele to be searched :3
3 found at index 0
'''