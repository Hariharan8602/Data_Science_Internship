import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[2,4,1,3,5]

# Line plot
# plt.plot(x,y)

# add title and labels
# plt.title("simple line plot")
# plt.xlabel("X.axis")
# plt.ylabel("Y=axis")
# plt.show()

# plt.plot([1,2,3,4,5],[10,15,20,25,30],marker='o',linestyle='--',color='b')
# plt.title("Plot example")
# plt.show()

# bar plot
# categories=[4,6,2,8]
# values=[4,7,1,8]
# plt.bar(categories,values,color='skyblue')
# plt.title("Scatter Plot example")
# plt.show()

# Scatter Plot
# categories=[4,6,2,8]
# values=[4,7,1,8]
# plt.scatter(categories,values,color='r')
# plt.show()

# Histogram
# data = [22,87,43,2,14,19,67,54,32]
# plt.hist(data,bins=5,color='green',edgecolor='black')
# plt.title('Histogram example')
# plt.show()

# Pie chart
# labels = ["python",'java','cpp','javascript']
# sizes=[45,25,15,5]
# colors=['blue','red','green','yellow']
# plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)
# plt.title('Pie Chart')
# plt.show()

# Multiple Plots
# plt.subplot(1,2,1)
# plt.plot([1,2,3],[4,5,6])
# plt.title('plot 1')

# plt.subplot(1,2,2)
# plt.bar(['A','B','C'],[3,5,7])
# plt.title('Plot 2')

# plt.show()
# plt.plot([1,2,3],[4,5,6],label='Line 1')
# plt.plot([1,2,3],[6,5,4],label='Line 2')
# plt.legend(loc='upper left',title='Lines',fontsize='small')
# plt.title('Legend example')
# plt.show()

# Grid example
plt.figure(figsize=(10,5))
plt.plot([1,2,3],[4,5,6])

plt.grid()
plt.show()





