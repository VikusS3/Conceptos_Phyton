from datetime import datetime

ahora = datetime.now()
fecha = ahora.date()
hora = ahora.hour
minutos = ahora.minute
dia = ahora.day
mes = ahora.month
año = ahora.year

def print_date(date):
    print(f"{date.day}/{date.month}/{date.year}")
    
print_date(ahora)

#esto es para obtener el timestamp de la fecha actual en segundos desde el 1 de enero de 1970 a las 00:00:00
timestamp = datetime.timestamp(ahora)

año_2024=datetime(2024,1,1)