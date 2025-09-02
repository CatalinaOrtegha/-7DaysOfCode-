import random

numero = random.randint(0,10)
intentos = 3

print('Adivina el número entre 0 y 10')
print(f'Tienes {intentos} intentos.')

for i in range(intentos):

    adivina = int(input("Ingresa el número: "))

    if adivina == numero:
        print('¡Adivinaste el número!')
        break
    else:
        if i < intentos -1: #Todavía quedan intentos
            if adivina < numero:
                print('El número secreto es mayor')
            else:
                print('El número secreto es  menor')
            print(f'Te quedan {intentos-(i+1)} intentos')
        
        else:
            print(f'❌ Usaste todos los intentos. El número era {numero}.')