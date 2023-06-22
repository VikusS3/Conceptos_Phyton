#creando una funcion que al ingresar un numero me 
#devuela los numeros primos hasta ese numero

def numeros_primos(numero):
    numeros_primos = []
    for i in range(1, numero+1):
        contador = 0
        for j in range(1, i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            numeros_primos.append(i)
    return numeros_primos



#forma de hacerlo creando dos funciones

#funcion que verifica si un numero es primo
def es_primo(numero):
    for i in range(2, numero-1):
        if numero%i == 0:
            return False
    return True

#funcion que devuelve una lista de numeros primos
def primos_hasta(numero):
    primos=[]
    #recorremos los numeros desde el 3 hasta el numero ingresado
    for i in range(3, numero+1):
        #llamamos a la funcion es_primo y guardamos el resultado
        resultado = es_primo(i)
        #si el resultado es True, agregamos el numero a la lista
        if resultado==True:
            primos.append(i)
    return primos

#llamamos a la funcion primos_hasta y guardamos el resultado
primos = primos_hasta(25)
print(primos)



# numero = int(input("Ingrese un numero: "))
# print(numeros_primos(numero))