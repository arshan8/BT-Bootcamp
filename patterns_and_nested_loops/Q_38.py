def fibonacci():
    """generator to yield pibonacci numbers indefinitely."""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def pattern(n: int):
    """ 1 
        1 2 
        3 5 8 
        13 21 34 55 
        . 
        N rows"""
    
    """1 1 2 3 5 8.."""
    fib = fibonacci()
    for i in range(1,n+1):
        for j in range(i):
            print(next(fib), end=" ")
        print()

if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)