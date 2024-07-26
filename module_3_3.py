def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [6, 5, 4]
values_dict = {'a': 10, 'b': "Hello", 'c': 10}
values_list_2 = [7, "Строка"]

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
