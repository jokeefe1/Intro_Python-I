# import random
# l = [ random.randint(-25, 20) for i in range(10)]
# print(l)

# l2 = [ random.randint(-25, 20) for num in range(10)]
# print(l2)

# my_sample = random.sample(l2, 3)
# print(my_sample)


# odd = lambda x : bool(x % 2)
# numbers = [ n for n in range(10)]
# numbers[:] = [ n for n in numbers if not odd(n)]
# print(numbers)


d1 = {'arg1': 'John', 'arg2': 'Candy', 'arg3': 'Jane' }

def print_kwargs(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

print_kwargs(**d1)