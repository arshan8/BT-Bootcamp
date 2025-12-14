

from Q_45 import populate_arr

def linear_search(arr: list[int], target: int) -> int:
    for idx,val in enumerate(arr):
        if val == target:
            return idx
    return -1


if __name__ == "__main__":

    try:

        n = int(input("Enter a positive integer: "))
        
        target = int(input("Enter the element to search for: "))

        if n <=0 or target < 0:
            raise ValueError("Input must be a positive integer.")
        arr = populate_arr(n)
        result = linear_search(arr, target)
        


        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found in the array.")

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)

