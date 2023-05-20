import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv(r'C:/Users/Batuhan/Desktop/Game.csv',encoding='Windows-1254')

#print(df)

X = df.iloc[:,:50]
y = df.iloc[:,2:4]
#print(np.matrix(X))

plt.scatter(X.iloc[:,1],y.iloc[:,0], c="red", cmap='viridis')
plt.xlabel('Sales')
plt.ylabel('Title')
plt.title('Tablo')
plt.show()