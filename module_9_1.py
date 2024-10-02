def apply_all_func(int_list: (int, float), *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

def min_1(l):
    return min(l)
def max_1(l):
    return max(l)
def len_1(l):
    return len(l)
def sum_1(l):
    return sum(l)
def sorted_1(l):
    return sorted(l)

print(apply_all_func([6, 20, 15, 9], min_1, max_1))
print(apply_all_func([6, 20, 15, 9], len_1, sum_1, sorted_1))




