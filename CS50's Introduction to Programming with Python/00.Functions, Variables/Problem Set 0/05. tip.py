def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.removeprefix("$")  # Removing the $ sign leaves it to str value
    return float(d)  # str value is converted to float


def percent_to_float(p):
    x = p.removesuffix("%")  # Removing the $ sign leaves it to str value
    p = float(x) / 100  # str value x is converted to float
    return float(p)  # str value p is converted to float


main()
