def int_frac(num : float) -> tuple[int,int]:
    
    """7.6 """
    """integer = 7"""
    """fraction = 0.6"""

    integer = int(num)
    fraction = round(num - integer, 10)
    return integer, fraction

if __name__ == "__main__":
    try:
        N = float(input(" Enter : "))
        integer, fraction = int_frac(N)
        print(f"Integer {integer} and fraction is {fraction} ")
    except:
        raise ValueError("Enter integer")