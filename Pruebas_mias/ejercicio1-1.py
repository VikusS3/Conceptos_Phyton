#promediode duracion 
o_cursos_min = 2.5
o_cursos_max = 7
o_cursos_promedio = 4
dalto_curso= 1.5

#direfencia de crudos
crudo_promedio =5
crudo_dalto =3.5

#diferecia de duracion
diferencia_con_min= round(dalto_curso / o_cursos_min) 
diferencia_con_max= round(dalto_curso  / o_cursos_max, 2) 
diferencia_con_promedio= 100 - dalto_curso / o_cursos_promedio * 100

#calculando el tiempo vacio promedio
tiempo_vacio_promedio = 100 - o_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print("--------------------------------------------------")
#mostrando las diferencias de duracion
print(f"el curso de dalto es {diferencia_con_min} % menos que el mas rapido")
print(f"el curso de dalto es {diferencia_con_max} % menos que el mas lento")
print(f"el curso de dalto es {diferencia_con_promedio} % menos que el promedio")

print("--------------------------------------------------")
#mostrando el tiempo vacio promedio
print("el tiempo vacio promedio es" , tiempo_vacio_promedio , "%")
print("el tiempo vacio de dalto es" , tiempo_vacio_dalto , "%")

print("--------------------------------------------------")
#mostrando la diferencia de si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a {o_cursos_promedio *100// dalto_curso /10} horas de otros cursos")
print(f"ver 10 horas otros cursos equivale a {dalto_curso *100// o_cursos_promedio /10} horas de este  cursos")
