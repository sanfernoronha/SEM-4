list = [2, 4, 7, 1, 6]
print ("Elements in list", list)
for num in list:
    print(num, end=' ')
print()
sum = 0;
for ele in list:
    sum = sum + ele
print (f"Sum is {sum}")

print ("\nFactorial")
n = int(input("Enter number for factorial--> "))
fact = 1;
while(n>0):
    fact = fact*n
    n = n-1
print (f"Factorial is {fact}")

arr = {}
print ("\nArray")
for ele in range(0,5):
    arr[ele] = int(input("Enter value--> "))

for num in arr:
    print(arr[num], end=' ')
print()

print("\nTuple unpacking")
tu = [(1,2), (5,6), (9,10)]

for a,b in tu:
    print(a,b)

print("\nDictonary")

d = {'k1': 1, 'k2': 2, 'k3': 3}

print("Normal, for loop for Dict")
for ele in d:
    print(ele)
print("Tuple conversion, for loop for Dict")
for ele in d.items():
    print(ele)
print("Tuple unpacking, for loop for Dict")
for key, val in d.items():
    print(val)
print("Printing values directly, for loop for Dict")
for val in d.values():
    print(val)

'''
Elements in list [2, 4, 7, 1, 6]
2 4 7 1 6
Sum is 20

Factorial
Enter number for factorial--> 4
Factorial is 24

Array
Enter value--> 2
Enter value--> 3
Enter value--> 4
Enter value--> 5
Enter value--> 6
2 3 4 5 6

Tuple unpacking
1 2
5 6
9 10

Dictonary
Normal, for loop for Dict
k1
k2
k3
Tuple conversion, for loop for Dict
('k1', 1)
('k2', 2)
('k3', 3)
Tuple unpacking, for loop for Dict
1
2
3
Printing values directly, for loop for Dict
1
2
3
'''
