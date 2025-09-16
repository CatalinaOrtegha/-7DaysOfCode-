categorias = {
    "frutas": ['banana', 'fresa', 'mora', 'manzana', 'pera', 'uva', 'piña', 'limón', 'naranja', 'sandia'],
    "verduras": ['zanahoria', 'lechuga', 'tomate', 'pepino', 'espinaca'],
    "lacteos": ['leche', 'queso', 'yogur',],
    "congelados": ['pollo', 'carne', 'pescado','jamon'],
    "dulce": ['chocolate', 'galletas', 'helado'],
    "granos": ['arroz', 'frijoles', 'lentejas']
}

lista_compras = {categoria: [] for categoria in categorias}

while True:
    pregunta = input('¿Deseas agregar un alimento a tu lista de compras? (si/no)').lower()

    if pregunta == 'si':
        alimento = input('Indica el nombre del alimento: ').lower()
        
        encontrado = False
        for categoria, alimentos in categorias.items():
            if alimento in alimentos:
                lista_compras[categoria].append(alimento)
                print(f'{alimento} agregado a {categoria}. ¡Genial!')
                encontrado = True
                break

        if not encontrado:  # Aquí se ejecuta la búsqueda de categoría solo después de que el bucle haya terminado
            print(f'El alimento "{alimento}" no está en las categorías registradas.')
            print('Categorías disponibles:')
            for cat in categorias.keys():
                print(f'- {cat.capitalize()}')
            
            nueva_categoria = input('Ingresa la categoría a la que pertenece (o escribe "salir" para no agregarlo): ').lower()
            
            if nueva_categoria in categorias:
                # Si la categoría existe, agrega el alimento a las categorías y a la lista de compras
                categorias[nueva_categoria].append(alimento)
                lista_compras[nueva_categoria].append(alimento)
                print(f'{alimento} agregado a {nueva_categoria} y a la lista de compras. ¡Listo!')
            else:
                print('Categoría no válida. El alimento no se agregó.')
    
    elif pregunta == 'no':
        print('\n--- Fin de la lista de compras ---')
        for categoria, alimentos in lista_compras.items():
            if alimentos:
                print(f'- {categoria.capitalize()}: {', '.join(alimentos)}')
        break
    else:
        print('Por favor, responde "si" o "no".')