
def sum_of_three(n):

    res = [1,4,7]

    if n == 1:
        return res[:n]
    elif n == 2:
        return res[:n]
    elif n == 3:
        return res[:n]
    
    sum = 12
    i = 0
    for _ in range(n-3):   #sliding window approach
        temp = sum
        res.append(temp)
        sum-=res[i]
        i+=1
        sum+=temp
    
    return res

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = sum_of_three(n)
    print("Sum of three series up to", n, "are:", result)   
