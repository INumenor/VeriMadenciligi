import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

Game=pd.read_csv('./rankedrm.csv',encoding="Windows-1254")

MatchupTeam = input("Enter Your Choice : ")
MatchupTeam2 = input("Enter Opponent's Choice :")

siralama = sorted([MatchupTeam, MatchupTeam2])
sonuc = '-'.join(siralama)

GameFinal = Game.loc[Game.matchup==sonuc]

X = GameFinal[['civ.win.name', 'civ.lose.name']]
y = GameFinal['matchup']

# Kategorik verileri sayısal değerlere dönüştürün
label_encoder = LabelEncoder()
X['civ.win.name'] = label_encoder.fit_transform(X['civ.win.name'])
X['civ.lose.name'] = label_encoder.transform(X['civ.lose.name'])

# Train ve test setlerini oluşturun
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sınıflandırma modelini oluşturun ve eğitin
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapın
tahminler = model.predict(X_test)

# Modelin doğruluğunu değerlendirin
dogruluk = accuracy_score(y_test, tahminler)
print("Model Doğruluğu:", dogruluk)

# Örnek bir giriş verisi üzerinde tahmin yapın
ornek_veri = pd.DataFrame({'civ.win.name': [MatchupTeam], 'civ.lose.name': [MatchupTeam2]})
ornek_veri['civ.win.name'] = label_encoder.transform(ornek_veri['civ.win.name'])
ornek_veri['civ.lose.name'] = label_encoder.transform(ornek_veri['civ.lose.name'])
tahmin = model.predict(ornek_veri)
print("Tahmin:", tahmin)