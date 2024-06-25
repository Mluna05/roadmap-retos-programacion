import os
import platform

"""Estructuras de datos"""

#Listas
mi_lista:list=[1,2,3,"uno","dos","tres"]

##Metodos
###Append:
mi_lista.append("cuatro")
print(f"se inserto el 'cuatro' a la lista con append y quedo asi :{mi_lista}")

###Insert
mi_lista.insert(0,"cinco")
print(f"se inserto el 'cinco' a la lista con append y quedo asi :{mi_lista}")

###Sort
mi_lista2=[1,2,3]
mi_lista2.sort(reverse=True)
print(f"se ordeno con sort lo elementos de lista :{mi_lista2} se modifica el arreglo original")

###Sorted
mi_lista3=[6,1,3,4]
lista_nueva_ordenada=sorted(mi_lista2)
print(f"se ordeno con sorted lo elementos de lista :{lista_nueva_ordenada} se creo un arreglo nuevo")

###Del
del mi_lista[1]
print(f"se borro elemento 1 a la lista con del y quedo asi :{mi_lista}")

###Remove
mi_lista.remove(3)
print(f"se inserto el 'cinco' a la lista con append y quedo asi :{mi_lista}")

###Clear
mi_lista.clear()
print(f"se borro la lista con clear y quedo asi :{mi_lista}")

#Tupla
mi_tupla:tuple=("3","2","1","tres","dos","uno")

##Metodos 
###Count e Index
print(mi_tupla.count(4))
print(mi_tupla.index("2"))

###sorted
mi_tupla=tuple(sorted(mi_tupla))
print(f"se puede ordenar una tupla casteandola con ella misma y guardandola en ella misma {mi_tupla}")

#Conjuntos
mi_conjunto={1,2,3}
print(f"esta es un conjunto todos los elementos son unicos {mi_conjunto}")

###Add
mi_conjunto.add(4)
print(f"esta es un conjunto se agrego con add el 4 en {mi_conjunto}")

###Remove
mi_conjunto.remove(1)
print(f"esta es un conjunto se elimino el numero 1 en {mi_conjunto}")

#Diccionario
mi_diccionario={"key1":"1", "key2":"2"}
print(mi_diccionario["key1"])

##Agregar datos al diccionario
mi_diccionario["key3"]="3"
print(f"se agrego un nuevo valor la diccionario es este: {mi_diccionario}")

##Eliminar datos al diccionario
del mi_diccionario["key1"]
print(f"se elimino el key1 del diccionario: {mi_diccionario}")


"""Extra"""

directorio={}

def ask_info(accion):
    print(f"\nSeccion: {accion}")
    nom = input(f"\n Ingresa el nombre del contacto: ")
    return nom

def accion_agregar(nombre, numero):
    directorio[nombre]=numero

def accion_eliminar(nombre):
    if nombre not in directorio:
        print(f"el nombre {nombre} no esta en la agenda")
    else:
        del directorio[nombre]
    
def accion_actualizar(nombre,numero):
    if nombre not in directorio:
        print(f"el nombre {nombre} no esta en la agenda")
    else:
        directorio[nombre]=numero
        print(f"El numero de {nombre} ha sido actualizado")

def accion_buscar(nombre):
    if nombre not in directorio:
        print(f"el nombre {nombre} no esta en la agenda")
    else:
        print(f"El numero de {nombre} es {directorio[nombre]} ")

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def valida_numero():
    while True:
        try:
            numero = int(input("Ingresa un numero: "))
            if len(str(abs(numero))) >= 11:
                break
            else:
                print("Ingresa un número con mas de 11 caracteres\n")
                continue
        except ValueError:
            print("Ingresa un numero que no contenga caracteres\n")
            continue
    return numero

def agenda():
    while True:    
        accion=int(input("Que accion quieres realizar: 1)Agregar, 2)Eliminar, 3)Actualizar, 4)Busqueda 5)Salir "))
        match accion:
            case 1:
                nombre = ask_info("Agregar")
                numero = valida_numero()
                accion_agregar(nombre, numero)
            case 2:
                nombre = ask_info("Eliminar")
                accion_eliminar(nombre)
            case 3:
                nombre = ask_info("Actualizar")
                numero = valida_numero()
                accion_actualizar(nombre, numero)
            case 4:
                nombre = ask_info("Buscar")
                accion_buscar(nombre)
            case 5:
                print("Hasta Luego!")
                break
            case _:
                print("No es una opcion valida")

agenda()