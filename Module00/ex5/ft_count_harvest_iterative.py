
def ft_count_harvest_iterative():
    try:
        i = 1
        days = int(input("Days until harvest: "))
        if days < 0:
            print("There are no negative days!!!")
        else:
            while i <= days:
                print("Day ", i)
                i = i + 1
            print("Harvest time!")
    except ValueError:
        print("We only count time in numbers of days!")
