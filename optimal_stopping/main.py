import numpy as np
np.set_printoptions(precision=3)
from itertools import permutations



def count():
    r = 6
    R = 6
    perms = permutations(range(1,R+1,1))
    perms = [np.array(p) for p in perms]
    options = [p for p in perms if (p[r-1] < p[0:r-1]).all()]
    n_options = len(options)
    n_optimal = len([p for p in options if p[r-1]==1])
    print('possible options', n_options)
    print('possible optimals', n_optimal)
    print('possible non-optimals', n_options-n_optimal)
    print('Win probability given option', n_optimal / n_options)
    print('Probability of having option', n_options / len(perms))


def get_VA():
    R_max = 10
    V = np.zeros((R_max,R_max))
    A = np.zeros((R_max,R_max))
    for R in range(1,R_max,1):
        V[R,R] = 1/(R+1)
        for r in range(R-1,-1,-1):
            V[R,r] = ( np.max([(r+1)/(R+1), V[R,r+1]]) * (1/(r+1)) ) + ( V[R,r+1] * (1-(1/(r+1))) )
            if (r+1)/(R+1) >= V[R,r+1]:
                A[R,r] = (r+1)/(R+1)
    return V, A


V, A = get_VA()
print(V)
print(A)






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







