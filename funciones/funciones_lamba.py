#crenado funciones lamba
#las funciones lamba son funciones anonimas, es decir, que no tienen nombre
#sintaxis: lambda <parametros>: <lo que retorna>
#nota: las funciones lamba solo pueden tener una linea de codigo no mas
#ejemplo:
multiplicar = lambda num1, num2: num1 * num2

numeros=[1,2,3,4,5,6,7,8,9,10]


def es_par(num):
    if num % 2 == 0:
        return True

#usando filter para filtrar los numeros pares
#filter recibe dos parametros, el primero es una funcion y el segundo es un iterable
#filter retorna un objeto de tipo filter, por lo que hay que convertirlo a una lista
#ejemplo:
numeros_pares = list(filter(es_par, numeros))


#usando filter con una funcion lamba
numeros_pares = list(filter(lambda num: num % 2 == 0, numeros))
print(numeros_pares)