def series(n: int) -> list:
    """  1, -5, 9, -13, 17, -21, ... N"""
    ###add 4 to previous , and toggle sign
    if n <= 0:
        return []
    arr = []
    term = 1
    sign = True   

    for _ in range(n):
        if sign:   # positive
            arr.append(term)
        else:      # negative
            arr.append(-term)
        term += 4
        sign = not sign  

    return arr


if __name__ == "__main__":
    try:
        N = int(input("Enter: "))
        arr = series(N)
        print(arr)
    except ValueError:
        print("Enter integer")


