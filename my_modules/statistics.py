def media (list):
    return sum(list) / len(list)

def mediana(list):
    #Ordenamos lista y declaramos variable mid que almacena la mitad de la lista, si es par, la media de posiciones en el
    #centro, si es impar, devolvemos la posicion en el medio
    sorted_numbers = sorted(list)
    mid = len(list) // 2
    if len(list) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]