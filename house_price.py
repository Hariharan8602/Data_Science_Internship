import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([500,700,800,1000,1200,1500]).reshape(-1,1)
y = np.array([100,150,180,210,250,300])

model = LinearRegression()
model.fit(X,y)

predicted_price = model.predict([[1500]])
print(f"Predicted price for 432 sq.ft house:{predicted_price[0]}")

plt.scatter(X,y,color='blue',label='Actual Data')
plt.plot(X,model.predict(X),color='red',label='Regression Line')
plt.xlabel('House size (sq.ft)')
plt.ylabel('Price (1000$)')
plt.show()