import time

def countup(n): #for the input number is negative 
     if n >= 0:
          print('Blastoff!')
     else:
          time.sleep(2)
          print(n)
          countup(n+1)
          

def countdown(n):#for the input number is positive
     if n <= 0:
          print('Blastoff!')
     else:
          time.sleep(2)
          print(n)
          countdown(n-1)
        
     

input1 = int(input("Add your number")) #input for number which allows only integer values

if input1 > 0 :  #conditional statement which will decide positive or negative integer what function should work 
    countdown(input1)
else:
    countup(input1)        
    
countdown(input1) if input1 >=0 else countup(input1)  # same functions with ternary operators
  
  
  
age=19
print("You are old enough to vote") if age >= 18 else print("You are not old enough to vote")
  