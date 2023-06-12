import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import openpyxl



Game=pd.read_csv('./rankedrm.csv',encoding="Windows-1254")

karsilasmalar = Game[['matchup', 'civ.win.name']]

ulkegucsiralamasi = Game['civ.win.name'].value_counts()/(Game['civ.win.name'].value_counts()+Game['civ.lose.name'].value_counts())
ulkegucsiralamasi = ulkegucsiralamasi.sort_values(ascending = False).reset_index().rename_axis("rank", axis='columns').rename(columns={'index':'civs'})
#Isimler alfabetik olarak gelsin diye
ulkegucsiralamasi = ulkegucsiralamasi.sort_values('civs')

ulkelerdf = ulkegucsiralamasi[['civs']]
ulkeler = ulkelerdf.to_numpy()

olasiKarsilasmalar = []
workbook = openpyxl.load_workbook('ageof.xlsx')
sheet = workbook.active



for x in range(len(ulkeler)):
    for y in range(x,len(ulkeler)):
        veri = ulkeler[x] + "-" + ulkeler[y]
        olasiKarsilasmalar.append(veri)

for x in range(len(olasiKarsilasmalar)):
    matchupNames = str(olasiKarsilasmalar[x])[2:len(str(olasiKarsilasmalar[x]))-2]
    ulke = matchupNames.split('-')
    selected_rows = karsilasmalar[karsilasmalar['matchup'] == matchupNames]
    print(len(selected_rows))
    c1winsayac = 0
    c2winsayac = 0
    for y in range(len(selected_rows)):
        if selected_rows.iloc[y]['civ.win.name'] == ulke[0]:
            c1winsayac +=1
        else:    
            c2winsayac +=1

    print(c1winsayac)
    print(c2winsayac)
    #sheet['A'+str(x+1)] = str(selected_rows['matchup'])

    #workbook.save('ageof.xlsx')