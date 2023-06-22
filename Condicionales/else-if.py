ingreso_semanal = 22000
gasto_semanal = 50000

#if anidados y else if

if ingreso_semanal > 1000:
    if ingreso_semanal - gasto_semanal >3000:
        print("Estas bien")

    elif ingreso_semanal - gasto_semanal > 1000:
         print("cuando menos estas bien")

    else:
        print("Estas mal")

else:
    print("Ingreso bajo")