"""Valor y Referencia"""

#Inmutables = Valor
arg1 = 12
arg2 = 12.3
arg3 = "Hola"
arg4 = (1, 2, 3) #Tupla
arg_Aux = ""

arg_Aux = arg1
arg_Aux = 12
print(arg1)
print(arg_Aux)

arg_Aux = arg2
arg_Aux = 15.123
print(arg2)
print(arg_Aux)

arg_Aux = arg3
arg_Aux = "Mundo"
print(arg3)
print(arg_Aux)

arg_Aux = arg4
arg_Aux = (4, 5, 6)
print(arg3)
print(arg_Aux)

##Mutables = Referencia
arg5 = [1, 2, 3] #Lista
arg6 = {"1": 1, "2": 2} #Diccionario
arg7 = {1, 2, 3} #Conjunto

arg_Aux_5 = arg5
arg_Aux_5.append(4)
print("este es arg5 {}".format(arg5))
print("este es arg_Aux_5 {}".format(arg_Aux_5))

arg_Aux_6 = arg6
arg_Aux_6["3"] = 3
print("este es arg6 {}".format(arg6))
print("este es arg_Aux_6 {}".format(arg_Aux_6))

arg_Aux_7 = arg7
arg_Aux_7.add(4)
print("este es arg7 {}".format(arg7))
print("este es arg_Aux_7 {}".format(arg_Aux_7))

#Funciones con datos por valor

def int_func(my_int):
    my_int = 20
    print(my_int)

int_func(arg1)
print(arg1)

def float_func(my_float):
    my_float = 33.3
    print(my_float)

float_func(arg2)
print(arg2)

def char_func(my_char):
    my_char = "Mundo"
    print(my_char)

char_func(arg3)
print(arg3)

def tupla_func(my_tupla):
    my_tupla = (4, 5, 6)
    print(my_tupla)

tupla_func(arg4)
print(arg4)


#Funciones con datos por referencia

def lista_func(my_lista):
    my_lista.append(5)
    print(my_lista)

lista_func(arg5)
print(arg5)

def diccionario_func(my_diccionario):
    my_diccionario["4"] = 4
    print(my_diccionario)

diccionario_func(arg6)
print(arg6)

def conjunto_func(my_conjunto):
    my_conjunto.add(5)
    print(my_conjunto)

conjunto_func(arg7)
print(arg7)

"""Extra"""

arg_e1 = 10
arg_e2 = (1, "a", "?") #Tupla
arg_e3 = { "a" : 1, "b" : 2, "c" : 3 }
arg_e4 = ["a", "b", "c"]

def pro_valor(arg_p1:int, arg_p2:tuple)->tuple:
    return arg_p2, arg_p1

nuevo_arg_e1, nuevo_arg_e2 = pro_valor(arg_e1, arg_e2)

print("este es arg_e1 {}".format(arg_e1))
print("este es arg_e2 {}".format(arg_e2))
print("este es nuevo_arg_e1 {}".format(nuevo_arg_e1))
print("este es nuevo_arg_e2 {}".format(nuevo_arg_e2))

def pro_referencia(arg_p3:dict, arg_p4:list)->tuple:
    temp = arg_p3
    temp["d"]=4
    arg_p3 = arg_p4
    arg_p3.append("d")
    arg_p4 = temp
    return arg_p3, arg_p4

nuevo_arg_e3, nuevo_arg_e4 = pro_referencia(arg_e3, arg_e4)

print("este es arg_e3 {}".format(arg_e3))
print("este es arg_e4 {}".format(arg_e4))
print("este es nuevo_arg_e1 {}".format(nuevo_arg_e3))
print("este es nuevo_arg_e2 {}".format(nuevo_arg_e4))