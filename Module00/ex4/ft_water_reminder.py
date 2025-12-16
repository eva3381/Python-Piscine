
def ft_water_reminder():
    days = input("Days since last watering: ")
    try:
        if int(days) > 2:
            print("Water the plants!")
        elif int(days) >= 0 & int(days) <= 2:
            print("Plants are fine")
        else:
            print("Days cannot be negative!")
    except ValueError:
        print("We only count time in numbers of days!")
