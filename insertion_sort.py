# insertion_sort sorts an input array in monotonically decreasing order
# references Cormen Introduction to Algorithms Section 2.1 code reference
def insertion_sort(input, input_len):
    for i in range(1, input_len):
        key = input[i]
        j = i - 1
        
        # flipping the comparison from arr[j] > to arr[j] < 
        # switches from monotonically increasing to decreasing
        while j >= 0 and input[j] < key:
            input[j + 1] = input[j]
            j = j - 1
        
        input[j + 1] = key
    return input

if __name__ == "__main__":
    inp = [1, 11, 4, 7, 21, 13, 5, 9]
    print("input: ", inp)
    out = insertion_sort(inp, len(inp))
    print("output: ", out)
