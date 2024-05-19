def digital_root(n):
    n = n
    while len(str(n)) > 1:
        lst = [numb for numb in str(n)]
        n = 0
        for i in lst:
            n += int(i)
    return n




print(digital_root(493193))