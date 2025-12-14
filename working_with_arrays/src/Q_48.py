
from Q_45 import populate_arr

def find_maximum(arr : list[int]) -> int:
  
    maxi = arr[0]
        

    for num in arr:
        if num > maxi:
            maxi = num
    return maxi
    

if __name__ == "__main__":

    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    
    
    arr = populate_arr(n)
    result = find_maximum(arr)
    print("The maximum element in the array is:", result)