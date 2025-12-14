from working_with_arrays.src.Q_45 import populate_arr

# python -m sort_and_search_arrays.Q_51


def sorted_array(arr: list[int], asc = True) -> list[int]:

    if asc:
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":

    try:

        n = int(input("Enter a positive integer: "))
        order = input("Sort in ascending order? (yes/no) ")
        order.strip().lower()

        if n <= 0 :
            raise ValueError("Input must be a positive integer.")
        
        if order not in ['yes', 'no']:
            raise ValueError("Input must be a positive integer.")
        
        arr = populate_arr(n)
        
        reversed_arr = sorted_array(arr, order == 'yes')
        
        print("Reversed array:", reversed_arr)

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)