# Source of the code: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec2_branch_loops/
# In VS Code, to comment - Ctrl + k + C, to uncomment - Ctrl + k + u

###################
## EXAMPLE: strings 
###################

# hi = "hello there"
# name = "ana"
# greet = hi + name  
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# silly = hi + (" " + name)*3
# print(silly)


####################
## EXAMPLE: output 
####################
# x = 1
# print(x)
# x_str = str(x)
# print("my fav number is", x, ".", "x=", x)
# print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is" + x_str + "." + "x=" + x_str)


####################
## EXAMPLE: input
####################
# text = input("Type anything... ")
# print(5*text)
# num = int(input("Type a number... "))
# print(5*num)


####################
## EXAMPLE: COMPARISON EXAMPLE FROM CLASSWORK
####################
# pset_time = 15
# sleep_time = 8
# print(sleep_time > pset_time)
# derive = True
# drink = False
# both = drink and derive
# print(both)


####################
## EXAMPLE: conditionals/branching 
####################
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
# elif x < y:
#    print("x is smaller")
# elif x > y:
#    print("y is smaller")
# print("thanks!")


####################
## EXAMPLE: remainder 
####################
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#    print("number is even")
# else:
#    print("number is odd")


####################
## EXAMPLE: while loops 
####################
# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
   
# print("\nYou got out of the Lost Forest!\n\o/")


## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter

####################
## EXAMPLE: while loops CLASSWORK 
####################
# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# counter = 0 
# while n == "right" or n == "Right":
#   counter += 1
#   if counter == 2:
#     print("☹  ☹  ☹\n")

#   elif counter > 2:
#     print("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┬─┬\n****************\n****************\n")

#   n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")

# print("\nYou got out of the Lost Forest!\n\o/")


# n = 0
# while n < 5:
#    print(n)
#    n = n+1


####################
## EXAMPLE: for loops
####################
# for n in range(5):
#    print(n)

# mysum = 0
# for i in range(10):
#    mysum += i
# print(mysum)

# mysum = 0
# for i in range(7, 10):
#    mysum += i
# print(mysum)

#CLASSWORK
# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
# print(mysum)

# mysum = 0
# for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
# print(mysum)


####################
## EXAMPLE: perfect squares
####################
# ans = 0
# neg_flag = False
# x = int(input("Enter an integer: "))

# if x < 0:
#    neg_flag = True
# while ans**2 < x:
#    ans = ans + 1
# if ans**2 == x:
#    print("Square root of", x, "is", ans)

# else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#       print("Just checking... did you mean", -x, "?")
        

####################
## TEST YOURSELF! 
##  <<<  HOMEWORK  >>>
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))

if x < 0:
   neg_flag = True
while ans**2 < x:
   ans = ans + 1
if ans**2 == x:
   print("Square root of", x, "is", ans)
   
else:
   if x > 0:
      print(x, "is not a perfect square")
   else:
    if neg_flag:
       x = -x
    while ans**2 < x:
       ans = ans + 1
    if ans**2 == x:
        print("Square root of", -x, "is", str(ans) + "i, where i is an imaginary number.")
    else:
       print(-x, "is not a perfect square")