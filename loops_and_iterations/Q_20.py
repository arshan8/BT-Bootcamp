def Q_20(n):
    
    res = []
    temp = 0
    for _ in range(n):
        
        if not res:
            res.append(1)
        else:
            res.append(res[-1] + temp)
        temp+=1
        
    return res

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = Q_20(n)
    print("Squares of even numbers up to", n, "are:", result)