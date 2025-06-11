import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    'Age': np.random.randint(18,60,100),
    'Salary': np.random.randint(30000,100000,100),
    'Work_experience': np.random.randint(0,40,100)
}

df = pd.DataFrame(data)

print("data_summary:\n",df.describe())

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.hist(df['Age'],bins=10,color='blue',alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Freuqnecy')
plt.title('Age Distribution')

plt.subplot(1,2,2)
plt.scatter(df['Work_experience'],df['Salary'],color='red',alpha=0.6)
plt.xlabel("Years of experience")
plt.ylabel('Salary')
plt.title("Salary vs Experience")

plt.show()