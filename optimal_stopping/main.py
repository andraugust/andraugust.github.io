import numpy as np
np.set_printoptions(precision=3)
from itertools import permutations
import matplotlib.pyplot as plt


def plot_value_function():
    farmers = [i + 1 for i in range(V.shape[0])]
    vegetables = farmers
    fig, ax = plt.subplots()
    im = ax.imshow(V)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(farmers)))
    ax.set_yticks(np.arange(len(vegetables)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(farmers)
    ax.set_yticklabels(vegetables)

    # Rotate the tick labels and set their alignment.
    # plt.setp(ax.get_xticklabels(), ha="right")

    # Loop over data dimensions and create text annotations.
    for i in range(len(vegetables)):
        for j in range(len(farmers)):
            if V[i, j] != 0.0:
                text = ax.text(j, i, f'{V[i, j]:.2f}', ha="center", va="center", color="w")

    ax.set_xlabel('r')
    ax.set_ylabel('R', rotation=0)
    ax.set_title("Value Function")
    fig.tight_layout()
    plt.show()


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


def plot_thresholds():
    thresholds = get_thresholds(V)
    plt.scatter(range(1, len(thresholds) + 1, 1), thresholds)
    # plt.xticks([1,25,50,75,100,125,150,175,200])
    plt.xticks([1,5,10,15,20])
    plt.xlabel('R')
    plt.ylabel('Threshold')
    plt.show()


def plot_win_probability():
    win_probability = V[1:,0]
    plt.scatter(range(2, len(win_probability) + 2, 1), win_probability)
    plt.xticks([1,25,50,75,100,125,150,175,200])
    plt.xlabel('R')
    plt.ylabel('Win Probability')
    plt.show()


V = get_V(R_max=2500)
# plot_thresholds()
# exit()

thresholds = get_thresholds(V)
thresholds_relative = [t/(R+1) for R,t in enumerate(thresholds)]
print(thresholds_relative[-10:])



# win_probabilities = np.max(V,axis=1)
# print(win_probabilities)


# plt.scatter(range(1,len(thresholds)+1,1), thresholds_relative)
# plt.show()






