# my_dict = {'Animals' : ['Dog', 'Cat', 'Monkey'], 'Fruits' : ['Apple', 'Orange', 'Pineapple'], 'Countries' : ['England', 'USA', 'Japan']}
# with open('test.txt','r') as rd: 
#      f_dict = rd.read()  
#      print(f_dict)     

# def invert_dict(d):
#                inverse = dict()
#                for key in d:
#                     val = d[key]
#                     for item in val:
#                          if item not in inverse:
#                               inverse[item] = [key]
#                          else:
#                               inverse[item].append(key)
                    
#                return inverse 

     
# # print(invert_dict(f_dict))
# mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
# a=0
# b=0
# total = 0
# while a <= 2:
#     while b < 2:
#      #    print(a)
#      #    print(b)
#         print("a",mylist[a])
#         print("b",mylist[b])
#         print('this ',mylist[a][b])
#         total += mylist[a][b]
#         print(total)
#         b += 1
#     a += 1
#     b = 0 
# print (total)
# try:
#     fin = open('the_file', 'r')
# except:
#     fin = open('the_file', 'w')
# fin.close()
pi = float(3.14159)
print (pi)
mylist = [ [2,2,1], [1,2,3], [1,1,1] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total)
# def fa():

#     fb()

# def fb():

#     fa()

# fa()
mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2
def procedure( n ):
    while n > 0:
        print (n,)
        n = n - 1
print(procedure(3))  
print('%s %d' % (5, 'dollars'))          