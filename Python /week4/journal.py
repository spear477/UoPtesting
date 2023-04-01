import math;

def hypotenuse(a,b,unit="centimeter"):
    #a and b are the length of other two legs of a right triangle
    #c is the length of the hypotenuse of the right triangle
    #According to the Pythagorean theorem, c**2 = a**2+b**2
    #so c =  math.sqrt(a**2+b**2)
    if isinstance(a,int) and isinstance(b,int):
        c = int(math.sqrt(a**2 + b**2))
    else:
        c = round(math.sqrt(a**2 + b**2),3)
        
    print("The hypotenuse is ",c,unit)
    return c

hypotenuse(3,4)
hypotenuse(2.3,10.3,"decimeter")
hypotenuse(2,2.3)



#the function that calculate the volume of a sphere
#In this function  r is the radius and h is the height of the cylinder with defult
#unit centimeters
#the volume of a cylinder is V= pi.r**2*h
def volume(r,h,unit="centimeters"):
    pi =round( math.pi,3)
    if not isinstance(r,int) or not isinstance(h,int):
        v = round((pi*(r**2)*h),3)
    else:
         
         v = int(pi*(r**2)*h)
    
    print("The volume of the cylinder is",v,"cubic",unit)
    
    return v

volume(3,4)
volume(2.3,5,"decimeters")           
volume(1.4,2.5)