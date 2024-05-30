def main():

    # prompts the user for a time
    user_input = input("What time is it? ")
    hours = convert(user_input)
    checkMealTime(hours)


def convert(time):

    # 12-hour format
    # checks if the input contains a.m. or p.m.
    if time.endswith("a.m.") or time.endswith("p.m."):

        # split the input into time and period
        meridian_time, period = time.split()

        # convert the meridian time from "HH:MM" format to a float representing the number of hours.
        hours, minutes = meridian_time.split(":")

        hours = float(hours)
        minutes = float(minutes)

        if period == "p.m." and hours != 12:
            hours = hours + 12
            return hours + (minutes/60)

        elif period == "a.m." and hours == 12:
            hours = 0
            return hours + (minutes/60)

        elif period == "a.m." and hours != 12:
            return hours + (minutes/60)

        elif period == "p.m." and hours == 12 and 00 <= minutes <= 59:
            return hours + (minutes/60)

        else:
            return 0

    # 24 hour format
    else:
        hours, minutes = time.split(":")
        return float(hours) + (float(minutes)/60)

def checkMealTime(hours):

    # outputs whether it’s breakfast time, lunch time, or dinner time.
    if 7 <= hours <= 8:
        print("breakfast time")

    elif 12 <= hours <= 13:
        print("lunch time")

    elif 18 <= hours <= 19:
        print("dinner time")

    else:
        print("Not meal time")


if __name__ == "__main__":
    main()
