
# Simple Linear Regression File
# Author : Deepak Pradeep Kumar
setwd("D:\\Personal\\DataPlatformGeeks\\Mar092019")

#Import the dataset
dataset = read.csv("Salary.csv")

#dividing the dataset into trainingset and testset
#install.packages('caTools')
library(caTools)
set.seed(123)

fragment = sample.split(dataset$Salary, SplitRatio = 2/3, group = NULL)
trainingset = subset(dataset, fragment == TRUE)
testset = subset(dataset, fragment == FALSE)

#Fitting simple Linear model to training set
LinearRegressor = lm(formula = Salary ~ YearsOfExperience,
                     data = trainingset )

summary(LinearRegressor)

#Predicting the Test Set Results
Predictor = predict(LinearRegressor, newdata = testset)

# Plotting the graph on testset results using ggplot2
#install.packages('ggplot2')
library(ggplot2)

ggplot() + 
  geom_point(aes(x = testset$YearsOfExperience, y = testset$Salary), 
             colour = 'blue') + 
  geom_line(aes(x = testset$YearsOfExperience, y= Predictor),
            colour = 'red') +
  ggtitle('Salary vs Experience') +
  xlab('YearsOfExperience') +
  ylab('Salary')

# Checking and validating the predicted results

testset1 = read.csv('validating.csv')

predict(LinearRegressor, newdata = testset1)










