import numpy as np
np.set_printoptions(precision=3)
import matplotlib.pyplot as plt
from multiprocessing.pool import Pool
from time import time
import matplotlib


R_max = 50
N = 100000


def plot_matrix(V, text_in_grid=True, colorbar=False):
    farmers = [i + 1 for i in range(V.shape[0])]
    vegetables = farmers
    fig, ax = plt.subplots()
    im = ax.imshow(V)

    # We want to show all ticks...
    # ax.set_xticks(np.arange(len(farmers)))
    # ax.set_yticks(np.arange(len(vegetables)))
    tick_list = list(np.arange(0,R_max,5))
    ax.set_xticks(tick_list)
    ax.set_yticks(tick_list)
    # ... and label them with the respective list entries
    # ax.set_xticklabels(farmers)
    # ax.set_yticklabels(vegetables)
    ax.set_xticklabels([1]+list(np.arange(5,R_max+1,5)))
    ax.set_yticklabels([1]+list(np.arange(5,R_max+1,5)))

    # Rotate the tick labels and set their alignment.
    # plt.setp(ax.get_xticklabels(), ha="right")

    # Loop over data dimensions and create text annotations.
    if text_in_grid:
        for i in range(len(vegetables)):
            for j in range(len(farmers)):
                if V[i, j] != 0.0:
                    text = ax.text(j, i, f'{V[i, j]:.2f}', ha="center", va="center", color="w")

    ax.set_xlabel('Threshold')
    ax.set_ylabel('R', rotation=0)
    ax.set_title("Win Probability")
    if colorbar:
        for PCM in ax.get_children():
            if type(PCM) == matplotlib.image.AxesImage:
                break
        plt.colorbar(PCM, ax=ax)
    fig.tight_layout()
    plt.show()


def get_success_rate(R, r_star):
    seq = np.array(range(R))
    seq = seq + 1
    successes = 0
    for i in range(N):
        np.random.shuffle(seq)
        for r in range(r_star-1,R,1):
            if r==R-1:
                if seq[r] == 1:
                    successes += 1
                break
            if np.all(seq[0:r+1] > seq[r+1]):
                if seq[r+1] == 1:
                    successes += 1
                break
    return successes/N

# Non multiprocessing way
# R_max = 10
# result = np.zeros((R_max, R_max))
# for R in range(1,R_max+1):
#     for r_star in range(R):
#         result[R-1,r_star] = get_success_rate(R, r_star)

result = np.zeros((R_max, R_max))
inputs = []
for R in range(1,R_max+1):
    for r_star in range(R):
        inputs.append((R,r_star))

t0 = time()
pool = Pool(4)
res = pool.starmap(get_success_rate, inputs)

i = 0
for R in range(1,R_max+1):
    for r_star in range(R):
        result[R-1, r_star] = res[i]
        i += 1

print(result)
plot_matrix(result, text_in_grid=False, colorbar=True)


