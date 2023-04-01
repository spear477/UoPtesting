import math

def my_sqrt(a):
    x=1#initialize the value of x =1,whatever the value of x , the function work
       #just like using math.sqrt()
    while True: #code form the given example 
          y = (x + a/x) / 2.0
          if y == x:
               break
          x = y 
     
    return y
     
     
print(my_sqrt(100))  


def test_sqrt():
     a=1 #a is a value of 1 at first
     
     while a < 26: #while looping statement that work for the value of a not greater than 26
                   #so the values are form 1 to 25
           #difference betweeen my_sqrt() and math.sqrt()
           #to get absolute value of the difference use abs() built-in function        
          diff = my_sqrt(a) -math.sqrt(a) 
          absoluteValue = abs(diff)
          #to get the given ouput , print like this
          print("a=",a,"|my_sqrt(a)=",my_sqrt(a),"|math.sqrt(a)=",math.sqrt(a),"|diff=",absoluteValue)
          #after the operation for a value , it needs to add 1 
          
          a=a+1   
test_sqrt()