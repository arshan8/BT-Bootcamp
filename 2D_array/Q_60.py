from Q_55 import populate_2D_arr


def multiply_2D_arrays(arr1: list, arr2: list) -> list:

    """m*n p*q : n == p and result is m*q"""

    rows1 = len(arr1)
    cols1 = len(arr1[0]) if rows1 > 0 else 0
    rows2 = len(arr2)
    cols2 = len(arr2[0]) if rows2 > 0 else 0

    if cols1 != rows2:
        raise ValueError("Incompatible dimensions for multiplication.")

    result = [[0]*cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result


if __name__ == "__main__":  

    try:

        rows1 = int(input("Enter rows for first array (positive integer): "))
        cols1 = int(input("Enter columns for first array (positive integer): "))
        rows2 = int(input("Enter rows for second array (positive integer): "))
        cols2 = int(input("Enter columns for second array (positive integer): "))

        if rows1 <=0 or cols1 <=0 or rows2 <=0 or cols2 <=0:
            raise ValueError("Input must be a positive integer.")
        
        
        arr1 = populate_2D_arr(rows1, cols1)
        arr2 = populate_2D_arr(rows2, cols2)

        result = multiply_2D_arrays(arr1, arr2)

        print("Resultant array after multiplication:")

        for row in result:
            print(row)
        
    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)