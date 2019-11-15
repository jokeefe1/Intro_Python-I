import random
l = [ random.randint(-25, 20) for i in range(10)]
print(l)

l2 = [ random.randint(-25, 20) for num in range(10)]
print(l2)

my_sample = random.sample(l2, 3)
print(my_sample)