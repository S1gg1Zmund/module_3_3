def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 2,3)
print_params(1, 2)
print_params(2)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list_ = ["wish", False, 10]
values_dict = {'a': 120, 'b': 3209, 'c': 676}
print_params(*values_list_)
print_params(**values_dict)
values_list_2 = ["Hello", 25]
print_params(*values_list_2, 42)