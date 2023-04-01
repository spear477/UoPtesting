# def factorial(n):
#    space = ' ' * (4 * n)
#    print(space, 'factorial', n)
#    if n == 0:
#      print(space, 'returning 1')
#      return 1
#    else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(space, 'returning', result)
#         return result


# factorial(4)    


# def calculate(num1,num2):
#     result = num1 + num2
#   return result #the way we used the return is wrong 
# calculate(1,2)
# TRIANGLE_BASE   = -2

# TRIANGLE_HEIGHT  = 4

# PYRAMID_HEIGHT   = -6

# def calculate_area_of_triangle(par_base, par_height):

#     w_ret = par_base

#     w_ret = (w_ret * par_height)

#     w_ret = (w_ret / 4)

#     return w_ret

# def calculate_volume_of_pyramid(par_base_area, par_height):

#     w_ret = par_base_area

#     w_ret = (w_ret * par_height)

#     w_ret = (w_ret / 3)

#     return w_ret 
# def my_main():

#     w_triangle = calculate_area_of_triangle(TRIANGLE_BASE, TRIANGLE_HEIGHT)

#     w_pyramid = calculate_volume_of_pyramid(w_triangle, PYRAMID_HEIGHT)

#     print("The volume of the pyramid is %d" % w_pyramid)

# my_main()

# n = int(input('Enter a positive number between 1 and 10: '))
# def countdown(x):
#    if x == 0:
#       print('Countdown complete')
#    else:
#      print(x)
#      countdown(x-1)
# y = int(input('Enter a negative number between -1 and -10: '))
# def countup(z):
#     if z == 0:
#      print('Countup complete')
#     else:
#      print(z)
#      countup(z+1)
#      countdown(x)  
#      countup(z)
# countdown(x)     

# x = int(input('Enter a positive number between 1 and 10: '))
# def countdown(x):
#     if n == 0:
#        print('Countdown complete')
#     else:
#       print(n)
#       countdown(n-1)
# z = int(input('Enter a negative number between -1 and -10: '))
# def countup(z):
#     if y == 0:
#         print('Countup complete')
#     else:
#         print(y)
#         countup(y+1)
#         countdown(x)
#         countup(z)
# countdown(x)        

# x = int(input('Enter a positive number between 1 and 10: '))
# def countdown(x):
#   if x == 0:
#     print('Countdown complete')
#   else:
#     print(x)
#     countdown(x+1)
#     countdown(x)
# countdown(x+1)    

# def test_function( length, width, height):
#     print ("the area of the box is ",length*width*height)
#     return length*width*height

# l = 12.5
# w = 5
# h = 2
# test_function(l, w, h)
# def area(l, w):
#     temp = l * w
#     return temp

# l = 4.0
# w = 3.25
# x = area(l, w)
# if ( x ):
#   print (x)
# n = int(10.)

# print(isinstance(n, float), isinstance(n * 1.0, float))
def compound_interest(capital, interest = 3):

    if capital >= 100000:

        print("You are rich! Enjoy your life")

        return

    else:

        asset = capital * ((interest / 100) + 1)

        year = 0

        print(str(year + 1) + " years after, your asset is " + str(round(asset)) + "dollars.")

        return capital * compound_interest(asset, interest)

compound_interest(10000, 5)

