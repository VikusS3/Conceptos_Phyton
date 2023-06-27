import re

email="feli24@gmail.com"


pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#con match solo busca al inicio de la cadena de texto 
result=re.match(pattern, email)

if result:
    print("Correo valido")
else:
    print("Correo invalido")