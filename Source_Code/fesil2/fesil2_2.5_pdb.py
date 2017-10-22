import pdb

def print_func(n):
    if n == 0: # funksiyanı bitirən əsas hal.
        pdb.set_trace()
        return 0
    elif n > 0:
        print(n)
        return print_func(n - 1) # rekursiv çağırış


if __name__ == "__main__":
    pdb.set_trace()
    print_func(4)
