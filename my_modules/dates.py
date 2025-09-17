from datetime import datetime

def get_current_date():
#Convierte a String a partir de un date. STRING FROM TIME
    return datetime.now().strftime("%d-%m-%Y")

def date_difference(date1, date2):
    #Convierte a fecha a partir de un texto. STRING PARSE TIME
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    #Guarda en variables las fechas, (puede hacer operaciones matematicas) y obtiene .days que es propio de objetos date
    return abs((d2-d1).days)