import numpy as np
np.set_printoptions(precision=5)
from itertools import permutations
import matplotlib.pyplot as plt


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


def get_V(R_max):
    V = np.zeros((R_max,R_max))
    for R in range(R_max):
        V[R,R] = 1/(R+1)
        for r in range(R-1,-1,-1):
            V[R,r] = ( np.max([(r+1)/(R+1), V[R,r+1]]) * (1/(r+1)) ) + ( V[R,r+1] * (1-(1/(r+1))) )
    return V


def get_thresholds(V):
    thresholds = []
    for row in V:
        # non_zeros = row[row != 0]
        # plt.clf()
        # plt.scatter(range(len(non_zeros)), non_zeros)
        # plt.show()
        for i in range(len(row)):
            if (row[i+1] + 1e-5) < row[i]:
                thresholds.append(i)
                break
    return thresholds

V = get_V(R_max=1000)
thresholds = get_thresholds(V)
win_probabilities = np.max(V,axis=1)
print(win_probabilities)
plt.scatter(range(1,len(thresholds)+1,1), thresholds)
# plt.show()
# plt.clf()

thresholds_relative = [t/(R+1) for R,t in enumerate(thresholds)]
plt.scatter(range(1,len(thresholds)+1,1), thresholds_relative)
# plt.show()


