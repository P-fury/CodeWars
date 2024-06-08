def create_phone_number(n):
    phone_nr = '('
    for x in range(len(n)):
        if x < 3:
            phone_nr += f'{n[x]}'
        if x == 3:
            phone_nr += ') '
        if x >= 3 and x <= 5:
            phone_nr += f'{n[x]}'
        if x == 6:
            phone_nr += '-'
        if x >= 6:
            phone_nr += f'{n[x]}'
    return (phone_nr)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def create_phone_number2(n):
    a = ''
    a += ''.join([str(x) for x in n])
    return f'({a[:3]}) {a[3:6]}-{a[6:10]}'


print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
