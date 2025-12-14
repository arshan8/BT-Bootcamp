

def populate_2D_arr(rows:int, cols:int)->list[list[int]]:
    arr = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            while True:
                try:
                    x = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            arr[i][j] = x
    return arr

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

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)