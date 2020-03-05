# programa do 100 primos 
num = 1
cont = 0
primos = 0
x = 0
while True:
    primos += 1

    while primos != num:
        if primos % num ==0:
            cont += 1
        num += 1    

    if cont == 2:
        print(primos)        

