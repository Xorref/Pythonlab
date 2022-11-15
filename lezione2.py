def sum_list(x):
    tot = 0
    for item in x:
        tot = tot + item
        if item not in x:
            return None
    return tot

my_list = None
risultato = sum_list(my_list)
print(risultato)