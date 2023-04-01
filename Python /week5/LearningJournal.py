prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    #check the looping letter is "O" or "Q"
    #if O and Q then , combine that letter with 'uack'
      
      if letter == "O" or letter == "Q":
        newSuffix='uack'
        print(letter+newSuffix)
      else:   #if others letters are not O and Q then , it will combine with "ack"
        print(letter + suffix)
        
        
#example 1 
# slice the string into one letter one line
def eachLine():
    string = "Can you give me full marks?"      
    for s in string:
        print("This is ",s)
eachLine()        
              
#example 2
#slice string array               
def accordingToIndex():
    array= ["Front-end Developer","Back-end Developer","Full-stack Developer","UI-UX designer"] 
    for no,job in enumerate(array):
        print(no,"I want to become",job)
accordingToIndex()        


#example 3
#input which ask intenger only 
#you can choose form 0 to 3 to get each data
#apart from 0 to 3 , this function will not show.
inputForJob = int(input("Choose from 0 to 3"))
def jobRoles():
    array= ["Front-end Developer","Back-end Developer","Full-stack Developer","UI-UX designer"] 
    
    for no,job in enumerate(array):
      if inputForJob == no:
         print("Do you want to apply for",job,"?")
      
jobRoles() 