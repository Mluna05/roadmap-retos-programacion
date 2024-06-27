"""Pilas y Colas"""

#Pilas - Stacks
arg1:list = [1,2,3]
arg1.append(4) #push
print(arg1)
#arg1.pop()
del arg1[len(arg1)-1] #pop
print(arg1)

#Colas - queues
arg2:list = [5,6,7]
arg2.append(8)
print(arg2)
arg2.pop(0)
print(arg2)

"""Extra"""

def web_nav():
    sitios_web:list = []
    actual_web:int = 0
    after_nav:str = ""
    print("Bienvenido al navegador web")
    while True:
        accion:int = int(input("Ingresa una accion: \n1)Sitio Anterior 2)navegar al sitio web  3)Sitio Siguiente 4)Salir"))
        match accion:
            case 1:
                print("\nSitio Anterior:")
                if(actual_web == 0):
                    print("No hay sitio anterior")
                else:
                    after_nav = sitios_web[actual_web] 
                    del sitios_web[actual_web]
                    actual_web = actual_web - 1
                    print(sitios_web[actual_web-1])
            case 2:
                sitio_nuevo = input("\nIngresa el nombre: ")
                sitios_web.append(sitio_nuevo)
                actual_web = len(sitios_web)-1
                print(sitios_web)
            case 3:
                print("\nSitio Siguiente:")
                if(after_nav == sitios_web[actual_web]):
                    print("No hay sitio siguiente")
                else:
                    sitios_web.append(after_nav)
                    actual_web = actual_web + 1
                    print(sitios_web[actual_web])
            case 4:
                print("Hasta Luego!")
                break
            case _:
                print("No es una opcion valida")
        print(f"\nSitio Web Actual: ")
        print(f"{sitios_web[actual_web]}")

web_nav()

def impresora():
    documentos = []
    print("Bienvenido que desea imprimir")
    while True:
        accion = input("Ingresa la accion: \n-Documento -Salir -Imprimir")
        match accion:
            case "Documento":
                doc_name = input("Ingresa El nombre del documento:")
                documentos.append(doc_name)
            case "Salir":
                print("Hasta Luego!")
                break
            case "Imprimir":
                if len(documentos) == 0:
                    print("No hay documentos para imprimir")
                else:
                    print(f"Imprimiendo el documento....{documentos[0]}")
                    del documentos[0]
            case _:
                print("No es una opcion valida")

impresora()