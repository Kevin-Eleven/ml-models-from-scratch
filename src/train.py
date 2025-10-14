import numpy as np
import pandas as pd
from model import LinearRegression
from utils import mean_squared_error, plot_line

df = pd.read_csv("data/Student_Performance.csv")

X = df.iloc[:, [0, 1, 3, 4]].values
y = df.iloc[:, 5].values

print(df.head())
# Generate sample data
# np.random.seed(42)  # reproducible results
# X = np.linspace(0, 10, 50)  # shape (50,)
# y = 2 * X + 1 + np.random.randn(50)  # shape (50,) with noise

# Initialize and train model
model = LinearRegression(lr=0.00001, epochs=1000)
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluate
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)
print("Learned parameters: w =", model.w, ", b =", model.b)

# Plot
plot_line(X, y, model)
