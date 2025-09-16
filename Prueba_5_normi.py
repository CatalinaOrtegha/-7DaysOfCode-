frutas=[]
lacteos=[]
dulces=[]
congelados=[]

agregar='si'

while agregar == 'si':
    comida=input('¿Qué comida deseas agregar?')
    categoria=input("¿En qué categoria encaja esta comida: 'frutas', 'lacteos', 'dulces' o 'congelados'?")

    if categoria == 'frutas':
        frutas.append(comida)
    elif categoria == 'lacteos':
        lacteos.append(comida)
    elif categoria == 'dulces':
        dulces.append(comida)
    elif categoria == 'congelados':
        congelados.append(comida)
    else:
        print('¡Esta categoría no está predefinida! Por favor, intenta de nuevo.')

    agregar = input('¿Desea agregar otra comida a la lista de compras? Responde "si" o "no". ')
    while agregar != 'si' and agregar != 'no':
        print('Operación no reconocida. Intenta de nuevo.')
        agregar = input('¿Desea agregar otra comida a la lista de compras? Responde "si" o "no". ')

print(f'Lista de compras:\n Frutas: {frutas}\n Lacteos: {lacteos}\n Dulces: {dulces}\n Congelados: {congelados}')