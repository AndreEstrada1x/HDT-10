import networkx as nx

def leer_archivo(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r') as file:
        next(file)
        for line in file:
            ciudad1, ciudad2, tiempo_normal, tiempo_lluvia, tiempo_nieve, tiempo_tormenta = line.strip().split()
            datos.append((ciudad1, ciudad2, float(tiempo_normal), float(tiempo_lluvia), float(tiempo_nieve), float(tiempo_tormenta)))
    return datos

def construir_grafo(datos):
    grafo = nx.DiGraph()
    for dato in datos:
        ciudad1, ciudad2, tiempo_normal, tiempo_lluvia, tiempo_nieve, tiempo_tormenta = dato
        grafo.add_edge(ciudad1, ciudad2, tiempo_normal=tiempo_normal, tiempo_lluvia=tiempo_lluvia, tiempo_nieve=tiempo_nieve, tiempo_tormenta=tiempo_tormenta)
    return grafo

def ruta_mas_corta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return "Las ciudades especificadas no existen en el grafo."

    try:
        shortest_path = nx.shortest_path(grafo, origen, destino, weight='tiempo_normal')
        shortest_time = nx.shortest_path_length(grafo, origen, destino, weight='tiempo_normal')

        if len(shortest_path) > 2:
            intermedias = shortest_path[1:-1]
            return f"La ruta más corta entre {origen} y {destino} es: {' -> '.join(shortest_path)}, tiempo: {shortest_time} horas.\nCiudades intermedias: {', '.join(intermedias)}"
        else:
            return f"La ruta más corta entre {origen} y {destino} es: {' -> '.join(shortest_path)}, tiempo: {shortest_time} horas.\nNo hay ciudades intermedias."
    except nx.NetworkXNoPath:
        return "No hay ruta posible entre las ciudades especificadas."


def ciudad_centro(grafo):
    centros = []
    for componente in nx.weakly_connected_components(grafo):
        componente_grafo = grafo.subgraph(componente)
        try:
            centro_componente = nx.center(componente_grafo)[0]
            centros.append(centro_componente)
        except nx.NetworkXError:
            pass
    return centros

def modificar_grafo(grafo, opcion):
    if opcion == "3":
        print("\nOpciones de modificación:")
        print("a. Hay interrupción de tráfico entre un par de ciudades.")
        print("b. Se establece una conexión entre ciudad1 y ciudad2 (recordar ingresar todos los tiempos).")
        print("c. Se indica el clima (normal, lluvia, nieve o tormenta) entre un par de ciudades.")
        accion = input("Seleccione una opción de modificación (a, b o c): ")

        if accion == "a":
            ciudad1 = input("Ingrese el nombre de la primera ciudad: ")
            ciudad2 = input("Ingrese el nombre de la segunda ciudad: ")
            if grafo.has_edge(ciudad1, ciudad2):
                grafo.remove_edge(ciudad1, ciudad2)
                print(f"Se interrumpió el tráfico entre {ciudad1} y {ciudad2}.")
            else:
                print(f"No hay una conexión entre {ciudad1} y {ciudad2} para interrumpir.")
        elif accion == "b":
            ciudad1 = input("Ingrese el nombre de la primera ciudad: ")
            ciudad2 = input("Ingrese el nombre de la segunda ciudad: ")
            tiempo_normal = float(input("Ingrese el tiempo normal entre las ciudades: "))
            tiempo_lluvia = float(input("Ingrese el tiempo con lluvia entre las ciudades: "))
            tiempo_nieve = float(input("Ingrese el tiempo con nieve entre las ciudades: "))
            tiempo_tormenta = float(input("Ingrese el tiempo con tormenta entre las ciudades: "))
            grafo.add_edge(ciudad1, ciudad2, tiempo_normal=tiempo_normal, tiempo_lluvia=tiempo_lluvia, tiempo_nieve=tiempo_nieve, tiempo_tormenta=tiempo_tormenta)
            print(f"Se estableció una conexión entre {ciudad1} y {ciudad2} en el grafo.")
        elif accion == "c":
            ciudad1 = input("Ingrese el nombre de la primera ciudad: ")
            ciudad2 = input("Ingrese el nombre de la segunda ciudad: ")
            clima = input("Ingrese el tipo de clima (normal, lluvia, nieve o tormenta): ")
            if grafo.has_edge(ciudad1, ciudad2):
                grafo[ciudad1][ciudad2]["clima"] = clima
                print(f"Se indicó que entre {ciudad1} y {ciudad2} hay clima {clima}.")
            else:
                print(f"No hay una conexión entre {ciudad1} y {ciudad2} para indicar clima.")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    archivo = "logistica.txt"
    datos = leer_archivo(archivo)
    grafo = construir_grafo(datos)

    while True:
        print("\nOpciones:")
        print("1. Calcular la ruta más corta entre dos ciudades.")
        print("2. Mostrar la ciudad que queda en el centro del grafo.")
        print("3. Modificar el grafo.")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            origen = input("Ingrese el nombre de la ciudad origen: ")
            destino = input("Ingrese el nombre de la ciudad destino: ")
            print(ruta_mas_corta(grafo, origen, destino))
        elif opcion == "2":
            centros = ciudad_centro(grafo)
            if centros:
                print("La ciudad que queda en el centro del grafo es:", centros[0])
            else:
                print("No se pudo encontrar una ciudad central.")
        elif opcion == "3":
            modificar_grafo(grafo, opcion)
            print("Grafo modificado.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
