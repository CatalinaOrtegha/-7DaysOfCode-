
backend = 'Back-End' 
frontend = 'Front-End'
area_backend1= 'C#'
area_backend2= 'JAVA'
area_fronted1= 'REACT'
area_fronted2= 'VUE'

while True:
    area = input(f'¿Qué area te gustaría seguir? ({backend} o {frontend}): ')

    if area == backend:
        input(f'¿Te gustaría aprender {area_backend1} o {area_backend2}?: ')
        break
    elif area == frontend:
        input(f'¿Te gustaría aprender {area_fronted1} o {area_fronted2}?: ')
        break
    else:
        print('Respuesta invalida, vuelve a intentarlo.')

especializacion = 'Especializacion'
fullstack = 'Fullstack'
elección = input(f'¿Quieres seguir una {especializacion}  o convertirte en {fullstack}: ')

print (f'Quieres seguir en {elección}')

tecnologias=[]

tecnologia=input('En qué tecnología te gustaría especializarte o aprender? ' )
tecnologias.append(tecnologia)

print(f'¡Excelente elección! {tecnologia} es muy interesante.')

while True:
    continuar = input('¿Hay alguna otra tecnología que te gustaría aprender? '
                    '(ok para continuar / no para terminar)').lower()
    
    if continuar == 'ok':
        nuevatec= input("Escribe el nombre de la tecnología: ")
        tecnologias.append(nuevatec)
        print(f'¡Genial! {nuevatec} es una gran opción para tu crecimiento.')

    else:
        print('"Gracias por compartir tus intereses en tecnología."')
        break


print(f'\nResumen de tecnologías que quieres aprender: {tecnologias}' )
