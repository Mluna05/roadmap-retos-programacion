"""Tipos de operadores"""
Ar1 = 2
Ar2 = 4
Ar3 = 5

#Operadores Aritméticos
print (Ar1 + Ar2)
print (Ar1 - Ar3)
print (Ar1 * Ar2)
print (Ar1 / Ar2)
print (Ar1 % Ar2)
print (Ar1 ** Ar3)
print (Ar1 // Ar3)

#Operadores de Comparacion
print (Ar1 > Ar2)
print (Ar1 < Ar2)
print (Ar1 >= Ar2)
print (Ar1 <= Ar2)
print (Ar1 == Ar2)
print (Ar1 != Ar2)

#Operadores de Logicos
print(Ar1 and Ar2)
print(Ar1 or Ar2)
print(not Ar1)

#Operadores de Asignacion
Ar4 = Ar1
print(Ar4)
Ar1 += 2
print(Ar1)
Ar1 -= 2
print(Ar1)
Ar1 *= 2
print(Ar1)
Ar1 /= 2
print(Ar1)
Ar1 %= Ar2
print(Ar1)
Ar1 **= Ar3
print(Ar1)
Ar1 //= Ar2
print(Ar1)

#Operadores de Identidad
print(Ar1 is Ar2)
print(Ar1 is not Ar2)

#Operadores de Pertenencia
Ar5 = [1,2,3,4,5]
print(Ar1 in Ar5)
print(Ar1 not in Ar5)

#Operadores de Bit 
print(Ar4 & Ar2)
print(Ar4 | Ar2)
print(Ar4 ^ Ar2)
print(~Ar4)
print(Ar4 << Ar2)
print(Ar4 >> Ar2)

"""Estructura de Control"""

#Condicionales
nombre = "Mario"

if nombre == "Mario":
    print("si es Mario")
elif nombre == "Mario2":
    print("si es Mario2")
else:
    print("no es Mario")

#Bucles
Ar6 = [1,2,3,4,5]

for i in range(10):
    print(i)

for j in Ar6:
    print(j)

while  Ar2 <= 10:
    print(Ar2)
    Ar2 += 1

#Manejo de Excepciones
try:
    print(Ar1/0)
except:
    print("No se puede dividir por 0")
finally:
    print("Se ejectura siempre al final")


"""Extra"""

for i in range(10,56):
    if (((i%2) == 0) and (i!=16) and ((i%3)!=0)) :
        print(i)

