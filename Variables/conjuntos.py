#ceando un conjunto con set
conjunto= set(["dato 1", "dato 2"])

#metiendo un conjunto dentro de otro conjunto

conjunto1= frozenset(["dato 1", "dato 2"])
conjunto2= {conjunto1, "dato 3"}
print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = {1,3,5,7}

#verificar si un conjunto es subconjunto de otro
resultado = conjunto1.issubset(conjunto2)
#tambien se puede usar <=

#verificar si un conjunto es superconjunto de otro
resultado = conjunto2.issuperset(conjunto1)
#tambien se puede usar >

#vericar si hay un numero en comun entre dos conjuntos
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)
