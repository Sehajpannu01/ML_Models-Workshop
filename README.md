#KNN:
Introduction
The K-Nearest Neighbors (KNN) algorithm is a simple and intuitive supervised machine learning algorithm used for classification and regression tasks. The algorithm classifies a data point based on how its neighbors are classified.
How KNN Works
- Choosing K: Select the number of neighbors (K) you want to consider for classification.
- Distance Calculation: Calculate the distance between the new data point and all other points in the dataset using a distance metric (e.g., Euclidean, Manhattan).
- Finding Neighbors: Identify the K nearest neighbors based on the calculated distances.
- Voting: For classification, the algorithm assigns the class that is most common among the K neighbors. For regression, it computes the average of the K neighbors' values.

Distance Metrics
-Common distance metrics used in KNN include:

- Euclidean Distance


------------------------------------------------------------------------------------------------------------------------------------

#Linear Regression:
Linear Regression is a supervised learning algorithm used for predicting a continuous target variable based on one or more input features. It models the relationship between the dependent variable (target) and independent variables (features) by fitting a linear equation to the observed data.

In the simplest form, a linear regression equation can be written as:

y = mx+b
-Where:

-y is the predicted target value,
-m = coefficient 
-b = intercept
​
-The goal of linear regression is to minimize the error between the predicted and actual values by optimizing the model coefficients.

Applications:

1.Predicting house prices based on features like size, location, etc.
2.Predicting Canada per capita income on yearly basis.
3.Predicting Salaries of employees on basis of experience
4.Estimating sales based on advertisement spending.
5.Forecasting trends in time-series data.

Linear regression assumes a linear relationship between the input variables and the output, and it works best when this assumption holds true. It is simple yet powerful, often serving as the baseline model in regression tasks.
