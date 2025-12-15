
def pattern(n : int):
    """ 11111111
        2222222
        3333333
        4444444
        N rows"""
    for i in range(n):
        for j in range(n):
            print(i+1, end="")
        print()

if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)

