#creando una funcion que me devuelva la serie de fibonaci
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610


def fibonaci(num):
    #creando variables
    a=0
    b=1
    #creando un ciclo for
    for i in range(num):
        #creando un generador
        #la funcion yield me permite devolver un valor sin terminar la funcion 
        yield a
        #creando una variable temporal
        a,b=b,a+b

#creando un ciclo for para imprimir los valores de la funcion fibonaci
# for x in fibonaci(5):
#     print(x)


#creando una funcion que me devuelva la serie de fibonaci otra forma


def serie_fibonaci(numero):
    #creando variables
    a,b=0,1
    #creando una lista
    fibonaci_list=[0]
    #creando un ciclo for
    for i in range(numero):
        #creando una condicion para que no se pase del numero que le indique en la funcion
        #si b es mayor que el numero que le indique en la funcion me devuelva la lista
        #si no es mayor que el numero que le indique en la funcion me agrege el valor de b a la lista
        if b>numero: return fibonaci_list
        else:
            fibonaci_list.append(b)
            a,b=b,a+b

resultado=serie_fibonaci(21)
print(resultado)

    
