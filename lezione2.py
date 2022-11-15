def sum_list(x):
    tot = 0
    for item in x:
        tot = tot + item
    return tot

my_list = [1, 2, 3, 4]
risultato = sum_list(my_list)
print(risultato)