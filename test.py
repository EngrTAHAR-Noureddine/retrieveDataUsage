listi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 6, 7]

first = None
second = "NONE"
first_time = True


def get_addition(index):
    print("iterate : ", index )
    global first, listi, second
    if first is None:
        first = listi.pop()
        if len(listi) == 0:
            listi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 6, 7]
    # if first_time:
    #     second = first
    if second is None:
        second = listi.pop()
        if len(listi) == 0:
            listi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 6, 7]
        print("first : ", first, " Second : ", second, " result: ", first + second)
        first = second

    second = None

for i in range(100):
    get_addition(i)