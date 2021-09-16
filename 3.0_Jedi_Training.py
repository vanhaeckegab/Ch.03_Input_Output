# Sign your name:Gabe Van Haecke
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("Hi there! What's your name")
print("Hi",name,"Nice to meet you")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
h=float(input("What is the height of your triangle? "))
b=float(input("What is the base of your input? "))
print(.5*h*b)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
import math
r=float(input("What is the radius of your circle? "))
print(math.pi*2*r)

# 4. Ask a user for an integer and then print the square root.
import math
i=int(input("What number would you like to find the square root of? "))
print(math.sqrt(i))

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
input("What is the mass of your object? ")
input("What is the acceleration of the object? ")
print("The Force")
print("Get it")
