def new_line():
    print(".")
    
def three_line():# new_line is nested function
    new_line()    #calling new_line() three time to get 3 lines dot      
    new_line()    
    new_line()

def nine_line():# three_line is nested function
    three_line() # calling three_line() three time to get 9 lines dot 
    three_line()        
    three_line()        


def clear_screen():# new_line,three_line, and also nine_line are nested functions 
    nine_line() #calling nine_line() 2 times to get 18 lines dot
    nine_line()
    three_line()#calling three_line() 2 times  to get 6 lines dot
    three_line()
    new_line()#calling new_line() to get 1 line dot so the total number of output is 25 lines dot
    

print("Printing nine lines")      
nine_line()
print("======") 
print("Calling clearScreen")
clear_screen()    
print("======") 

