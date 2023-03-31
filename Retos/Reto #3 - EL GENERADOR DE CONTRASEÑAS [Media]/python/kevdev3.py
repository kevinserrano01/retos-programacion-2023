"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random

def generar_password(longitud, min, may, num, sim):
    """Genera una contraseña aleatoria con los parámetros especificados."""
    caracteres = ""
    if longitud >=8 and longitud <=16:
        if min:
            caracteres += "abcdefghijklmnopqrstuvwxyz"
        if may:
            caracteres += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if num:
            caracteres += "1234567890"
        if sim:
            caracteres += "ºª!·$%&/()=?¿¡'[]{}#~@¬/*+;:,.<>"

        newPassword = ''
        for i in range(longitud):
            newPassword += random.choice(caracteres) # Devuelve un elemento aleatorio de una lista
        return newPassword
    else:
        print('Error, debes ingresar una cantidad entre 8 y 16 ')


longitud = int(input('Ingresa la cantidad de caracteres entre 8 y 16: '))

num = input('Quieres que incluya números[y/n]: ')
if num == 'y':
    num = True
elif num == 'n':
    num = False
else:
    print('Parámetro no válido.')

may = input('Quieres que incluya mayúsculas[y/n]: ')
if may == 'y':
    may = True
elif may == 'n':
    may = False
else:
    print('Parámetro no válido.')

sim = input('Quieres que incluya símbolos[y/n]: ')
if sim == 'y':
    sim = True
elif sim == 'n':
    sim = False
else:
    print('Parámetro no válido.')

min = True

password = generar_password(longitud, min, may, num, sim)
print(f'*** Contraseña generada***: \n{password}')