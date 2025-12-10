
def ft_garden_summary():
    name = str(input("Enter garden name: "))
    number = int(input("Enter number of plants: "))
    print("Garden:", name)
    if number < 0:
        print("Plants: You entered a negative number!")
    else:
        print("Plants:", number)
    print("Status: Growing well!")