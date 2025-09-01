nombre = input('¿Cuál es tu nombre? ')
edad = int(input('¿Cuál es tu edad? '))
lenguaje = input('¿Qué lenguaje de programación estás estudiando? ')

print(f'Hola {nombre} tienes {edad} años y estás aprendiendo {lenguaje}')

print(f'¿Te gusta estudiar {lenguaje}?')

while True:

    opcion=input('Responde con el número 1 para SÍ o 2 para NO: ')

    if opcion == '1':
        print('¡Muy bien! Sigue estudiando y tendrás mucho éxito')
        break
    elif opcion == '2':
        print('Oh, qué pena... ¿Ya intentaste aprender otros lenguajes?')
        break
    else:
        print('Respuesta invalida.')
        
        