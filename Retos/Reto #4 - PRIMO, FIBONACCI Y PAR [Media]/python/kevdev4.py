"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

numero es primo cuando: Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero. Dicho de otra forma, si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.

numero es fibonacci: Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores, de manera que: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

par: Un número es par si es múltiplo de dos. 
"""
def es_primo(num: int):
    """Determina si un numero es primno o no"""
    if num < 2: # 2 es el primer numero primo
        return False
    else:
        for i in range(2,num): # verifico si es divisible por algún número entre 2 y el numero ingresado.
            if num % i == 0: # (num/i el resto no es un entero)Si el número es divisible por algún número en este rango, entonces no es primo.
                return False
        return True # Si el número no es divisible por ningún número en este rango, entonces es primo.

def es_fibonacci(num: int):
    """Determina si un número es un número de Fibonacci o no."""
    if num == 0 or num == 1: # Casos especiales
        return True
    # inicializamos las variables
    fib1 = 0
    fib2 = 1
    # Buscar el número de Fibonacci más cercano a num
    while fib2 < num:
        # Actualizar los valores de fib1 y fib2
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
    # Si b es igual al número que estamos comprobando, entonces el número es parte de la serie de Fibonacci
    if fib2 == num: 
        return True
    else:
        return False

def es_par(num: int):
    """Determina si un numero es par o impar"""
    if num % 2 == 0:
        return True
    else:
        return False

def main(num: int):
    message = ''
    if es_primo(num):
        message += f'{num} es primo, '
    else:
        message += f'{num} no es primo, '
    if es_fibonacci(num):
        message += 'fibonacci, '
    else:
        message += 'no es fibonacci, '
    if es_par(num):
        message += 'es par.'
    else:
        message += 'es impar.'
    return message

n = int(input('Ingrese un numero: '))
print(main(n))