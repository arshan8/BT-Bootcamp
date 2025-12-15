
def pattern(n : int):
    """ ****
        ****
        ****
        ****"""
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)

