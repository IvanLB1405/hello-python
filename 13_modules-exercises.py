from my_modules import calculator

print(calculator.sumValues(2,3))

from my_modules import converter

print(converter.convert_temperature(20))

from my_modules import students

students.names_showcase()

from my_modules import geometry
print(geometry.circle_area(12))
print(geometry.square_area(2))

from my_modules import enhanced_calc
print(enhanced_calc.sum_alot(1,2,3,4,5))

from my_modules.car import Car
coche = Car("Renault", "Clio", 2020)
coche.accelerate()
print(coche.get_speed())

from my_modules.reader_writer import lectura, escritura
escritura("./test-files/Hola.txt", "Soy Ivan")
lectura("./test-files/Hola.txt")

from my_modules.statistics import media, mediana
lista1 = [1,2,30,4,5,6]
print(f"La media de la {lista1} es {media(lista1)}")
print(f"La mediana de la {lista1} es {mediana(lista1)}")

from my_modules.word_counter import word_counter
print(f"La cantidad de veces que aparece la palabra especificada es: {word_counter("Hola Hola hola ivan", "Hola")}")

from my_modules.dates import get_current_date, date_difference
print(get_current_date())
print(date_difference("10-10-1994", "20-10-1994"))