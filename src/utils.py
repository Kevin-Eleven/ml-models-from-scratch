import numpy as np
import matplotlib.pyplot as plt


def mean_squared_error(y_true, y_pred):
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    return np.mean((y_true - y_pred) ** 2)


def plot_line(X, y, model):
    X = np.array(X)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    y_pred = model.predict(X)

    plt.scatter(X[:0], y, color="blue", label="Data points")
    plt.plot(X, y_pred, color="red", label="Fitted line")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()
    plt.show()
