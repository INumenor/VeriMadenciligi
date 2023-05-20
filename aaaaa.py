import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# veri setini yükleme
data = pd.read_csv("boy_kilo2.csv")

# özellikler ve hedef değişken olarak ayırma
X = data.iloc[:, 1:3]
y = data.iloc[:, 3]
print(np.matrix(X))

plt.scatter(X.iloc[:,0], X.iloc[:,1], c=y, cmap='viridis')
plt.xlabel('Boy (cm)')
plt.ylabel('Kilo (kg)')
plt.title('Cinsiyet')
plt.show()


# verileri eğitim ve test kümelerine bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
for k in [1, 3, 5]:
    #knn = KNeighborsClassifier(n_neighbors=k)
    knn = KNeighborsClassifier(weights='distance')
    

    # modeli eğitme
    knn.fit(X_train, y_train)

    # test seti üzerinde tahmin yapma
    y_pred = knn.predict(X_test)

    # tahmin başarısını hesaplama
    accuracy = knn.score(X_test, y_test)
    print("K={} için test seti doğruluğu: {:.2f}".format(k, accuracy))