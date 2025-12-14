
def natural_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = natural_numbers(n)
    print("Natural numbers up to", n, "are:", result)