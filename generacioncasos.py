import numpy as np
import random
import copy
import time
w = 0
r = 1
g = 2
b = 3
y = 4
o = 5

U = 0
F = 1
L = 2
R = 3 
D = 4
B = 5
total = []
algoritmo = ''
secuencia_movimiento = []
cubo = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[y,y,y],[y,y,y],[y,y,y]],[[o,o,o],[o,o,o],[o,o,o]]]
#cubo = [[[w,w,w],[w,w,w],[w,o,w]],[[r,w,r],[r,r,r],[r,r,r]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[y,y,y],[y,y,y],[y,y,y]],[[o,r,o],[o,o,o],[o,o,o]]]
archivo = open('datos_buenos.csv','w')
archivo.write("U00,U01,U02,U10,U11,U12,U20,U21,U22,F00,F01,F02,F10,F11,F12,F20,F21,F22,L00,L01,L02,L10,L11,L12,L20,L21,L22,R00,R01,R02,R10,R11,R12,R20,R21,R22,D00,D01,D02,D10,D11,D12,D20,D21,D22,B00,B01,B02,B10,B11,B12,B20,B21,B22\n")
archivo.close()
tiempo_inicio = time.time()
for d in range(1000000):
    secuencia_movimiento = []
    for i in range((20)):
        num = random.randint(0,12)
        secuencia_movimiento.append(num)
    for i in range(len(secuencia_movimiento)):
        #algoritmo = ''
        cubo_actual = copy.deepcopy(cubo)
        if(secuencia_movimiento[i] == 0):
            #algoritmo += "U -"
            cubo[U][0][1] = cubo_actual[U][1][0]
            cubo[U][1][2] = cubo_actual[U][0][1]
            cubo[U][2][1] = cubo_actual[U][1][2]
            cubo[U][1][0] = cubo_actual[U][2][1]
            cubo[U][0][2] = cubo_actual[U][0][0]
            cubo[U][2][2] = cubo_actual[U][0][2]
            cubo[U][2][0] = cubo_actual[U][2][2]
            cubo[U][0][0] = cubo_actual[U][2][0]
            cubo[F][0][1] = cubo_actual[R][0][1]
            cubo[R][0][1] = cubo_actual[B][0][1]
            cubo[B][0][1] = cubo_actual[L][0][1]
            cubo[L][0][1] = cubo_actual[F][0][1]
            cubo[F][0][0] = cubo_actual[R][0][0]
            cubo[R][0][0] = cubo_actual[B][0][0]
            cubo[B][0][0] = cubo_actual[L][0][0]
            cubo[L][0][0] = cubo_actual[F][0][0]
            cubo[F][0][2] = cubo_actual[R][0][2]
            cubo[R][0][2] = cubo_actual[B][0][2]
            cubo[B][0][2] = cubo_actual[L][0][2]
            cubo[L][0][2] = cubo_actual[F][0][2]
        elif(secuencia_movimiento[i] == 1):
            #algoritmo += "U' -"
            cubo[U][1][0] = cubo_actual[U][0][1]
            cubo[U][0][1] = cubo_actual[U][1][2]
            cubo[U][1][2] = cubo_actual[U][2][1]
            cubo[U][2][1] = cubo_actual[U][1][0]
            cubo[U][0][0] = cubo_actual[U][0][2]
            cubo[U][0][2] = cubo_actual[U][2][2]
            cubo[U][2][2] = cubo_actual[U][2][0]
            cubo[U][2][0] = cubo_actual[U][0][0]
            cubo[R][0][1] = cubo_actual[F][0][1]
            cubo[B][0][1] = cubo_actual[R][0][1]
            cubo[L][0][1] = cubo_actual[B][0][1]
            cubo[F][0][1] = cubo_actual[L][0][1]
            cubo[R][0][0] = cubo_actual[F][0][0]
            cubo[B][0][0] = cubo_actual[R][0][0]
            cubo[L][0][0] = cubo_actual[B][0][0]
            cubo[F][0][0] = cubo_actual[L][0][0]
            cubo[R][0][2] = cubo_actual[F][0][2]
            cubo[B][0][2] = cubo_actual[R][0][2]
            cubo[L][0][2] = cubo_actual[B][0][2]
            cubo[F][0][2] = cubo_actual[L][0][2]
        elif(secuencia_movimiento[i] == 2):
            #algoritmo += "F -"
            cubo[F][0][1] = cubo_actual[F][1][0]
            cubo[F][1][2] = cubo_actual[F][0][1]
            cubo[F][2][1] = cubo_actual[F][1][2]
            cubo[F][1][0] = cubo_actual[F][2][1]
            cubo[F][0][2] = cubo_actual[F][0][0]
            cubo[F][2][2] = cubo_actual[F][0][2]
            cubo[F][2][0] = cubo_actual[F][2][2]
            cubo[F][0][0] = cubo_actual[F][2][0]
            cubo[L][0][2] = cubo_actual[D][0][0]
            cubo[U][2][2] = cubo_actual[L][0][2]
            cubo[R][2][0] = cubo_actual[U][2][2]
            cubo[D][0][0] = cubo_actual[R][2][0]
            cubo[L][1][2] = cubo_actual[D][0][1]
            cubo[U][2][1] = cubo_actual[L][1][2]
            cubo[R][1][0] = cubo_actual[U][2][1]
            cubo[D][0][1] = cubo_actual[R][1][0]
            cubo[L][2][2] = cubo_actual[D][0][2]
            cubo[U][2][0] = cubo_actual[L][2][2]
            cubo[R][0][0] = cubo_actual[U][2][0]
            cubo[D][0][2] = cubo_actual[R][0][0]
        elif(secuencia_movimiento[i] == 3):
            #algoritmo += "F' -"
            cubo[F][1][0] = cubo_actual[F][0][1]
            cubo[F][0][1] = cubo_actual[F][1][2]
            cubo[F][1][2] = cubo_actual[F][2][1]
            cubo[F][2][1] = cubo_actual[F][1][0]
            cubo[F][0][0] = cubo_actual[F][0][2]
            cubo[F][0][2] = cubo_actual[F][2][2]
            cubo[F][2][2] = cubo_actual[F][2][0]
            cubo[F][2][0] = cubo_actual[F][0][0]
            cubo[D][0][0] = cubo_actual[L][0][2]
            cubo[L][0][2] = cubo_actual[U][2][2]
            cubo[U][2][2] = cubo_actual[R][2][0]
            cubo[R][2][0] = cubo_actual[D][0][0]
            cubo[D][0][1] = cubo_actual[L][1][2]
            cubo[L][1][2] = cubo_actual[U][2][1]
            cubo[U][2][1] = cubo_actual[R][1][0]
            cubo[R][1][0] = cubo_actual[D][0][1]
            cubo[D][0][2] = cubo_actual[L][2][2]
            cubo[L][2][2] = cubo_actual[U][2][0]
            cubo[U][2][0] = cubo_actual[R][0][0]
            cubo[R][0][0] = cubo_actual[D][0][2]
        elif(secuencia_movimiento[i] == 4):
            #algoritmo += "L -"
            cubo[L][0][1] = cubo_actual[L][1][0]
            cubo[L][1][2] = cubo_actual[L][0][1]
            cubo[L][2][1] = cubo_actual[L][1][2]
            cubo[L][1][0] = cubo_actual[L][2][1]
            cubo[L][0][2] = cubo_actual[L][0][0]
            cubo[L][2][2] = cubo_actual[L][0][2]
            cubo[L][2][0] = cubo_actual[L][2][2]
            cubo[L][0][0] = cubo_actual[L][2][0]
            cubo[B][0][2] = cubo_actual[D][2][0]
            cubo[U][2][0] = cubo_actual[B][0][2]
            cubo[F][2][0] = cubo_actual[U][2][0]
            cubo[D][2][0] = cubo_actual[F][2][0]
            cubo[B][1][2] = cubo_actual[D][1][0]
            cubo[U][1][0] = cubo_actual[B][1][2]
            cubo[F][1][0] = cubo_actual[U][1][0]
            cubo[D][1][0] = cubo_actual[F][1][0]
            cubo[B][2][2] = cubo_actual[D][0][0]
            cubo[U][0][0] = cubo_actual[B][2][2]
            cubo[F][0][0] = cubo_actual[U][0][0]
            cubo[D][0][0] = cubo_actual[F][0][0]
        elif(secuencia_movimiento[i] == 5):
            #algoritmo += "L' -"
            cubo[L][1][0] = cubo_actual[L][0][1]
            cubo[L][0][1] = cubo_actual[L][1][2]
            cubo[L][1][2] = cubo_actual[L][2][1]
            cubo[L][2][1] = cubo_actual[L][1][0]
            cubo[L][0][0] = cubo_actual[L][0][2]
            cubo[L][0][2] = cubo_actual[L][2][2]
            cubo[L][2][2] = cubo_actual[L][2][0]
            cubo[L][2][0] = cubo_actual[L][0][0]
            cubo[D][2][0] = cubo_actual[B][0][2]
            cubo[B][0][2] = cubo_actual[U][2][0]
            cubo[U][2][0] = cubo_actual[F][2][0]
            cubo[F][2][0] = cubo_actual[D][2][0]
            cubo[D][1][0] = cubo_actual[B][1][2]
            cubo[B][1][2] = cubo_actual[U][1][0]
            cubo[U][1][0] = cubo_actual[F][1][0]
            cubo[F][1][0] = cubo_actual[D][1][0]
            cubo[D][0][0] = cubo_actual[B][2][2]
            cubo[B][2][2] = cubo_actual[U][0][0]
            cubo[U][0][0] = cubo_actual[F][0][0]
            cubo[F][0][0] = cubo_actual[D][0][0]
        elif(secuencia_movimiento[i] == 6):
            #algoritmo += "R -"
            cubo[R][0][1] = cubo_actual[R][1][0]
            cubo[R][1][2] = cubo_actual[R][0][1]
            cubo[R][2][1] = cubo_actual[R][1][2]
            cubo[R][1][0] = cubo_actual[R][2][1]
            cubo[R][0][2] = cubo_actual[R][0][0]
            cubo[R][2][2] = cubo_actual[R][0][2]
            cubo[R][2][0] = cubo_actual[R][2][2]
            cubo[R][0][0] = cubo_actual[R][2][0]
            cubo[F][0][2] = cubo_actual[D][0][2]
            cubo[U][0][2] = cubo_actual[F][0][2]
            cubo[B][2][0] = cubo_actual[U][0][2]
            cubo[D][0][2] = cubo_actual[B][2][0]
            cubo[F][1][2] = cubo_actual[D][1][2]
            cubo[U][1][2] = cubo_actual[F][1][2]
            cubo[B][1][0] = cubo_actual[U][1][2]
            cubo[D][1][2] = cubo_actual[B][1][0]
            cubo[F][2][2] = cubo_actual[D][2][2]
            cubo[U][2][2] = cubo_actual[F][2][2]
            cubo[B][0][0] = cubo_actual[U][2][2]
            cubo[D][2][2] = cubo_actual[B][0][0]
        elif(secuencia_movimiento[i] == 7):
            #algoritmo += "R' -"
            cubo[R][1][0] = cubo_actual[R][0][1]
            cubo[R][0][1] = cubo_actual[R][1][2]
            cubo[R][1][2] = cubo_actual[R][2][1]
            cubo[R][2][1] = cubo_actual[R][1][0]
            cubo[R][0][0] = cubo_actual[R][0][2]
            cubo[R][0][2] = cubo_actual[R][2][2]
            cubo[R][2][2] = cubo_actual[R][2][0]
            cubo[R][2][0] = cubo_actual[R][0][0]
            cubo[D][0][2] = cubo_actual[F][0][2]
            cubo[F][0][2] = cubo_actual[U][0][2]
            cubo[U][0][2] = cubo_actual[B][2][0]
            cubo[B][2][0] = cubo_actual[D][0][2]
            cubo[D][1][2] = cubo_actual[F][1][2]
            cubo[F][1][2] = cubo_actual[U][1][2]
            cubo[U][1][2] = cubo_actual[B][1][0]
            cubo[B][1][0] = cubo_actual[D][1][2]
            cubo[D][2][2] = cubo_actual[F][2][2]
            cubo[F][2][2] = cubo_actual[U][2][2]
            cubo[U][2][2] = cubo_actual[B][0][0]
            cubo[B][0][0] = cubo_actual[D][2][2]
        elif(secuencia_movimiento[i] == 8):
            #algoritmo += "D -"
            cubo[D][0][1] = cubo_actual[D][1][0]
            cubo[D][1][2] = cubo_actual[D][0][1]
            cubo[D][2][1] = cubo_actual[D][1][2]
            cubo[D][1][0] = cubo_actual[D][2][1]
            cubo[D][0][2] = cubo_actual[D][0][0]
            cubo[D][2][2] = cubo_actual[D][0][2]
            cubo[D][2][0] = cubo_actual[D][2][2]
            cubo[D][0][0] = cubo_actual[D][2][0]
            cubo[B][2][0] = cubo_actual[R][2][0]
            cubo[R][2][0] = cubo_actual[F][2][0]
            cubo[F][2][0] = cubo_actual[L][2][0]
            cubo[L][2][0] = cubo_actual[B][2][0]
            cubo[B][2][1] = cubo_actual[R][2][1]
            cubo[R][2][1] = cubo_actual[F][2][1]
            cubo[F][2][1] = cubo_actual[L][2][1]
            cubo[L][2][1] = cubo_actual[B][2][1]
            cubo[B][2][2] = cubo_actual[R][2][2]
            cubo[R][2][2] = cubo_actual[F][2][2]
            cubo[F][2][2] = cubo_actual[L][2][2]
            cubo[L][2][2] = cubo_actual[B][2][2]
        elif(secuencia_movimiento[i] == 9):
            #algoritmo += "D' -"
            cubo[D][1][0] = cubo_actual[D][0][1]
            cubo[D][0][1] = cubo_actual[D][1][2]
            cubo[D][1][2] = cubo_actual[D][2][1]
            cubo[D][2][1] = cubo_actual[D][1][0]
            cubo[D][0][0] = cubo_actual[D][0][2]
            cubo[D][0][2] = cubo_actual[D][2][2]
            cubo[D][2][2] = cubo_actual[D][2][0]
            cubo[D][2][0] = cubo_actual[D][0][0]
            cubo[R][2][0] = cubo_actual[B][2][0]
            cubo[F][2][0] = cubo_actual[R][2][0]
            cubo[L][2][0] = cubo_actual[F][2][0]
            cubo[B][2][0] = cubo_actual[L][2][0]
            cubo[R][2][1] = cubo_actual[B][2][1]
            cubo[F][2][1] = cubo_actual[R][2][1]
            cubo[L][2][1] = cubo_actual[F][2][1]
            cubo[B][2][1] = cubo_actual[L][2][1]
            cubo[R][2][2] = cubo_actual[B][2][2]
            cubo[F][2][2] = cubo_actual[R][2][2]
            cubo[L][2][2] = cubo_actual[F][2][2]
            cubo[B][2][2] = cubo_actual[L][2][2]
        elif(secuencia_movimiento[i] == 10):
            #algoritmo += "B -"
            cubo[B][0][1] = cubo_actual[B][1][0]
            cubo[B][1][2] = cubo_actual[B][0][1]
            cubo[B][2][1] = cubo_actual[B][1][2]
            cubo[B][1][0] = cubo_actual[B][2][1]
            cubo[B][0][2] = cubo_actual[B][0][0]
            cubo[B][2][2] = cubo_actual[B][0][2]
            cubo[B][2][0] = cubo_actual[B][2][2]
            cubo[B][0][0] = cubo_actual[B][2][0]
            cubo[R][0][2] = cubo_actual[D][2][2]
            cubo[U][0][0] = cubo_actual[R][0][2]
            cubo[L][2][0] = cubo_actual[U][0][0]
            cubo[D][2][2] = cubo_actual[L][2][0]
            cubo[R][1][2] = cubo_actual[D][2][1]
            cubo[U][0][1] = cubo_actual[R][1][2]
            cubo[L][1][0] = cubo_actual[U][0][1]
            cubo[D][2][1] = cubo_actual[L][1][0]
            cubo[R][2][2] = cubo_actual[D][2][0]
            cubo[U][0][2] = cubo_actual[R][2][2]
            cubo[L][0][0] = cubo_actual[U][0][2]
            cubo[D][2][0] = cubo_actual[L][0][0]
        elif(secuencia_movimiento[i] == 11):
            #algoritmo += "B' -"
            cubo[B][1][0] = cubo_actual[B][0][1]
            cubo[B][0][1] = cubo_actual[B][1][2]
            cubo[B][1][2] = cubo_actual[B][2][1]
            cubo[B][2][1] = cubo_actual[B][1][0]
            cubo[B][0][0] = cubo_actual[B][0][2]
            cubo[B][0][2] = cubo_actual[B][2][2]
            cubo[B][2][2] = cubo_actual[B][2][0]
            cubo[B][2][0] = cubo_actual[B][0][0]
            cubo[D][2][2] = cubo_actual[R][0][2]
            cubo[R][0][2] = cubo_actual[U][0][0]
            cubo[U][0][0] = cubo_actual[L][2][0]
            cubo[L][2][0] = cubo_actual[D][2][2]
            cubo[D][2][1] = cubo_actual[R][1][2]
            cubo[R][1][2] = cubo_actual[U][0][1]
            cubo[U][0][1] = cubo_actual[L][1][0]
            cubo[L][1][0] = cubo_actual[D][2][1]
            cubo[D][2][0] = cubo_actual[R][2][2]
            cubo[R][2][2] = cubo_actual[U][0][2]
            cubo[U][0][2] = cubo_actual[L][0][0]
            cubo[L][0][0] = cubo_actual[D][2][0]
        elif(secuencia_movimiento[i] == 12):
            cubo_actual = copy.deepcopy(cubo)
        else:
            print("ERROR")
        
    total.append(copy.deepcopy(cubo))
datos = ''   
for l in range(len(total)):
    for i in range(len(total[0])):
        for j in range(len(total[0][0])):
            for k in range(len(total[0][0][0])):   
                if((i == 5) and (j == 2) and (k == 2)):
                    datos += (str(total[l][i][j][k])+'\n')
                else:
                    datos += (str(total[l][i][j][k])+',')

archivo = open('datos_buenos.csv','a')
archivo.write(datos)
archivo.close()
tiempo_fin = time.time()

tiempo_transcurrido = tiempo_fin - tiempo_inicio
tiempo_transcurrido_segundos = round(tiempo_transcurrido, 2)
print(tiempo_transcurrido_segundos)  
    
    
    
    
    
    
    
    
    