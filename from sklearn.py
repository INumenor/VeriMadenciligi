from sklearn.neighbors import KDTree
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree

# Örnek veri kümesi oluşturma
iris = load_iris()

# İlk iki öznitelikleri seçme
X = iris.data[:, :2]
y = iris.target

# Scatter plot oluşturma
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Çanak Yaprak Uzunluğu (cm)')
plt.ylabel('Çanak Yaprak Genişliği (cm)')
plt.title('Iris Veri Seti')
plt.show()


# KDD-Tree modeli oluşturma
kdt = KDTree(X, leaf_size=2)

query = X[0]
query = query.reshape(1, -1)
# KDD-Tree modelini kullanarak sorgu verilerine en yakın komşuları bulma
dist, ind = kdt.query(query, k=2)

# Sonuçları ekrana yazdırma
print("Sorgu verileri:")
print(query)
print("En yakın komşuların indeksleri:")
print(ind)
print("En yakın komşuların mesafeleri:")
print(dist)