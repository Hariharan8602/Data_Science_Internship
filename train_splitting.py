import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data = {
    'Size': [
        1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
        2100, 2200, 2300, 2400, 2500, 2600, 2800, 3000, 3200, 3400,
        3600, 3800, 4000, 4200, 4500, 4800, 5100, 5500, 6000, 6500
    ],
    'Bedrooms': [
        2, 2, 2, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 4, 4, 4, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5, 5, 5, 6, 6
    ],
    'Price': [
        3000000, 3200000, 3500000, 3700000, 4000000, 4200000, 4500000, 4800000, 5000000, 5200000,
        5400000, 5600000, 5800000, 6000000, 6200000, 6400000, 6700000, 7000000, 7300000, 7600000,
        8000000, 8200000, 8500000, 8700000, 8900000, 9200000, 9400000, 9600000, 10200000, 10800000
    ]
}
df = pd.DataFrame(data)

X = df[['Size','Bedrooms']]
y = df['Price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict([[X_test]])
print(X_test)
print(y_pred)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"Mean squared error:{mse}")
print(f'R2 score:{r2}')