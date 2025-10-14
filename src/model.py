import numpy as np


class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = None

    def fit(self, X, y):
        # Ensure X and y are 2D and 1D arrays respectively
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(
                -1, 1
            )  # reshapes the array -1 means figure out rows automatically
        y = np.array(y).flatten()  # shape (n_samples,)

        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.epochs):
            y_pred = np.dot(X, self.w) + self.b
            dw = -(2 / n_samples) * np.dot(X.T, (y - y_pred))  # shape (n_features,)
            db = -(2 / n_samples) * np.sum(y - y_pred)

            # Update weights and bias
            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return np.dot(X, self.w) + self.b
