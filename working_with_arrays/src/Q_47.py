
from Q_45 import populate_arr

def find_minimum(arr : list[int]) -> int:
  
    mini = arr[0]
    for num in arr:
        if num < mini:
            mini = num
    return mini
if __name__ == "__main__":

    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    
    
    arr = populate_arr(n)
    result = find_minimum(arr)
    print("The minimum element in the array is:", result)