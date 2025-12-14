
def populate_arr(n:int)->list:
    arr = [0]*n
    for i in range(n):
        while True:
            try:
                x = int(input(f"Enter element {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        arr[i] = x
    return arr




if __name__ == "__main__":

    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    
    
    arr = populate_arr(n)
    print("The populated array is:", arr)