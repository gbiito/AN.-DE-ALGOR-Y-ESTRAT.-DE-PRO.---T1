import random

def crearEntrenador(lista):
    print("\n--- CREAR ENTRENADOR Y POKEMON ---")
    entrenador = input("Ingrese el nombre del entrenador: ").strip()
    pokemon = input("Ingrese el nombre del pokemon: ").strip()
    
    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)
    
    entrenador_dupla = (entrenador, pokemon, ataque, vida)
    lista.append(entrenador_dupla)
    
    print(f"¡Entrenador {entrenador} y Pokemon {pokemon} creados exitosamente!")
    print(f"Stats -> Ataque: {ataque} | Vida: {vida}")

def listaEntrenador(lista):
    print("\n--- LISTA DE ENTRENADORES Y POKEMONES (Ordenados por Ataque) ---")
    if not lista:
        print("La lista esta vacia.")
        return

    total_elementos = len(lista)
    for pasada in range(total_elementos):
        for posicion in range(0, total_elementos - pasada - 1):
            if lista[posicion][2] < lista[posicion + 1][2]:
                lista[posicion], lista[posicion + 1] = lista[posicion + 1], lista[posicion]
                
    for correlativo, (entrenador, pokemon, ataque, vida) in enumerate(lista, start=1):
        print(f"{correlativo}. Entrenador: {entrenador} | Pokemon: {pokemon} | Ataque: {ataque} | Vida: {vida}")

def ordenamientoSeleccionPorVida(lista):
    total_elementos = len(lista)
    for indice_actual in range(total_elementos):
        indice_minimo = indice_actual
        for indice_siguiente in range(indice_actual + 1, total_elementos):
            if lista[indice_siguiente][3] < lista[indice_minimo][3]:
                indice_minimo = indice_siguiente
        lista[indice_actual], lista[indice_minimo] = lista[indice_minimo], lista[indice_actual]

def busquedaBinariaPorVida(lista, vida_buscada):
    paso_unidad = len("a")
    posicion_no_encontrada = -paso_unidad
    divisor_mitad = paso_unidad + paso_unidad
    
    limite_inferior = 0
    limite_superior = len(lista) - paso_unidad
    
    while limite_inferior <= limite_superior:
        suma_limites = limite_inferior + limite_superior
        punto_medio = suma_limites // divisor_mitad
        vida_actual = lista[punto_medio][3]
        
        if vida_actual == vida_buscada:
            return punto_medio
        elif vida_actual < vida_buscada:
            limite_inferior = punto_medio + paso_unidad
        else:
            limite_superior = punto_medio - paso_unidad
            
    return posicion_no_encontrada

def borraPorPokemon(lista):
    print("\n--- BORRAR POR VIDA DE POKEMON ---")
    if not lista:
        print("La lista está vacía.")
        return

    try:
        vida_buscada = int(input("Ingrese la cantidad de vida a buscar para eliminar: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return

    ordenamientoSeleccionPorVida(lista)
    indice_encontrado = busquedaBinariaPorVida(lista, vida_buscada)
    
    if indice_encontrado != -1:
        eliminado = lista.pop(indice_encontrado)
        print(f"Se eliminó a {eliminado[0]} con su pokemon {eliminado[1]} (Vida: {eliminado[3]}).")
    else:
        print(f"No se encontró ningún pokemon con vida igual a {vida_buscada}.")

def peleaPokemon(lista):
    print("\n--- PELEA POKEMON ---")
    if len(lista) < 2:
        print("Se necesitan al menos 2 entrenadores para iniciar una pelea.")
        return

    listaEntrenador(lista)
    
    try:
        correlativo_primer_pokemon = int(input("\nIngrese el número correlativo del Primer Pokemon: "))
        correlativo_segundo_pokemon = int(input("Ingrese el número correlativo del Segundo Pokemon: "))
        
        indice_primer_pokemon = correlativo_primer_pokemon - 1
        indice_segundo_pokemon = correlativo_segundo_pokemon - 1
        
        if (indice_primer_pokemon < 0 or indice_primer_pokemon >= len(lista) or 
            indice_segundo_pokemon < 0 or indice_segundo_pokemon >= len(lista)):
            print("Número de pokemon fuera de rango.")
            return
            
        if indice_primer_pokemon == indice_segundo_pokemon:
            print("Debe seleccionar dos pokemones diferentes.")
            return
            
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return

    primer_combatiente = lista[indice_primer_pokemon]
    segundo_combatiente = lista[indice_segundo_pokemon]

    multiplicador_primer_pokemon = random.uniform(0, 5)
    multiplicador_segundo_pokemon = random.uniform(0, 5)

    danio_primer_pokemon = primer_combatiente[2] * multiplicador_primer_pokemon
    danio_segundo_pokemon = segundo_combatiente[2] * multiplicador_segundo_pokemon

    vida_restante_primer_pokemon = primer_combatiente[3] - danio_segundo_pokemon
    vida_restante_segundo_pokemon = segundo_combatiente[3] - danio_primer_pokemon

    print("\n¡COMBATE!")
    print(f"{primer_combatiente[1]} (Entrenador {primer_combatiente[0]}) ataca haciendo {danio_primer_pokemon:.2f} de daño.")
    print(f"{segundo_combatiente[1]} (Entrenador {segundo_combatiente[0]}) ataca haciendo {danio_segundo_pokemon:.2f} de daño.")
    print(f"Vida restante -> {primer_combatiente[1]}: {vida_restante_primer_pokemon:.2f} | {segundo_combatiente[1]}: {vida_restante_segundo_pokemon:.2f}")

    if vida_restante_primer_pokemon > vida_restante_segundo_pokemon and vida_restante_primer_pokemon > 0:
        print(f"\n¡GANADOR: Entrenador {primer_combatiente[0]} y su Pokemon {primer_combatiente[1]}!")
        lista.remove(segundo_combatiente)
    elif vida_restante_segundo_pokemon > vida_restante_primer_pokemon and vida_restante_segundo_pokemon > 0:
        print(f"\n¡GANADOR: Entrenador {segundo_combatiente[0]} y su Pokemon {segundo_combatiente[1]}!")
        lista.remove(primer_combatiente)
    else:
        print("\n¡Ambos pokemones quedaron fuera de combate o empataron! Ambos pierden.")
        lista.remove(primer_combatiente)
        lista.remove(segundo_combatiente)

lista_entrenadores = []

while True:
    print("\n==============================")
    print("       MENÚ POKEMON")
    print("==============================")
    print("1. Crear Entrenador")
    print("2. Listar Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Fin")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    if opcion == "1":
        crearEntrenador(lista_entrenadores)
    elif opcion == "2":
        listaEntrenador(lista_entrenadores)
    elif opcion == "3":
        borraPorPokemon(lista_entrenadores)
    elif opcion == "4":
        peleaPokemon(lista_entrenadores)
    elif opcion == "5":
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción entre 1 y 5.")