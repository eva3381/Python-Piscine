
def ft_plant_age():
    days = input("Enter plant age in days: ")
    try:
        if int(days) > 60:
            print("Plant is ready to harvest!")
        elif int(days) <= 60 & int(days) >= 0:
            print("Plant needs more time to grow.")
        else:
            print("Plant age cannot be negative!")
    except ValueError:
        print("We only count time in numbers of days!")
