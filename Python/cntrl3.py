import math
import random

choice = int(input("Enter\n1. Area of Triangle\n2. Area of Rectangle\n3. Area of Circle\n4. To generate random numbers and swap\n5. To convert km to miles\n"))
# print (choice.type())
if choice == 1:
 s1 = float(input("Enter 1st side "))
 s2 = float(input("Enter 2nd side "))
 s3 = float(input("Enter 3rd side "))
 s = (s1+s2+s3)/2.0
 area  = float(math.sqrt(s*(s-s1)*(s-s2)*(s-3)))
 print ("Area of triangle is--> ", area)

elif choice == 2:
    s1 = float(input("Enter 1st side "))
    s2 = float(input("Enter 2nd side "))
    area  = s1*s2
    print ("Area of rectangle is--> ", area)

elif choice == 3:
    r = float(input("Enter radius of Circle "))
    area = math.pi*r*r
    print ("Area of circle is-->", area)

elif choice == 4:
    x = random.randint(0, 15)
    y = random.randint(30, 45)
    print ("x-> ", x, "y-> ", y)
    x,y = y,x
    print ("x-> ", x, "y-> ", y)

elif choice == 5:
    km = float(input("Enter kilometers\n"))
    m = km*0.6213712;
    print (f"Kilometers->{km} and Miles->{m}")

else:
    print ("Wrong choice")

'''
Enter
1. Area of Triangle
2. Area of Rectangle
3. Area of Circle
4. To generate random numbers and swap
5. To convert km to miles
1
Enter 1st side 4
Enter 2nd side 5
Enter 3rd side 6
Area of triangle is-->  17.1846588560844

Enter
1. Area of Triangle
2. Area of Rectangle
3. Area of Circle
4. To generate random numbers and swap
5. To convert km to miles
2
Enter 1st side 5
Enter 2nd side 6
Area of rectangle is-->  30.0

Enter
1. Area of Triangle
2. Area of Rectangle
3. Area of Circle
4. To generate random numbers and swap
5. To convert km to miles
3
Enter radius of Circle 5
Area of circle is--> 78.53981633974483

Enter
1. Area of Triangle
2. Area of Rectangle
3. Area of Circle
4. To generate random numbers and swap
5. To convert km to miles
4
x->  15 y->  45
x->  45 y->  15

Enter
1. Area of Triangle
2. Area of Rectangle
3. Area of Circle
4. To generate random numbers and swap
5. To convert km to miles
5
Enter kilometers
5
Kilometers->5.0 and Miles->3.106856
'''
