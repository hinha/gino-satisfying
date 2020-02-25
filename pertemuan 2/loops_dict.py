




cc = {
    '1': "angka satu",
    '2': "angka dua",
    '3': "angka tiga",
    '4': "angka empat",
}

data_masuk = str(input("angka: "))
data_nilai = input("nilai: ")
if data_masuk not in cc:
    cc.update({data_masuk: data_nilai})



final = []
    
x = dict(sorted(cc.items(), key=lambda x: x[0], reverse=True))
# print(x)

for key, val in x.items():
    temp = (key, val)
    final.append(temp)

print(final)







