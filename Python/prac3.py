num = int(input("Enter number: " ))


print("\nMultiplication Table")
def mult(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
mult(num)

print("\nFibonacci")
def fib(n):
    n1 = 0
    n2 = 1
    print("Series", end = ' ')
    print(f"{n1} {n2}", end = ' ')
    for i in range(1, n):
        sum = n1 + n2
        n1 = n2
        n2 = sum
        print(f"{sum}", end = ' ')
    return sum

print(f"\nFibonacci addition of {num} is {fib(num)}")

print("\nFactorial")
def fact(num):
    if(n == 0):
        return 1
    else:
        return n*fact(n - 1)
print(f"Factorial of {num} is {fact(num)}")

print("\nPrime")
def prime(n):
    check = False
    for i in range(1,n):
        if(n%i != 0):
            check = True
            break
    if(check):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

prime(num)

print("\nArmstrong")
new = int(input("Enter a number to check if it's a Armstrong number: "))
def armstrong(n):
    temp = n
    sum = 0
    while(temp != 0):
        d = temp%10
        sum = sum + d**3
        temp = int(temp/10)
    if(sum == n):
        print(f"{n} is an armstrong number")
    else:
        print(f"{n} is not an armstrong number")
armstrong(new)

print("\nLargest number")
def larnum(num, new):
    th = int(input("Enter a new number: "))
    '''if(num > new):
        if(num > th):
            print(f"From {num}, {new} and {th}, {num} is the largest number")
        else:
            print(f"From {num}, {new} and {th}, {th} is the largest number")
    else:
        if(new > th):
            print(f"From {num}, {new} and {th}, {new} is the largest number")
        else:
            print(f"From {num}, {new} and {th}, {th} is the largest number")'''
    print(f"From {num}, {new} and {th}, {max(num, new, th)} is the largest number")

larnum(num, new)

'''
Enter number: 5

Multiplication Table
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Fibonacci
Series 0 1 1 2 3 5
Fibonacci addition of 5 is 5

Factorial
Factorial of 5 is 120

Prime
5 is a prime number

Armstrong
Enter a number to check if it's a Armstrong number: 153
153 is an armstrong number

Largest number
Enter a new number: 340
From 5, 153 and 340, 340 is the largest number
'''
