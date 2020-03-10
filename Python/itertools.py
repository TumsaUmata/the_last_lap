import itertools


abc = ['a', 'b', 'c']
print(list(itertools.permutations(abc, 3)))
print(list(itertools.combinations(abc, 3)))
