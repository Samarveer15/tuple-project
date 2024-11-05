tup1 = (4, 3, 2, 1, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)


result = tuple(a * b for a, b in zip(tup1, tup2))


print(result)