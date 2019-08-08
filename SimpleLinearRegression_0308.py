#Simple Linear Regression
"""
Created on Friday 03/08/2019 11:25 PM
@author: Deepak Pradeep Kumar
"""
#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing the data
dataset = pd.read_csv('Salary.csv')

# Validate the dataset
dataset.describe()

# Split into Dependent and Independent variables
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:, 1].values

#X = dataset.YearsOfExperience
#Y = dataset.Salary

# No Manipulation or Imputation of data is needed as this is a Sample and clean dataset.
#Splitting the dataset to Train and Test data.
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,Y, test_size = 0.3, random_state = 1)

#Fitting the Simple Linear Regression Model
from sklearn.linear_model import LinearRegression
LinearRegressor = LinearRegression()
LinearRegressor.fit(Xtrain, Ytrain)

# Predicting the Test Set Results
YPredictor = LinearRegressor.predict(Xtest)

# Evaluating the Intercept
LinearRegressor.intercept_

#Plotting the Graph for Predicted Test Set Results
plt.scatter(Xtest, Ytest, color = 'blue')
plt.plot(Xtest, YPredictor, color = 'red')
plt.title('Experience vs Salary')
plt.xlabel('Number of Years of Experience')
plt.ylabel('Salary')
plt.show()

YPred = LinearRegressor.predict(16.5)





