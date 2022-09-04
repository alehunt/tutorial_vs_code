def buscar_fruta(cajon_frutas, nombre_fruta):
    encontrada = False
    indice = 0
    while not encontrada and indice < len(cajon_frutas):
        if cajon_frutas[indice] == nombre_fruta:
            print(f"Encontré la fruta {nombre_fruta}, en la posición {indice}")
            encontrada = True
        indice += 1
    
    if not encontrada:
        print(f"No encontré la fruta {nombre_fruta} en el cajon de {len(cajon_frutas)} frutas")

def mostrar_frutas(cajon_frutas):
    print(f"El cajon de frutas tiene {len(cajon_frutas)} frutas y son: ")
    for indice, variable_que_guarda_dato in enumerate(cajon_frutas):
        print(f"{indice} - {variable_que_guarda_dato}")
        

cajon_frutas = ["manzana", "banana", "nabo", "pera", "sandia"]
buscar_fruta(cajon_frutas, "pera")
buscar_fruta(cajon_frutas, "Melón")
mostrar_frutas(cajon_frutas)
