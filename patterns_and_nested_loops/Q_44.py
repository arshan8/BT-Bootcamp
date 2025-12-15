def reverse(s: str) -> str:
    """reverse: abc -> cba"""
    arr = list(s)
    i, j = 0, len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return "".join(arr)

if __name__ == "__main__":
    string = input("Enter: ")
    reversed_string = reverse(string)
    print("Reversed string is :",reversed_string)
