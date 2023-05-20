import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

Game=pd.read_csv('./Game.csv')

GameTitle = input("Oyunu ismi Nedir?")

print(Game.loc[Game.Title==GameTitle])
