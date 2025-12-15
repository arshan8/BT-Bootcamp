def pattern(n:int):
    """ 1 
        12 
        123 
        1234 
        . 
        . 
        N ro"""
    for i in range(n):
        for j in range(1,i+1):
            print(j,end="")
        print()

if __name__ == "__main__":
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)