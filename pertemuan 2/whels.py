i = 1
while i <=5 :
    if i == 4:
        i = i+1
        continue
    else:
        print(i)
        i = i+1


num =int(input('enter a number'))
while num >= 0:
    if num == 0:
        print('equal to zero')
    elif num > 0:
        print('greater than zero')
    else:
        print('enter a valid number')
    break