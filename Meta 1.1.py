#ALANIS MONTSERRAT RODRIGUEZ ALARCON, 951, 20-08-2023

#Ejercicio 1.Duplicados
numeros=[1,2,3,10,6,7,7,8]

def duplicado(numeros):
    if len(numeros) == len(set(numeros)):
        return False
    else:
        return True
print("La lista de numeros es:", duplicado(numeros))

#En este codigo imprime false si los numeros son diferentes y true si alguno se repite.

#Ejercicio 2. Suma de dos números

def suma(nums, target):
    numindi = {}

    for index, num in enumerate(nums):
        com = target - num

        if com in numindi:
            return (numindi[com], index)

        numindi[num] = index
    return None

nums = [2, 7, 11, 15]
target = 9
indi = suma(nums, target)
if indi is not None:
    print(f"Los índices de los números que suman {target} son: {indi}")
else:
    print("No solucion.")

# Este ejercicio presenta una lista de números que retorna una lista de los que sumados den el resultado

#Ejercicio 3. Encriptar
abc = "abcdefghijklmnopqrstuvwxyz"
encript = "ixmrklstnuzbowfaqejdcpvhyg"
codigo = "hrpcm"

def encriptar(encript,codigo):
    abc= "abcdefghijklmnopqrstuvwxyz"
    res=""
    for i in codigo:
        ind=abc.index(i)
        res=res+encript[ind]
    return res
print("La contraseña es:", encriptar(encript,codigo))

#En este codigo incripta un mensaje oculto retornando una contrasena.


#Ejercicio 4. Desencriptar
abc = "abcdefghijklmnopqrstuvwxyz"
encript = "ixmrklstnuzbowfaqejdcpvhyg"
codigo = "hrpcm"

def encriptar(encript,codigo):
    abc= "abcdefghijklmnopqrstuvwxyz"
    res=""
    for i in codigo:
        ind=encript.index(i)
        res=res+abc[ind]
    return res
print("El mensaje oculto es:", encriptar(encript,codigo))

#En este ejercicio da como respuesta el codigo incriptado del anterior problema.

#Ejercicio 5. Gestion de pensionistas
class Pensionista:
    def __init__(self, identificador, nombre, edad, gastos_mensuales):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales

class GrupoPensionistas:
    def __init__(self, pens):
        self.pens = pens

    def mediaGast(self, identificador):
        for pension in self.pens:
            if pension.identificador == identificador:
                return sum(pension.gastos_mensuales) / len(pension.gastos_mensuales)
        return None

    def mediaAge(self):
        total_edad = sum(p.edad for p in self.pens)
        return total_edad / len(self.pens)

    def edadesExtreme(self):
        min_pen = min(self.pens, key=lambda p: p.edad)
        max_pen = max(self.pens, key=lambda p: p.edad)
        return min_pen, max_pen

    def promsuma(self):
        total_promedio = sum(sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pens)
        return total_promedio

    def mediaMax(self):
        max_media = 0
        max_pen = None

        for pension in self.pens:
            media = sum(pension.gastos_mensuales) / len(pension.gastos_mensuales)
            if media > max_media:
                max_media = media
                max_pen = pension

        return max_media, max_pen.nombre, max_pen.identificador

    def gastprom(self):
        gastos_promedio = [(sum(p.gastos_mensuales) / len(p.gastos_mensuales)) for p in self.pens]
        gastos_promedio.sort()
        return gastos_promedio


pen1 = Pensionista('1111A', 'Carlos', 68, [640, 589, 573])
pen2 = Pensionista('2222A', 'Alanis', 88, [990, 500, 893])
pen3 = Pensionista('3333A', 'Roberto',87, [498, 899, 976])

grupo_pensionistas = GrupoPensionistas([pen1, pen2, pen3])

pensionista_menor, pensionista_mayor = grupo_pensionistas.edadesExtreme()
print("Los pensionistas con las edades extremas:", (pensionista_menor.nombre, pensionista_menor.edad), (pensionista_mayor.nombre, pensionista_mayor.edad))
print("La media de los gastos del pensionista '1111A':", grupo_pensionistas.mediaGast('1111A'))
print("La Media de las edades de los pensionistas son:", grupo_pensionistas.mediaAge())
print("La Suma del promedio de los gastos de los pensionistas:", grupo_pensionistas.promsuma())
print("El mayor promedio de gastos es:", grupo_pensionistas.mediaMax())
print("Los gastos promedio ordenados:", grupo_pensionistas.gastprom())

#En este codigo se tiene la informacion de tres pensionistas y se imprimen diferentes calculos de sus ingresos


#Ejercicio 6. Estadistica basica

import matplotlib.pyplot as plt
from collections import Counter

class Estadistica:
    def __init__(self, nums):
        self.nums = nums

    def numsfrec(self):
        frec = Counter(self.nums)
        return frec

    def moda(self):
        frec = self.numsfrec()
        moda = max(frec, key=frec.get)
        return moda

    def histogr(self):
        frec = self.numsfrec()
        nums = list(frec.keys())
        frec = list(frec.values())

        plt.bar(nums, frec)
        plt.xlabel('Numero')
        plt.ylabel('Frecuencia')
        plt.title('Histograma')
        plt.show()


nums= [6, 3, 5, 3, 3, 3, 3, 7, 5, 5,5, 6, 7, 5]
estadisticas = Estadistica(nums)

frec = estadisticas.numsfrec()
print("La frecuencia es:", frec)

moda = estadisticas.moda()
print("La moda es:", moda)

estadisticas.histogr()

#En este codigo se tiene una clase con numeros donde se imprimen diferentes conjuntos de valores numericos y se presenta de manera grafica las tendencias en un histograma