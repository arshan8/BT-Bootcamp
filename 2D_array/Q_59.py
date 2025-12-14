from Q_55 import populate_2D_arr
from Q_58 import transpose_2D_array


if __name__ == "__main__":  

    try:

        rows = int(input("Enter rows (positive integer): "))
        cols = int(input("enter columns (positive integer): "))

        if rows <=0 or cols <=0:
            raise ValueError("Input must be a positive integer.")
        
        
        arr = populate_2D_arr(rows, cols)
        print("The populated 2D array is:")

        for row in arr:
            print(row)

        print("\n transpose:")
        
        T = transpose_2D_array(arr)

        for row in T:
            print(row)
        
    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)