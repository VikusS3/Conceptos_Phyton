yuan = int(input("Introduce el valor en yuanes: "))
won = int(input("Introduce el valor en wones: "))
yen = int(input("Introduce el valor en yenes: "))

cambio_dolar_yuan = yuan * 0.15
cambio_dolar_won = won * 0.0007
cambio_dolar_yen = yen * 0.0075

print("El valor en dolares es: ", cambio_dolar_yuan + cambio_dolar_won + cambio_dolar_yen)
