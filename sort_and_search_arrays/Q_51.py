from working_with_arrays.src.Q_45 import populate_arr

# python -m sort_and_search_arrays.Q_51

if __name__ == "__main__":

    try:

        n = int(input("Enter a positive integer: "))
        

        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        
        arr = populate_arr(n)
        
        print(arr)

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)