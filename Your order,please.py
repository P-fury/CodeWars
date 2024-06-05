import re


def order(sentence):
    numbers = []
    sorted_lst = []
    for word in sentence.split():
        numbers += (re.findall('\d', word))
    numbers.sort()
    for x in numbers:
        for word in sentence.split():
            if x in word:
                sorted_lst.append(word)
    return ' '.join(sorted_lst)


print(order("is2 Thi1s T4est 3a"))


def order2(sent):
    return ' '.join(sorted(sent.split(), key=min))


print(order2("is2 Thi1s T4est 3a"))
