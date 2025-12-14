def square(N):
    squares = []
    for i in range(1, N + 1):
        squares.append(i * i)
    return squares

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = square(n)
    print("Squares of natural numbers up to", n, "are:", result)