import re

texto='''En esta cadena se 5 encuentra una palabra magica 8 bien
        , hola, que quiero encontrar. Hola es la palabra
        ;como en hola 2 a COMO, esta escrita _ igual 236 que hola
        ,Estas bien? Estamos muy bien'''
  
#con fla re.IGNORECASE se ignora si la palabra esta en mayuscula o minuscula      
# flags=re.IGNORECASE

#haciendo una expresion regular con re.findall
# resultado=re.findall('Esta', texto)


#\d -- busca digitos numericos del 0 al 9
# resultado=re.findall(r"\d", texto)

#\D -- busca todo lo que no sea un digito numerico
# resultado=re.findall(r"\D", texto)


#\w -- busca todo lo que sea alfanumerico [a-z , A-Z , 0-9  _]
# resultado=re.findall(r"\w", texto)

#\W -- busca todo lo que no sea alfanumerico
# resultado=re.findall(r"\W", texto)

#\s -- busca espacios en blanco, espacios, tabuladores, saltos de linea
# resultado=re.findall(r"\s", texto)

#\S -- busca todo lo que no sea un espacio en blanco
# resultado=re.findall(r"\S", texto)

#. -- busca cualquier caracter, todo menos saltos de linea
# resultado=re.findall(r".", texto)

#\n -- busca saltos de linea
# resultado=re.findall(r"\n", texto)

#\t -- busca tabuladores
# resultado=re.findall(r"\t", texto)

#^ -- busca al inicio de la cadena de texto
#flags=re.M -> busca en cada linea de texto osea lo vueve multilineadddddddddddddddddddddddddddddddddddddddddddddfdddddddddddddd 
# resultado=re.findall(r"^En", texto)

#\ cancelamos caracteres especiales como el punto y coma ;
# resultado=re.findall(r"\;", texto)

#creando una cadena que busque un numero, seguido de un espacio en blanco, seguido de un texto
# resultado=re.findall(r"\d\s\w+", texto)

#$ -- busca al final de la cadena de texto 
# resultado=re.findall(r"bien$", texto, flags=re.M)

#{n} -- busca una cantidad de caracteres especificos
# resultado=re.findall(r"\w{4}", texto)

#{n,m} -- busca una cantidad de caracteres especificos, pero entre un rango
# resultado=re.findall(r"\d{2,4}", texto)

# * -- busca 0 o mas repeticiones de un caracter
# resultado=re.findall(r"\d*", texto)

# + -- busca 1 o mas repeticiones de un caracter
# resultado=re.findall(r"\d+", texto)

# | busca una palabra o la otra palabra 
resultado=re.findall(r"como|bien", texto)

print(resultado)