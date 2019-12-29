
for i in range(0, 10, 2):
    print(i)

nama = ['Lily', 'Brad', 'Fatima', 'Zining']

for nam in nama:
    print(nam)

for letter in 'Lily':
    print(letter)


ev_data = [['Kendaraan', 'Jarak', 'Harga'],
           ['Tesla Model 3 LR', '310', '49900'],
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]
for row in ev_data[1:]:
    ev_range = row[1]
    ev_range = int(ev_range)
    row[1] = ev_range



data_mobil1 = [['Tesla Model 3 LR', '310', '49900'],
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]

data_mobil2 = [['Mobilio', '310', '49900'],
           ['Ford Gt', '154', '30315'],
           ['Chevy', '218', '36620']]

for data1, data2 in zip(data_mobil1, data_mobil2):
    print(data1)