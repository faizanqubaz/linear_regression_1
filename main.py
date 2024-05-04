import pandas as pd
from distribution import check_distribution
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# READ THE DATASET

data = pd.read_csv(r"C:/Users/CL/Desktop/placement.csv")

# distribution
check_distribution(data)

X_train,X_test,Y_train,Y_test = train_test_split(data.iloc[:,0:1],data.iloc[:,-1],test_size=0.2,random_state=2)


lr = LinearRegression()

lr.fit(X_train,Y_train)



print('X_test',X_train)
print('Y_test',Y_train)

lr_predect=lr.predict(X_test.iloc[1].values.reshape(-1,1))
print('lr_predect',lr_predect)


# YOU NEED TO SHOW IF THE BEST FIT LINE

plt.figure(figsize=(12,12))
sns.scatterplot(x=data['cgpa'],y=data['package'],data=data)
plt.plot(X_test,lr.predict(X_test),color='red')
plt.show()