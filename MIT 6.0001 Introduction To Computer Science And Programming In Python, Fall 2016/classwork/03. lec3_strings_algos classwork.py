# CLASSWORK

# print the length of the string in parenthesis
# x = "abcdefgh"
# print("Length of the string:", len(x))

# # Indexing starts from 0
# print("position 1:", x[0])  # print the string at postion 0
# print("position 2:", x[1])
# #print("position 9:", x[8])  # Index out of range; Error
# print("position 8:", x[-1])  # Last element starts from -1 

# # slice examples 
# print(x[3:6])
# print(x[3:6:2]) 
# print(x[::])
# print(x[::-1])
# print(x[4:1:-2])

# Strings are immutable 
# print(x[0])
# x[0] = 'y'  # Gives an error
# x = "y" + x[0: len(x)]
# print(x)


####################
## EXAMPLE: for loops over strings
####################
# s = "demo loops"
# for index in range(len(s)):
#    if s[index] == 'i' or s[index] == 'u':
#        print("There is an i or u")
#    else:
#        print("There is no i or u")
#        break
#
# for char in s:
#    if char == 'i' or char == 'u':
#        print("There is an i or u")
#    else:
#        print("There is no i or u")
#        break


####################
## EXAMPLE: while loops and strings
####################
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
#    char = word[i]
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)
#    i += 1
# print("What does that spell?")
# for i in range(times):
#    print(word, "!!!")


## CHALLENGE: rewrite while loop with a for loop
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# # if in confusion, go to line 31 & 38
# for char in word:
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)

# print("What does that spell?")
# for i in range(times):
#    print(word, "!!!")


## # In-class question
# The following code includes spaces also
# s1 = "mit u rock"
# s2 = "i rule mit"

# if len(s1) == len(s2):
#     for char1 in s1:
#         for char2 in s2:
#             if char1 == char2:
#                 print("common letter")
#                 break


####################
## EXAMPLE: perfect cube 
####################
# The following code does not consider negative cubes and imperfect cubes
# cube = 27
# #cube = 8120601
# #cube = 2156  # silently fails keeps going on
# for guess in range(cube+1):
#    if guess**3 == cube:
#        print("Cube root of", cube, "is", guess)
#        # loops keeps going even after found the cube root
    

####################
## EXAMPLE: guess and check cube root 
####################
# cube = 27
# cube = 8120601
# cube = 6505
# cube = -27
# # The absolute value (or modulus) | x | of a real number x is the non-negative value of x without regard to its sign
# for guess in range(abs(cube)+1):
#    # passed all potential cube roots
#    if guess**3 >= abs(cube):
#        # no need to keep searching
#        break
# if guess**3 != abs(cube):
#    print(cube, 'is not a perfect cube')
# else:
#    if cube < 0:
#        guess = -guess
#    print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
#cube = 27
# cube = 8120601
# #cube = 10000
# epsilon = 0.1
# guess = 0.0
# increment = 0.01
# num_guesses = 0
# # look for close enough answer and make sure
# # didn't accidentally skip the close enough bound
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#    guess += increment
#    num_guesses += 1
# print('num_guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, "with these parameters.")
# else:
#    print(guess, 'is close to the cube root of', cube)


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
# cube = 36
# # cube = 8120601
# # won't work with x < 1 because initial upper bound is less than ans
# #cube = 0.25
# epsilon = 0.01
# num_guesses = 0
# low = 0  # lower boundary 
# high = cube  # upper boundary 
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#    if guess**3 < cube:
#        # look only in upper half search space
#        low = guess
#    else:
#        # look only in lower half search space
#        high = guess
#    # next guess is halfway in search space
#    guess = (high + low)/2.0
#    num_guesses += 1
# print('num_guesses =', num_guesses)
# print(guess, 'is close to the cube root of', cube)

## Assignment 
# Modify the above code for x < 1 
# cube = 0.064
# epsilon = 0.01
# num_guesses = 0
# low = cube  # lower boundary 
# high = 1  # upper boundary 
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#    if guess**3 < cube:
#        # look only in upper half search space
#        low = guess
#    else:
#        # look only in lower half search space
#        high = guess
#    # next guess is halfway in search space
#    guess = (high + low)/2.0
#    num_guesses += 1
# print('num_guesses =', num_guesses)
# print(guess, 'is close to the cube root of', cube)

## Assignment 
# Modify the above code for negative cubes
cube = -125
epsilon = 0.01
num_guesses = 0
low = cube  # lower boundary 
high = 0  # upper boundary 
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
 

# In-class question
# s = "6.00 is 6.0001 and 6.0002"
# new_str = ""
# new_str += s[-1]
# new_str += s[0]
# new_str += s[4::30] 
# new_str += s[13:10:-1]
# print(new_str)
