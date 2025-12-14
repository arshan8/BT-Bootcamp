from working_with_arrays.src.Q_45 import populate_arr

# python -m sort_and_search_arrays.Q_51


def reverse_array(arr: list[int]) -> list[int]:
    left = 0
    right = len(arr) - 1
    
    while left < right:

        arr[left] = arr[left] ^ arr[right]
        arr[right] = arr[left] ^ arr[right]
        arr[left] = arr[left] ^ arr[right]

        left += 1
        right -= 1
    
    return arr

if __name__ == "__main__":

    try:

        n = int(input("Enter a positive integer: "))
        

        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        
        arr = populate_arr(n)
        
        reversed_arr = reverse_array(arr)
        
        print("Reversed array:", reversed_arr)

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)