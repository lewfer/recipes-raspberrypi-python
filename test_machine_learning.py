# Import Python libraries for data manipuation and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot

# Import the Python machine learning libraries we need
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the data set
dataset = pd.read_csv("world_data.csv")

# Split into input and output features
y = dataset["happiness"]
X = dataset[["lifeexp","income"]]

# Split into test and training sets
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=test_size, random_state=seed)

# Select algorithm
model = LogisticRegression()

# Fit model to the data
model.fit(X_train, y_train)

# Check model performance on training data
predictions = model.predict(X_train)
print("Training score", accuracy_score(y_train, predictions))

# Evaluate the model on the test data
predictions = model.predict(X_test)

# Compute the accuracy score
print("Test score", accuracy_score(y_test, predictions))