
from functools import lru_cache

# @lru_cache(None)
# def factorial(n):
                                 #recursion memory overhead
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    

# def pattern(n : int):
#     temp = 0
#     for i in range(n):
#         for j in range(i + 1):
#             print(factorial(temp), end=" ")
#             temp+=1
#         print()
        

def factorial():
    " factorial generator "   #stream friendly
    prev = 1
    temp = 1
    while True:
        yield prev
        prev = prev * temp
        temp += 1


def pattern(n : int):
    """ 1 
        1 2 
        6 24 120"""
    
    #factorial(N) = N * factorial(N-1)
    #fact(0) = fact(1) = 1
    
    fact = factorial()
    for i in range(n):
        for j in range(i + 1):
            print(next(fact), end=" ")
        print()

if __name__ == "__main__": 
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern(x)