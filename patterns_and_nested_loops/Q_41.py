
num_to_word = ["Zero","One","Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

"""a. Input: 270176  
b. Output: Two Seven Zero One Seven Six"""

if __name__ == "__main__":
    try:
        N = input("Enter number: ")
        N = list(map(int,N))
    except:
        raise ValueError("enter integers only ")
    # ans = ""  #creates new string every time
    ans = []
    for ele in N:
        if ele >= 0:
            ans.append(num_to_word[ele])

    

    print(" ".join(ans))



