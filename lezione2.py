def sum_list(x):
    tot = 0
    for item in x:
        tot = tot + item
    return tot

my_list = [3, 9, 5, 10]
risultato = sum_list(my_list)
print(risultato)