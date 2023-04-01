def any_lowercase1(s):

     for c in s:

          if c.islower():

               return True

          else:

               return False

 

def any_lowercase2(s):

     for c in s:

          if 'c'.islower():

               return True

          else:

               return False

 

def any_lowercase3(s):

     for c in s:

          flag = c.islower()

     return flag

 

def any_lowercase4(s):

     flag = False

     for c in s:

          flag = flag or c.islower()

     return flag

 

def any_lowercase5(s):

     for c in s:

          if not c.islower():

               return False

     return True

 

def lowercase_function_checker(func):

     check_table = [["A", False], ["a", True], ["Aa", True], ["aA", True], ["HELLO WORLD", False], ["Hello World", True]]

     for n in range(len(check_table)):

          test_string = check_table[n][0]

          expected_result = check_table[n][1]

          if (func(test_string) == expected_result):

               print("OK: The function returns the expected result of case %d" % n)

          else:

               print("NG: The function returns the unexpected result of case %d" % n)

 

# Check any_lowercase1

print ("#1 any_lowercase1")

lowercase_function_checker(any_lowercase1)

print("")

 

# Check any_lowercase2

print ("#2 any_lowercase2")

lowercase_function_checker(any_lowercase2)

print("")

 

# Check any_lowercase3

print ("#3 any_lowercase3")

lowercase_function_checker(any_lowercase3)

print("")

 

# Check any_lowercase4

print ("#4 any_lowercase4")

lowercase_function_checker(any_lowercase4)

print("")

 

# Check any_lowercase5

print ("#5 any_lowercase5")

lowercase_function_checker(any_lowercase5)

print("")