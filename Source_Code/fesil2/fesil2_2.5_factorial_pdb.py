import pdb

def factorial(n):
    if n == 0 or n == 1:
        pdb.set_trace()
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    pdb.set_trace()
    factorial(5)
