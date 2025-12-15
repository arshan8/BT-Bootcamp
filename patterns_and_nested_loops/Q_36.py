
def pattern(n:int):
    """ 1 
        22 
        333 
        4444 
        . 
        . 
        N rows """
    for i in range(1,n+1):
        for j in range(i):
            print(i, end="")
        print()
    
if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)