import math
import random

choice = input("Enter\n1. Area of Triangle\n2. Area of Rectangle\n3. Area of Circle\n4. To generate random numbers and swap\n5. To convert km to miles\n")
if choice == 1:
 s1 = input("Enter 1st side ")
 s2 = input("Enter 2nd side ")
 s3 = input("Enter 3rd side ")
 s = (s1+s2+s3)/2.0
 area  = float(math.sqrt(s*(s-s1)*(s-s2)*(s-3)))
 print "Area of triangle is--> ", area

elif choice == 2:
    s1 = input("Enter 1st side ")
    s2 = input("Enter 2nd side ")
    area  = s1*s2
    print "Area of rectangle is--> ", area

elif choice == 3:
    r = input("Enter radius of Circle ")
    area = math.pi*r*r
    print "Area of circle is-->{}".format(area)

elif choice == 4:
    x = random.randint(0, 15)
    y = random.randint(30, 45)
    print "x-> ", x, "y-> ", y
    x,y = y,x
    print "x-> ", x, "y-> ", y

elif choice == 5:
    km = input("Enter kilometers\n")
    m = km*0.6213712;
    print "Kilometers->{} and Miles->{}".format(km, m)

else:
    print "Wrong choice"
