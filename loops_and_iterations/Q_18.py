
def odd_numbers(n):
    temp = 1
    result = []
    for _ in range(n):
        result.append(temp)
        temp += 2
    return result

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n <=0:
        raise ValueError("Input must be a positive integer.")
    result = odd_numbers(n)
    print("Odd numbers up to", n, "are:", result)