import pandas as pd
# data = [10,20,30,40]
# series = pd.Series(data)
# print(series)

# data = {
#     "Name":['arun','kiran','vimal','vikram','siva','mohan','kumar','anirudh'],
#     "age": [15,23,18,56,21,45,37,24],
#     "Place": ["London","Chicago","Seattle","Hong kong",'washington','Britain','Mumbai','Beijing']
# }

# df = pd.DataFrame(data,index=[1,2,3,4,5,6,7,8])
# df.drop('Place',axis=1,inplace=True)
# print(df['Name'])

# filtered = df[df['age']>25]
# print(filtered)

# df.to_csv("data.csv",index=False)
# df = pd.read_csv('data.csv',usecols=['Name','age'])

# print(df.loc[6])
# print(df.iloc[0])



# df = pd.read_csv("C:/Users/harih/OneDrive/Desktop/M.Tech/mini_project/uber_data.csv")
# print(df.head())

# new_data = {
#     "Name":["David"],
#     "Age":[29],
#     "Place":["India"]
# }
# new_df = pd.DataFrame(new_data)

# new_df.to_csv("data.csv",mode='a',index=False,header=False)
# df = pd.read_csv('data.csv',usecols=)

data = {
    "Name":['arun','kiran','vimal','vikram','siva','mohan','kumar','anirudh'],
    "age": [15,23,18,None,21,45,37,24],
    "Place": ["London","Chicago","Seattle","Hong kong",'washington','Britain','Mumbai','Beijing']
}
df = pd.DataFrame(data)
# df.fillna({'Name':'Vinay','age':0,"Place":'Unknown'},inplace=True)
# # df.dropna(inplace=True)
# df.insert(1,'City',['America','Europe','Australia','Sydney','d','e','f','g'])
df.rename({'Place':'Nationality'})
print(df)