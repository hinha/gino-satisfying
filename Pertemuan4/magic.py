class Operasi(object):
    def __init__(self, math_list):
        self.math_list = math_list

    def __sub__(self, other):
        minuslst = []
        zipped = zip(self.math_list, other.math_list)
        for tup in zipped:
            minuslst.append(tup[0] - tup[1])

        return Operasi(minuslst)

    def __add__(self, other):
        addlst = [x + y for x, y in zip(self.math_list, other.math_list)]
        return Operasi(addlst)

    def __mul__(self, other):
        mullst = [x * y for x, y in zip(self.math_list, other.math_list)]
        return Operasi(mullst)

    def __repr__(self):
        return str(self.math_list)


x = Operasi([100, 90, 80, 70, 60])
y = Operasi([10, 9, 8, 7, 6])

p = x - y
z = x + y
q = x * y

print('Pengurangan: ' + str(p))
print('Tambah: ' + str(z))
print('Perkalian: ' + str(q))