from Q_55 import populate_2D_arr


def search_2D_array(arr : list, target: int) -> tuple[int,int]:

    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return (i,j)
    return (-1,-1)


if __name__ == "__main__":

    try:
        target = int(input("Enter the target : "))
        rows = int(input("Enter rows (positive integer): "))
        cols = int(input("enter columns (positive integer): "))


        if rows <=0 or cols <=0:
            raise ValueError("Input must be a positive integer.")
        
        
        arr = populate_2D_arr(rows, cols)
        i,j = search_2D_array(arr,target)
        print(arr)
        if (i,j) == (-1,-1):
            print("element not found in the array.")
        else:
            print(f"wlement found at position ({i}, {j})")

    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)