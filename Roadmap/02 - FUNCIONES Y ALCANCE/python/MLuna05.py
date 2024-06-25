
"""Funciones definidas por el usuario"""

#Funcion Simple

def saludar():
    print("hola visitante!")

saludar()

#Funcion con Retorno

def devuelve_saludo():
    return "Hola de regreso"

saludo_devuelta = devuelve_saludo()
print(saludo_devuelta)

#Funciones con un argumento

def saludo_personalizado(persona):
    return f"Hola este es un saludo personalizado para {persona}"

print(saludo_personalizado("Mario"))

#Funciones con argumentos

def saludo_personalizado_multi(per1, per2, per3):
    return f"Hola este es un saludo personalizado para: {per1}, {per2}, {per3}"

print(saludo_personalizado_multi("Mario", "Juan", "Luis"))

print(saludo_personalizado_multi( per3="Mario", per1="Juan", per2="Luis"))

#Funciones con argumentos predeterminado

def saludo_personalizado(persona="Pedro"):
    return f"Hola este es un saludo personalizado para {persona}"

print(saludo_personalizado())


#Funcion con retorno de multiples valores

def multiple_saludos():
    return "Hola", "Hi"

esp_saludo, eng_saludo = multiple_saludos() 

print(f"{esp_saludo} asi saludamos en español")
print(f"{eng_saludo} asi saludamos en ingles")

#Funciones con numero variable no especifico de argumentos

def saludo_personalizado_multi_n(*names):
    for name in names:
        print(f"Hola! {name}")

saludo_personalizado_multi_n("Mario", "Juan", "Luis")

#Funciones con numero variable no especifico de argumentos pero con palabra clave

def saludo_personalizado_multi_nc(**names):
    for key, name in names.items():
        print(f"Asi se imprima{name} {key}")

saludo_personalizado_multi_nc(apellido="Dallas", name="Mario")

#Funciones dentro de otras funciones

def funcOut(argOut):
    def funcIn(argIn):
        return argIn
    return funcIn(argOut)

print(f"Resultado de una funcion dentro de otra funcion {funcOut('Es posible!!!')}")

#Funciones dentro del lenguaje (Built-In)

arg1=[6,2,1,4,5]
arg2="mLuna05i"

print(len(arg1))
print(type(arg1))
print(arg2.upper())
print(arg2.capitalize())
print(sorted(arg1))
print(min(arg1))
print(max(arg1))
print(list(range(10)))

#Variables Globales y locales

arg3="Global"

def funcion_local():
    arg4="Local"
    print(f"dentro de la funcion accediendo a la variable {arg3}")
    print(f"dentro de la funcion accediendo a la variable {arg4}")

funcion_local()

print(f"Fuera de la funcion accediendo a la variable {arg3}")

try:
    print(f"Fuera de la funcion accediendo a la variable {arg4}")
except:
    print("No se puede llamar a las variable de dentro de la funcion")

"""Extra"""

def imp_1_100(arg_1, arg_2):
    count=0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(arg_1 + str(arg_2))
        elif i % 3 == 0:
            print(arg_2)
        elif i % 5 == 0:
            print(arg_1)
        else:
            print(i)
            count+=1
    return count            
        

def extra_func(arg_1="uno", arg_2=2)->int:
    arg_ex_1=imp_1_100(arg_1,arg_2)
    return arg_ex_1

print(f"Este es el resultado del ejercicio extra {extra_func()}")


