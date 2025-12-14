from Q_55 import populate_2D_arr


def sum_2D_array(arr):

    total = 0
    for row in arr:
        for num in row:
            total += num
    return total


if __name__ == "__main__":

    try:

        rows = int(input("Enter rows (positive integer): "))
        cols = int(input("enter columns (positive integer): "))

        if rows <=0 or cols <=0:
            raise ValueError("Input must be a positive integer.")
        
        
        arr = populate_2D_arr(rows, cols)
        result = sum_2D_array(arr)
        print("The sum of all elements in the 2D array is:", result)

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)