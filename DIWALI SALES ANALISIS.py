import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("new diwali sales.xlsx")
print(df)

jj=df.head(1000)

df1=df.describe()
print(df1)

var1=df.loc[:,["State","Gender"]].value_counts()
print(var1) 
 
df5=df.shape
print(df5)

d3=df["Amount"].sum()
print(d3) 

d4=df.info()
print(d4)

d5=pd.isnull(df).sum()  # check for null values 
print(d5)

d6=df.where(df['Gender']=="F")
d7=d6.groupby("Product_Category")
print(d7.describe())

d8=df.where(df["Gender"]=="M")
d9=d8.groupby("Product_Category")
print(d9.describe())



x=jj["Amount"]
y=jj["State"]
plt.figure(figsize=(12,6))         #here we r cheaking which state makes high profit by state 
plt.xlabel('amount')
plt.ylabel('State')
plt.title("higest profit by states's",fontsize=15)
plt.bar(x,y)
plt.show()


  








