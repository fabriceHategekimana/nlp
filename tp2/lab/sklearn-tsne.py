import numpy as np
from sklearn.manifold import TSNE

# Keep close distance close and expend great distance greate


X = np.array([[0, 0, 0],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

X_embedded = TSNE(
    n_components=2, learning_rate="auto", init="random", perplexity=3
).fit_transform(X)

res = np.array([[-71.34111, -141.35843],
                [31.503876, 93.8399],
                [97.52083, -74.776985],
                [-136.15637, 27.545347]])


# assert ((X_embedded - res).sum() == 0)
print((X_embedded - res).sum())
