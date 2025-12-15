def square(n):
    """square number generator"""
    temp = 1

    while True:
        yield temp * temp
        temp += 1


def pattern(n: int):
    """1
      -4 9 
      -16 25 -36 """
    sq = square(1)
    sign = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(sign*next(sq), end=" ")
            sign *= -1
        print()

if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)