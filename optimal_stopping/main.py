import numpy as np
from itertools import permutations


r = 5
N = 6

def count():
    perms = permutations(range(1,N+1,1))
    perms = [np.array(p) for p in perms]
    options = [p for p in perms if (p[r-1] < p[0:r-1]).all()]
    n_options = len(options)
    n_optimal = len([p for p in options if p[r-1]==1])
    prob_success = n_optimal / n_options
    print('N possible options', n_options)
    print('N possible optimals', n_optimal)
    print('N possible non-optimals', n_options-n_optimal)
    print('Win probability', prob_success)

count()








# ranks = np.array([4,3,1,2,0])

# N = 100

# def I(k):
#     if k == N:
#         return 1
#     elif np.any(ranks[0:k] < ranks[k]):
#         return 0
#     else:
#         return 1

# def r(k):
#     if k == N:
#         return 0
#     if k == 0:
#         return 0
#     return (N - k) / k
#
# R = 0
# s = 0
# for k in range(N,-1,-1):
#     R += r(k)
#     s += 1
#     if R >= 1:
#         break
#
# Q = 1
# for k in range(N,s-1,-1):
#     Q *= k/N
#
#
# print('\nN', N)
# print('s', s)
# print('\nR', R)
# print('Q', Q)
# print(Q*R)







