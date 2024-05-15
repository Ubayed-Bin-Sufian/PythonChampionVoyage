# prompts the user for mass as an integer (in kilograms)
user_input = int(input("Enter the value of mass (kg): "))
c = 300000000  # meters per second

# outputs the equivalent number of Joules as an integer
print(user_input * c ** 2)
