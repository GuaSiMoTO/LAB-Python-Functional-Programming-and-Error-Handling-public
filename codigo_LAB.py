# Iteration 1 / Add_the_positives_results
try:
    lista = [1, -4, 7, "Katana", -2, -7, 10, -1, "shuriken"]
    suma_positivos = sum(filter(lambda x:  isinstance(x, int) and x >= 0, lista))
    # type(x) in [int] / isinstance(x, int) se puede hacer de estas dos maneras para asegurar que sea un numero entero  
    print(suma_positivos)
except:
    print("Algo ha ido mal")




# Iteration 2.1 / Count_the_color

from functools import reduce

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

# Iteration 2.2 / Count_the_color_multidimensional
from functools import reduce

lista_colores = [
    ["red", "blue", "red", "white"],
    ["yellow", "red", "blue", "green"],
    ["white", "red", "blue", "yellow"],
    ["green", "black", "orange", "orange"]
]

# Pedir al usuario el color a buscar
color_buscar = input("Que color quieres buscar?: ").strip().lower()

# Aplanar la lista multidimensional (convertirla en 1D)
lista_plana = reduce(lambda ct, sublista: ct + sublista, lista_colores, [])

# Filtrar solo los colores que coincidan
colores_filtrados = list(filter(lambda color: color == color_buscar, lista_plana))

# Contar ocurrencias con reduce
cantidad = reduce(lambda ct, _: ct + 1, colores_filtrados, 0)

print(f"El color '{color_buscar}' aparece {cantidad} veces.")

# Iteration 3 / strings_order

misiones = [
    "Rescue", "Infiltrate", "Guard", "Retrieve", 
    "Investigate", "Defend", "Escort", "Patrol", 
    "Eliminate", "Capture"
]

# Ordenar usando sorted + lambda (de menor a mayor longitud)
misiones_ordenadas = sorted(misiones, key=lambda x: len(x))

""" para cambiar el orden (de mayor a menor longitud) (reverse=True) o (-len(x0)), ejemplos:
- misiones_ordenadas = sorted(misiones, key=lambda x: len(x), reverse=True)
- misiones_ordenadas = sorted(misiones, key=lambda x: -len(x))
"""
print(misiones_ordenadas)

# Iteration 4 / Calculate Total Strength

from functools import reduce

ninjas = [
    {'name': 'Naruto', 'strength': 9000},
    {'name': 'Sasuke', 'strength': 8500},
    {'name': 'Sakura', 'strength': 'high'},
    {'name': 'Kakashi', 'strength': 9500},
    {'name': 'Rock Lee', 'strength': 8000},
    {'name': 'Hinata', 'strength': 'unknown'}
]

# aqui valido si la fuerza es numerico (int) o str
def validar_fuerza(ninja):
    try:
        return isinstance(ninja['strength'], int) # podemos usar type(ninja['strength']) == int
    except KeyError:
        return False
    
# si la funcion validar_fuerza devuelve False entonces mantiene ct sin sumarle ninja['strength'] en lo contrario suma el valor a ct (acumulador)   
total_strength = reduce(
    lambda ct, ninja: ct + ninja['strength'] if validar_fuerza(ninja) else ct, 
    ninjas, 0  # Le damos a ct = 0 de primera
)

print(total_strength)

# Iteration 5 / Calculate who are the strongest

from functools import reduce

def filtrar_ninja_por_fuerza(ninjas, fuerza):
    try:
        # Verifica si la fuerza es numerico(int) o es str, si es str da un ERROR
        if not isinstance(fuerza, int):
            raise ValueError("La Fuerza debe ser numerico")
        
        # Filtra ninjas con fuerza >= 8000 que introduzco como argumento como fuerza
        # y que ninja['strength'] sea int porque sino da error al comparar str con int
        ninjas_filtrados = list(
            filter(lambda ninja: isinstance(ninja['strength'], int)  and ninja['strength'] >= fuerza, ninjas) 
        ) 
        
        return ninjas_filtrados
    
    except ValueError as e:
        return f"Error: {e}"
    
