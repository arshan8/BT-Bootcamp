from Q_45 import populate_arr

def calculate_odd_frequency(arr: list[int]) -> int:
    odd_count = 0
    for num in arr:
        if num &1:
            odd_count += 1
    return odd_count

if __name__ == "__main__":


    try: 
        n = int(input("Enter a positive integer: "))
        
        if n <=0:
            raise ValueError("Input must be a positive integer.")
        
        arr = populate_arr(n)
        odd = calculate_odd_frequency(arr)
        even = n - odd

        print("total odd numbers in array", odd)
        print("total odd numbers in array", n - odd)
    except ValueError as e:
        print("Invalid input. Please enter integers only.")
        print(e)