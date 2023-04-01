# def credit(no,no_to_keep =4, chr='*'):
    
    
    
    
    
# import re

# credit("4259 9826 4096 9299")
# def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
#    cc_string_total = sum(map(str.isdigit, cc_string))

#    if digits_to_keep >= cc_string_total:
#        print("Not enough numbers. Add 10 or more numbers to the credit card number.")

#    digits_to_mask = cc_string_total - digits_to_keep
#    masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

#    return masked_cc_string


# print(mask_cc_number("4259 9826 4026 9299"))
# print(mask_cc_number("4259 982& 4026 9299"))
# print(mask_cc_number("4259 9826 40p6 9299"))


import math
def my_sqrt(a):
    x=1
    
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y
print(my_sqrt(100))


def test_sqrt():
    for a in range (1,26):
        my,lib = my_sqrt(a),math.sqrt(a)
        print(f"a = {a} | my_sqrt(a) = {my} | math.sqrt(a) = {lib} | diff = {abs(my - lib)}") 
    
test_sqrt()    