ninjas = [
    {'name': 'Naruto', 'strength': 9000},
    {'name': 'Sasuke', 'strength': 8500},
    {'name': 'Sakura', 'strength': 'high'},
    {'name': 'Kakashi', 'strength': 9500},
    {'name': 'Rock Lee', 'strength': 8000},
    {'name': 'Hinata', 'strength': 'unknown'}
]

# aquí enseñara a todos los que tenga >= 8000 de fuerza al pasarlo como argumento a la funcion
print(filtrar_ninja_por_fuerza(ninjas, 8000))

# aqui debe dar el error de que le paso fuerza como un str
print(filtrar_ninja_por_fuerza(ninjas, 'high'))

# Iteration 6 / Get the Ninja Names

ninjas = [
    {'name': 'Naruto', 'strength': 9000},
    {'name': 'Sasuke', 'strength': 8500},
    {'name': 'Sakura', 'strength': 'high'},
    {'name': 'Kakashi', 'strength': 9500},
    {'name': 'Rock Lee', 'strength': 8000},
    {'name': 'Hinata', 'strength': 'unknown'}
]

ninja_nombres_mayusculas = list(map(lambda personaje: personaje['name'].upper(), ninjas))

print(ninja_nombres_mayusculas)

# BONUS - get_best_students

	# opción sin usar filter + map (Funcional)

def mejores_estudiantes(students):
    mejores_estudiantes = []
    
    # aqui itero por cada linea de students
    for estudiante in students: 
        notas = estudiante["subjectsMarks"] # cojo las notas
        promedio = sum(notas) / len(notas)
        
        # aqui si el promedio es mayor o igual lo meno en la lista mejores_studiantes, su emial y el promedio
        if promedio >= 9:
            mejores_estudiantes.append({
                "email": estudiante["email"],
                "average": round(promedio, 1)
            })
    
    # Ordenar por promedio (de mayor a menor)
    mejores_estudiantes.sort(key=lambda x: x["average"], reverse=True)
    
    return mejores_estudiantes

students = [
    {"name": "Naruto", "subjectsMarks": [9, 8, 10, 5, 10], "email": "naruto@konoha.com"},
    {"name": "Sasuke", "subjectsMarks": [9, 8, 10, 9, 10], "email": "sasuke@konoha.com"},
    {"name": "Sakura", "subjectsMarks": [9, 10, 10, 9, 10], "email": "sakura@konoha.com"},
    {"name": "Shikamaru", "subjectsMarks": [8, 8, 7, 6, 8], "email": "shikamaru@konoha.com"}
]

print(mejores_estudiantes(students))

	# ahora con filter 

def mejores_estudiantes(students):
    # filtramos estudiantes con promedio >= 9 y calculamos promedio
    students_with_avg = []

    for student in students:
        promedio = sum(student["subjectsMarks"]) / len(student["subjectsMarks"])
        if promedio >= 9:
            students_with_avg.append({
                "email": student["email"],
                "average": round(promedio, 1)  # aquí creamos la llave "average"
            })
           
    # ordenar por promedio (de mayor a menor)
    estudiantes_sorted = sorted(
        students_with_avg,
        key=lambda x: x["average"],
        reverse=True
    )
    
    return estudiantes_sorted

students = [
    {"name": "Naruto", "subjectsMarks": [9, 8, 10, 5, 10], "email": "naruto@konoha.com"},
    {"name": "Sasuke", "subjectsMarks": [9, 8, 10, 9, 10], "email": "sasuke@konoha.com"},
    {"name": "Sakura", "subjectsMarks": [9, 10, 10, 9, 10], "email": "sakura@konoha.com"},
    {"name": "Shikamaru", "subjectsMarks": [8, 8, 7, 6, 8], "email": "shikamaru@konoha.com"}
]

print(mejores_estudiantes(students))
