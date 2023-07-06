###Escribe en el programa para que muestra los números del 1 al 100
# ambos en un salto de linea, reemplazar los numeros 
# multimplos de tres con la plabra fizz
# multiplos de 5 con  buzzz
# y multiplo de 3 y 5 con tezzz###

my_list = [i + 1 for i in range(100)]

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "tezzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzzz"
    else:
        return number

my_list = [fizz_buzz(i) for i in range(100)]
print(my_list)


