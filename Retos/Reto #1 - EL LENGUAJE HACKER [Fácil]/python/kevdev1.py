"""
    Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    se caracteriza por sustituir caracteres alfanuméricos.
    Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""
traductor = {
    'a': '4',
    'b': '6',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '6',
    'h': '|-|',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|_',
    'm': '|\/|',
    'n': '|\|',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': '`/',
    'z': '2',
}

def transformar_Lenguaje_Hacker(texto):
    """Funcion que transforma un texto en lenguaje hacker"""
    palabraTraducida = '' # guardo la palabra nueva ya traducida
    for letra in texto.lower():
        if letra in traductor:
            palabraTraducida += traductor[letra]
        else:
            palabraTraducida += letra
    return palabraTraducida

texto = input('Ingrese una palabra: ')
print(transformar_Lenguaje_Hacker(texto))