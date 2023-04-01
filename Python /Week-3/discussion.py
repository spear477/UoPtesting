#  Chanined conditionals
# age=10   

# if age == 18 : #statement 1
#     print("U can vote")
# elif age > 18 :    #statement 2
#      print("U are old enough to vote and participate")
# else:     #statement 3
#     print("U can't vote or participate")     
    


#Nested conditional

# if age == 18: #statement 1
#     print("U can vote")
    
# else:  
#     if age > 18: #statement 2
#        print("U are old enough to vote and participate")
#     elif age < 18: #statement 3
#         print("U can't vote or participate")

gender="dog"
 
# #simple conditional with "or" 
# if gender == "male" or gender =="female":
#     print("You are",gender)
# else:
#     print("You are not human")   
# #nested conditional
# if gender == "male":
#     print("You are",gender)
# else:
#     if gender == "female":
#        print("You are",gender)   
#     else:
#      print("You are not human")    
        


print("You are",gender) if gender == "male" or gender =="female"  else print("You are not human") 