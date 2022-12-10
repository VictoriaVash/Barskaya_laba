# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

# •	гистограмма: распределение хоккеистов по количеству участий в ЧМ;
# •	график: тренды изменения роста на протяжении всех ЧМ для каждой позиции (вратарь, защитник, нападающий);
# •	столбчатая диаграмма (вертикальная): распределение хоккеистов по месяцам рождения (по всему набору данных);
# •	круговая диаграмма: распределение позиций (вратарь, защитник, нападающий) между хоккеистами (по всему набору данных).


df = pd.read_csv('hockey_players.csv', encoding='cp1252')

playr_stat = df.name.value_counts()
all_playrs = playr_stat
all_playrs_sum = all_playrs.sum()
unic_player = len(all_playrs)
maxs = all_playrs[0]

list_doli = []
for i in range(maxs):
    i += 1
    all_playrss = all_playrs[(all_playrs.values == i)]
    list_doli.append(len(all_playrss) / unic_player)

# plt.bar(range(maxs), list_doli, color='red', width=1, edgecolor='darkblue')
#
# plt.title('Распределение хоккеистов по учасвствию в ЧМ')
# plt.xlabel('Количество ЧМ')
# plt.ylabel('Доля')
# plt.show()

max_year = max(df.year)
mix_year = min(df.year)
time_line = range(mix_year,max_year+1)
positions = ['Вратарь', 'Защитник', 'Нападающий']
positions = ['D', 'F', 'G']
D_year_stat = []
F_year_stat = []
G_year_stat = []

for year in time_line:
    all_players_this_year = df[df.year == year]
    for pos in positions:
        all_pos_player = all_players_this_year[all_players_this_year.position == pos]
        if pos == 'D': D_year_stat.append(all_pos_player.height.mean())
        elif pos == 'F': F_year_stat.append(all_pos_player.height.mean())
        elif pos == 'G': G_year_stat.append(all_pos_player.height.mean())

        print(all_pos_player.height.mean())
    print()
print(D_year_stat)
print(F_year_stat)
print(G_year_stat)
time_line = [i for i in time_line]
# Построим линии тренда
#create scatterplot
#plt.scatter(time_line, D_year_stat)

#calculate equation for trendline
z = np.polyfit(time_line, D_year_stat, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(time_line, p(D_year_stat), color="purple", linewidth=3, linestyle="--")
plt.show()
print(D_year_stat, time_line)