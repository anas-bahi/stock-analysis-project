import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("aapl_us_d.csv")

data = data.dropna()

data["Day"] = range(len(data))

X = data[["Day"]]
y = data["Close"]

model = LinearRegression()
model.fit(X, y)

future_days = [[len(data) + i] for i in range(30)]

predictions = model.predict(future_days)

plt.plot(data["Close"], label="Real")
plt.plot(range(len(data), len(data)+30), predictions, label="Prediction")

plt.legend()
plt.show()