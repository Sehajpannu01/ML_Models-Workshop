Introduction
The K-Nearest Neighbors (KNN) algorithm is a simple and intuitive supervised machine learning algorithm used for classification and regression tasks. The algorithm classifies a data point based on how its neighbors are classified.
How KNN Works
- Choosing K: Select the number of neighbors (K) you want to consider for classification.
- Distance Calculation: Calculate the distance between the new data point and all other points in the dataset using a distance metric (e.g., Euclidean, Manhattan).
- Finding Neighbors: Identify the K nearest neighbors based on the calculated distances.
- Voting: For classification, the algorithm assigns the class that is most common among the K neighbors. For regression, it computes the average of the K neighbors' values.

Distance Metrics
-Common distance metrics used in KNN include:

1. Euclidean Distance
2. Manhattan Distance
3. Minkowski Distance
