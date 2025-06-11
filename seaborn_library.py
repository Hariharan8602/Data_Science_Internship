import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset("tips")
# sns.scatterplot(x="total_bill",y="tip",data=dataset)
#sns.histplot(data=dataset,x='total_bill',kde=True,bins=20)
#sns.kdeplot(x=dataset["total_bill"],fill=True)
#sns.violinplot(x="day",y="total_bill",data=dataset)
sns.pairplot(dataset,hue='tip')
plt.show()
# print(dataset.head())