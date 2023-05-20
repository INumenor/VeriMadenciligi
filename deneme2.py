from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pickle


kelime1 = input("İlk kelimeyi girin: ")
kelime2 = input("İkinci kelimeyi girin: ")

siralama = sorted([kelime1, kelime2])
sonuc = '-'.join(siralama)

print("Sonuç:", sonuc)

