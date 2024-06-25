# Cadena de Caracteres
arg1 = "simon"
arg2 = "mario"
arg3 = "12345"
arg4 = "1234abc"

## Acceso a caracteres específicos
print(arg1[4])

## Subcadenas
arg1_sub = arg1[0:2]
print(arg1_sub)

## Longitud
print(len(arg1))

## Concatenación
print(arg1 + " " + arg2)

## Repetición
print(arg1 * 3)

## Recorrido
for letra in arg1:
    print(letra)

## Mayúsculas
print(arg1.upper())

## Minúsculas
print(arg1.lower())

## Reemplazo
print(arg1.replace("i", "al"))

## División
print(arg1.split("m"))

## Unión
print(" ".join(arg1.split("m")))

## Interpolación
print("Hola %s %s" % ("mario", "luna"))

## Verificación
print("mario" in arg2)
print("mario" not in arg1)
if arg4.isalnum():
    print(f"arg4  solo tiene letras o dígitos son: {arg4}")
if arg3.isdigit():
    print(f"arg3 solo tiene numeros son: {arg3}")
if arg2.isalpha():
    print(f"arg2 solo tiene letras son: {arg2}")

## Extra   

def palindromo_detector():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    if palabra1[::-1] == palabra2:
        print(f"Las palabras son palindromos y la palabra fue : {palabra1}")
    else:
        print(f"Las palabras {palabra1} y {palabra2} no son palindromos")

palindromo_detector()

def anagrama_detector():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    palabra1_mod = (palabra1).replace(" ", "").lower()
    palabra2_mod = (palabra2).replace(" ", "").lower()
    if len(palabra1_mod) == len(palabra2_mod) and sorted(palabra1_mod) == sorted(palabra2_mod):
        print(f"Las palabras son Anagramas y las palabra fueron : \n{palabra1} \n{palabra2}")
    else:
        print(f"Las palabras {palabra1} y {palabra2} no son Anagramas")

anagrama_detector()

def isograma_check(palabra_mod):
    isograma = set()
    for letra in palabra_mod:
        if letra not in isograma:
            isograma.add(letra)
            return True
        else:
            return False

def isograma_detector():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    palabra1_mod = (palabra1).replace(" ", "").lower()
    palabra2_mod = (palabra2).replace(" ", "").lower()
    if isograma_check(palabra1_mod):
        print(f"La palabra {palabra1} es un isograma")
    else:
        print(f"La palabra {palabra1} no es un isograma")

    if isograma_check(palabra2_mod):
        print(f"La palabra {palabra2} es un isograma")
    else:
        print(f"La palabra {palabra2} no es un isograma")

isograma_detector()