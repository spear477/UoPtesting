# def any_lowercase1(s):
#      for c in s:
#           if c.islower():#check whether the first letter of the string is lowercase or uppercase
#                return True
#           else:
#                return False
# print(any_lowercase1("Hello"))           
# print(any_lowercase1("hello"))           

# def any_lowercase2(s):
#      for c in s:
#           if 'c'.islower():#only working the if statement 
#                            #whether it is lower or upper
#                return 'True'
#           else:
#                return 'False'
# print(any_lowercase2("hello"))           
# print(any_lowercase2("Hello"))           
# print(any_lowercase2("123"))           
           
           
           
# def any_lowercase3(s):
#      for c in s:
#           flag = c.islower()# check the last letter of the string if it is lower or upper
#      return flag           
 
# print(any_lowercase3("Hello"))           
# print(any_lowercase3("hello"))    
# print(any_lowercase3("HellO"))           
# print(any_lowercase3("hellO"))           
       
 
def any_lowercase4(s):
     flag = False
     for c in s: #check if there is lowercase letter in the string
                 #if there is no lowercase letter, it will show false
          flag = flag or c.islower()
     return flag

print(any_lowercase4("HElLO"))           
print(any_lowercase4("heLlO"))           
print(any_lowercase4("Hello"))           
print(any_lowercase4("HELLO"))           
print(any_lowercase4("HelloO"))           


# def any_lowercase5(s):
#      for c in s: #check if the whole string is in lowercase or not
#           if not c.islower():
#                return False
#      return True

# print(any_lowercase5("HELLO"))           
# print(any_lowercase5("Hello"))           
# print(any_lowercase5("hello"))           
# print(any_lowercase5("hellO"))           
 