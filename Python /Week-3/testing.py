import turtle
import math
import time
import datetime
bob = turtle.Turtle()

def square(t):
    for i in range(6):
        t.fd(100)
        t.lt(90)

square(bob)
we = turtle.Turtle()
square(we)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 5, 10)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
circle(bob,100)    

print(time.time_ns())
print(time.thread_time())

print(datetime.datetime.now())




# print("Is blue, red, or brown your favorite color?")
# def fav_col(x):
#     if x!="blue""red""brown":
#         print("My favourite color is ",x)
#         print("This color wasn't an option.")
#     else:  
#         print("My favourite color is ",x)   
#         if x=="blue":
#             print("This is the color of water")
#         if x=="red":
#             print("This is the color of fire")    
#         if x=="brown":
#             print("This is the color of earth")
        
        
# fav_col("red")        
# print (1,000,000)