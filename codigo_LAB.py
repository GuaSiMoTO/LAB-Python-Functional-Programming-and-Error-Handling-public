# Iteration 1 / Add_the_positives_results
try:
    lista = [1, -4, 7, "Katana", -2, -7, 10, -1, "shuriken"]
    suma_positivos = sum(filter(lambda x:  isinstance(x, int) and x >= 0, lista))
    print(suma_positivos)
except:
    print("Algo ha ido mal")


# type(x) in [int] / isinstance(x, int) se puede hacer de estas dos maneras para asegurar que sea un numero entero
    

# Iteration 2.1 / Count_the_color

rom functools import reduce

def contar_color(lista):
    try:
        # pregunto el color a buscar en la lista
        color_buscar = input("Que color quieres buscar?: ").lower().strip()
    
        
        # si esta vacio!
        if not isinstance(color_buscar, str):
            raise ValueError("no puede estar vacio")
        
        # si el color no esta
        if color_buscar not in lista:
            raise ValueError (f'color {color_buscar} no esta en la lista')
        
        # aqui creamos una lsita con los colores repetidos
        contar_color = list(filter(lambda x: x == color_buscar, lista))
        
        # aqui contamos cuantos elemento hay en la lista
        cantidad = reduce(lambda ct, _: ct + 1, contar_color, 0)

        print(f"El color {color_buscar} aparece {cantidad} veces.")
    
    except ValueError as e:
        print(f"Error: {e}")

color_lista_de_colores = ["red", "blue", "red", "white", "green", "black", "orange", "black", "red"]
contar_color(color_lista_de_colores)