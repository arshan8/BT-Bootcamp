def even_squares(n):
    temp = 2
    squares = []
    for _ in range(n):
        squares.append(temp*temp)
        temp += 2
    return squares

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = even_squares(n)
    print("Squares of even numbers up to", n, "are:", result)