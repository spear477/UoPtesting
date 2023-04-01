#Part 1
  
pi=3.1415926535897932
def print_volume(r,unit="centimeter"):# function that calculate volume with argument r
    sphereVolume = round((4/3*pi*r**3),3) 
    # sphereVolume=4/3*pi*r**3
    print("Its volume is:", sphereVolume,"cubic",unit)
    
    
print_volume(3,"decimeter")    
print_volume(5,"millimeter")    
print_volume(8)   



def introName(name): #ask name to get result just like "I'm John"
    print("I'm ",name)
def age(birthYear):#function that caclulates how old are you now if we give arguments BirthYear
    print("I'm", 2022-birthYear,"years old")    
def occupation(job):#function that describe what are you now
    print("I'm a",job)    
    
def greeting(name,Birthyear,job):#introName(),age(),and status() are nested in greetint() with three arguements' name,BirthYear,job'
        introName(name) 
        age(Birthyear)
        occupation(job)
print("Person 1 ")     
greeting("John",2002,"student")   
print("Person 2 ")     
greeting("Julius",1992,"manager") 
print("Person 3 ")            
greeting("Johnny",1982,"doctor")    



def Addition(x, y):
    result = x + y
    return result
def Multiplication(myFun, a, b):
    function_result =  myFun(a, b)
    final_result = function_result * 3
    print(final_result)

Multiplication(Addition, 3, 3)  