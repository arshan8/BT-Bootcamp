def solve(n):
    "fibonacci"

    arr = [1,1]

    if n == 1:
        return arr[:1]
    elif n == 2:
        return arr[:2]
    
    for i in range(n-2):
        temp = arr[-1] + arr[-2]
        arr.append(temp)

    return arr

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = solve(n)
    print("Fibonacci series: ", result)