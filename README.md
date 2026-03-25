# Stock Market Analysis and Price Prediction (Python)

## Project Overview

This project performs stock market data analysis and future price prediction using Python.
Historical stock data is loaded from a CSV dataset, cleaned, analyzed, visualized, and used to train a machine learning model to predict future prices.

The goal of this project is to demonstrate data analysis, visualization, and basic machine learning skills that are commonly required for Data Analyst / Data Science roles.

---

## Technologies Used

* Python 3
* pandas
* matplotlib
* scikit-learn
* numpy

---

## Dataset

The dataset contains historical daily stock prices with the following columns:

* Date
* Open
* High
* Low
* Close
* Volume

The data is loaded from:

```
aapl_us_d.csv
```

---

## Project Steps

### 1. Data Loading

The dataset is loaded using pandas.

### 2. Data Cleaning

Missing values are removed and the data is sorted by date.

### 3. Data Visualization

Stock closing prices are plotted using matplotlib to observe trends.

### 4. Feature Engineering

A numeric time index is created to train the prediction model.

### 5. Machine Learning Model

A Linear Regression model from scikit-learn is used to learn the relationship between time and price.

### 6. Prediction

The model predicts stock prices for the next 30 days.

### 7. Visualization of Prediction

The real prices and predicted future prices are plotted together.

---

## Example Output

* Historical price graph
* Future prediction graph
* Machine learning regression model

---

## How to Run

1. Clone the repository

```
git clone https://github.com/anas-bahi/stock-analysis-project.git
```

2. Install dependencies

```
pip install pandas matplotlib scikit-learn numpy
```

3. Run the script

```
python main.py
```

---

## Skills Demonstrated

* Data analysis with pandas
* Data visualization with matplotlib
* Machine learning with scikit-learn
* Time series style prediction
* Working with real-world datasets
* Project structure for GitHub

---

## Future Improvements

* Train / test split
* Accuracy metrics (R², MSE)
* Multiple stocks comparison
* Advanced models (Random Forest, LSTM)
* Interactive dashboard

---

## Author

Anas Bahi
