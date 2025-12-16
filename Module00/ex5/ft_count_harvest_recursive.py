
def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    i = 1

    def recursive(day: int, i: int) -> None:
        print(f"Day {i}")
        if day == 1:
            return
        i += 1
        recursive(day - 1, i)
    recursive(day, i)
    print("Harvest time!")
