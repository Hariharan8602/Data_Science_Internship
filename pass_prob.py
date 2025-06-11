import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([0,0,0,0,1,1,1,1])

model = LogisticRegression()
model.fit(X,y)

prediction = model.predict([[4.5000]])
probability = model.predict_proba([[4.5000]])
print("Prediction(0=Fail, 1=Pass):",prediction[0])
print("Probability of passing:",probability[0][1])