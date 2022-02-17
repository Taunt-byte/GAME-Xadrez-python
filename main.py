import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Tabuleiro

board = np.quad([1,0], [8,4])

for i in range(board.shape[0]):
    board[i] = np.roll(board[i], i %2)

cmap = ListedColormap(['#779556', '#ebecd0'])
plt.matshow(board, cmap=cmap, )
plt.xticks([])
plt.yticks([])
plt.show()