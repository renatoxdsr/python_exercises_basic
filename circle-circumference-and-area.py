#import Math package 
import math

# calculate the circumference and area of a circle.
#calculating the circumference of a circle
#it is 2 multiplied per pi  multiplied per raid
C= 2 * 0.43 * math.pi;

#calculating area of a circle 
#it is pi multplied per raid to the power of 2
#For reference, ** is the symbol for exponentiation

A= math.pi * 0.43 ** 2;

#print the result of circumference and area
#print as a string str
print("Circumference: " + str(C));
print("Area: " + str(A) + "\n");

#print as a float
print(f"The Circumference of the circle is: {C}");
print(f"The Area of the circle is: {A}" + "\n");

#format output of the float to 3 decimals 
#it's called f-string formatting (:3f)
print(f"The Circumference of the circle is: {C:.3f}");
print(f"The Area of the circle is: {A:.3f}" + "\n");
#printing 2 decimals
print(f"The Circumference of the circle is: {C:.2f}");
print(f"The Area of the circle is: {A:.2f}" + "\n");

#rounding the variable before printing
print(f"The Circumference of the circle is: {round(C,2)}");
print(f"The Area of the circle is: {round(A, 2)}" + "\n");
