def bin_str_list(n):
      if n == 0:
            #base case
            return ['']
      else:
            # Rekursiya
            return [i + '0' for i in bin_str_list(n-1)] + [i + '1' for i in bin_str_list(n-1)]

print(bin_str_list(4))
