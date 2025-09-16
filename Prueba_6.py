categorias = {
    "frutas": ['banana','fresa','mora','manzana','pera','uva','piña','limón','naranja','sandia'],
    "verduras": ['zanahoria','lechuga','tomate','pepino','espinaca'],
    "lacteos":['leche','queso','yogur'],
    "congelados":['pollo','carne','pescado','jamon'],
    "dulce": ['chocolate','galletas','helado'],
    "granos":['arroz','frijoles','lentejas'],
}

lista_compras= {categoria: [] for categoria in categorias}

while True:
    pregunta = input('¿Deseas agregar un alimento a tu lista de compras? (si/no)').lower()

    if pregunta =='si':
        alimento = input('Indica el nombre del alimento: ').lower()

        encontrado = False
        for categoria, alimentos in categorias.items():
            if alimento in alimentos:
                lista_compras[categoria].append(alimento)
                print(f'{alimento} agregado a {categoria}. ¡Genial!')
                encontrado = True
                break
        
        if not encontrado:
            print(f'El alimento "{alimento}" no está en las categorías registradas. ')
            print('Categorías disponibles:')
            for cat in categorias.keys():
                print(f' - {cat.capitalize()}')

        nueva_categoría = input('Ingresa la categoría a la que pertenece (o escribe "salir" para no agregarlo): ').lower()

        if nueva_categoría in categorias:
            categorias[nueva_categoría].append(alimento)
            lista_compras[nueva_categoría].append(alimento)
            print(f'{alimento} agregado a {nueva_categoría} y a la lista de compras. ¡Listo!')
        else:
            print('Categoría no válida, El alimento no se agregó.')

    elif pregunta == 'no':
        print('\n --- Fin de la lista de compras ---')
        for categoria, alimentos in lista_compras.items():
            if alimentos:
                print(f' - {categoria.capitalize()}: {', '.join(alimentos)}')
        break
    else:
        print('Por favor, responde "si" o "no".')

    deshacer= input('¿Deseas eliminar un item de la lista? (si/no): ' ).lower()

    if deshacer == 'si':
        item_a_eliminar= input('Introduce el alimento a eliminar: ').lower()
        item_encontrado= False

        for categoria, alimentos_en_lista in lista_compras.items():
            if item_a_eliminar in alimentos_en_lista:
                alimentos_en_lista.remove(item_a_eliminar)
                print(f'{item_a_eliminar} eliminado de la lista de {categoria}')
                item_encontrado=True
                break

        if not item_encontrado:
            print('El alimento no se encontró en tu lista de compras ---')
           
    elif pregunta == 'no':
        print('\n--- Fin de la lista de compras ---')
        for categoria, alimentos in lista_compras.items():
            if alimentos:
                print(f' - {categoria.capitalize() } : {', '.join(alimentos)}')
        break
    else:
        print('Por favor, responde "si" o "no". ' )
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