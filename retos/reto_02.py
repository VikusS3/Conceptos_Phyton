### escriba una funcion que cuando se ingreso
# dos palabras y estas sean un amagrama retorne 
# un boelano verdadero o falso, sabiendo que un amagrama
# consiste en formar una palabra reordenando TODAS
# las palabras de otra con su incial####


def amagrama(word1, word2):
    #Por si las palabras tienen mayusculas o espacios usar lower y replace
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    #Ordenar las palabras con sorted, que sirve para listas y strings 
    word1 = sorted(word1)
    word2 = sorted(word2)
    #Comparar las palabras si son iguales
    if word1 == word2:
        return True
    else:
        return False
    
print(amagrama("Hola", "aloh"))
print(amagrama("casa", "asco"))
print(amagrama("amor", "roma"))