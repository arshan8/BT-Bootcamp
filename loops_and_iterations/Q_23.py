def solve(n):

    """ add 4 to previous number but add 8 to every 4th number """
    res = [1]

    to_add = [8,4,4,4]  # 0 1 2 3,   

    for i in range(1,n):
        
        x = res[-1] + to_add[i%4]
        res.append(x)

    return res


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = solve(n)
    print("Series :", result)
