frutas = ["manzana", "pera", "mango", "piña", "fresa", "uva", "sandia", "melon", "cereza", "durazno"]

#continue hace que se salte el ciclo y continue con el siguiente
for fruta in frutas:
    if fruta == "pera":
        continue
    print("Voy a comer una fruta llamada " + fruta)


#evitar que el ciclo siga ejecutandose
for fruta in frutas:
    print("Voy a comer una fruta llamada " + fruta)
    if fruta == "piña":
        break
    print("Voy a comer una fruta llamada " + fruta)

print("Fin del ciclo")