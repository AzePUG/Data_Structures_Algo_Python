def massiv_siralidirmi(massiv):
    print("Yeni massiv : {}".format(massiv))
    # Esas hal
    if len(massiv) == 1:
        return True
    # Rekursiya
    if massiv[0] <= massiv[1] and massiv_siralidirmi(massiv[1:]):
        return True
    else:
        return False

massiv1 = [23, 34, 45, 56, 88, 97, 101, 125]
# True qayitmalidir
print(massiv_siralidirmi(massiv=massiv1))

massiv2 = [23, 34, 45, 56, 88, 97, 101, 125, 5]
# False qayitmalidir
print(massiv_siralidirmi(massiv2))
