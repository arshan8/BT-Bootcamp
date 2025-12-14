from Q_45 import populate_arr


#from working_with_arrays.src.Q_45 import populate_arr
#python -m working_with_arrays.src.Q_46

def sum(arr : list) -> int: 
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":

    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    
    
    arr = populate_arr(n)
    result = sum(arr)
    print("The sum of the array elements is:", result)