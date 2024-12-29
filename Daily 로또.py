from itertools import permutations

s = list(permutations([i for i in range(1,46)]))

print('\n'.join(map(str,s)))