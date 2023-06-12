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

X_train = GameFinal.drop(['rating.win', 'rating.lose', 'map_type', 'civ.win.name','civ.lose.name','matchup'],axis=1)
y_train = GameFinal['civ.win.name']

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Kategorik verileri sayısal değerlere dönüştürün
treeModel = DecisionTreeClassifier()

treeModel.fit(X_train,y_train)

treeModel.score()