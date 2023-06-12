import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

win_rate_table=pd.read_csv('./rankedrm.csv',encoding="Windows-1254")

size = len(win_rate_table.index)
map_types = win_rate_table['map_type.name'].value_counts().reset_index().rename(columns={'index':'maps','map_type.name':'num_games'})
map_types.index += 1

map_types['percentage'] = map_types['count'] * 100 / size

print(map_types)

map_types_plot = win_rate_table['map_type.name'].value_counts().plot.pie()
plt.show()

#--------------------------------------------------------------------


win_rate_all = win_rate_table['civ.win.name'].value_counts()/(win_rate_table['civ.win.name'].value_counts()+win_rate_table['civ.lose.name'].value_counts())
win_rate_all = win_rate_all.sort_values(ascending = False).reset_index().rename_axis("rank", axis='columns').rename(columns={'index':'civs',0:'win_rate'})

num_civ = len(win_rate_all.index)

win_rate_all['count'] = win_rate_all['count'] * 100
print(win_rate_all)
win_rate_all.index += 1
win_rate_all['advantage'] = win_rate_all['count'] - 50
        
#print("In", size, "recorded AOE2 ranked 1v1 games, the win rates of the" ,num_civ, "civs are as follows: \n")

print(win_rate_all)

#--------------------------------------------------------------------


win_rate_table_low = win_rate_table.loc[win_rate_table['rating.win' ] < 1000]
size_low = len(win_rate_table_low.index)
win_rate_table_mid = win_rate_table.loc[win_rate_table['rating.win'] >= 1000]
win_rate_table_mid = win_rate_table_mid.loc[win_rate_table['rating.win'] < 1300]
size_mid = len(win_rate_table_mid.index)
win_rate_table_high = win_rate_table.loc[win_rate_table['rating.win'] >= 1300]
size_high = len(win_rate_table_high.index)


elos = pd.DataFrame({ 
              'num_games': [size_low, size_mid, size_high, size]},
             index=['low_elo', 'mid_elo','high_elo','total'])

print(elos)
elos_plot = elos.iloc[0:3].plot.pie(y = 'num_games')
plt.show()

#--------------------------------------------------------------------


win_rate_low = win_rate_table_low['civ.win.name'].value_counts()/(win_rate_table_low['civ.win.name'].value_counts()+win_rate_table_low['civ.lose.name'].value_counts())
win_rate_low = win_rate_low.sort_values(ascending = False).reset_index().rename_axis("rank", axis='columns').rename(columns={'index':'civs',0:'win_rate'})
'''
win_rate_low = win_rate_low.to_string(formatters={
    'win_rate': '{:,.2%}'.format
})
'''
win_rate_low['count'] = win_rate_low['count'] * 100
win_rate_low.index += 1
win_rate_low['advantage'] = win_rate_low['count'] - 50

print("In ", size_low, " recorded AOE2 low elo ( < 1000 ) ranked 1v1 games, the win rate of the civs are as follows: \n")

#--------------------------------------------------------------------
print(win_rate_low)

win_rate_mid = win_rate_table_mid['civ.win.name'].value_counts()/(win_rate_table_mid['civ.win.name'].value_counts()+win_rate_table_mid['civ.lose.name'].value_counts())
win_rate_mid = win_rate_mid.sort_values(ascending = False).reset_index().rename_axis("Rank", axis='columns').rename(columns={'index':'civs',0:'win_rate'})
'''
win_rate_mid = win_rate_mid.to_string(formatters={
    'win_rate': '{:,.2%}'.format
})
'''

win_rate_mid['count'] = win_rate_mid['count'] * 100
win_rate_mid.index += 1
win_rate_mid['advantage'] = win_rate_mid['count'] - 50

print("In ", size_mid, " recorded AOE2 middle elo (1000-1300) ranked 1v1 games, the win rate of the civs are as follows: \n")


print(win_rate_mid)

#--------------------------------------------------------------------

win_rate_high = win_rate_table_high['civ.win.name'].value_counts()/(win_rate_table_high['civ.win.name'].value_counts()+win_rate_table_high['civ.lose.name'].value_counts())
win_rate_high = win_rate_high.sort_values(ascending = False).reset_index().rename_axis("Rank", axis='columns').rename(columns={'index':'civs',0:'win_rate'})
'''win_rate_high = win_rate_high.to_string(formatters={
    'win_rate': '{:,.2%}'.format
})
'''
win_rate_high['count'] = win_rate_high['count'] * 100
win_rate_high.index += 1
win_rate_high['advantage'] = win_rate_high['count'] - 50

print("In ", size_high, " recorded AOE2 high elo (>= 1300) ranked 1v1 games, the win rate of the civs are as follows: \n")
print(win_rate_high)

#--------------------------------------------------------------------
