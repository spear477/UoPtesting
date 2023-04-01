# a = 10 
# b= 0
# # print(a/b)

# try:
#     # if code in try are ok enough to wrok
#     # it will show or operate as a result
#     c=a/b
# except:
#     #codes in try are not ok to work , then codes in except will work
#     #exception with manual error message
#     print("you cannot divide with zero")    
    
 
# import os
# cwd = os.getcwd()
# import os

# print(os.path.abspath('test.py'))
# print(os.path.isdir(cwd))
# print(os.path.exists(cwd))
# print(os.listdir(cwd))

# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# print(walk('Week-3'))
# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError()

f = open('test.txt','r')

print(f.name)

f.close()