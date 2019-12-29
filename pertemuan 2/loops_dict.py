def get_limit(results, start, limit):
    
    start = int(start)
    limit = int(limit)
    count = len(results)
    
    offset = (start - 1) * limit
    pagermax = limit
    data = results[offset: offset+limit]
    
    
    return data




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







