from itertools import product
n = 4
bin_str_list = [''.join(p) for p in product('01', repeat=n)]

print(bin_str_list)
