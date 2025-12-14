

from working_with_arrays.src.Q_45 import populate_arr

def binary_search(arr: list[int], target: int) -> int:

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) >> 1

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    try:

        n = int(input("Enter a positive integer: "))
        
        target = int(input("Enter the element to search for: "))

        if n <=0 or target < 0:
            raise ValueError("Input must be a positive integer.")
        
        arr = populate_arr(n)

        arr.sort() 
        
        result = binary_search(arr, target)
        


        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found in the array.")

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)