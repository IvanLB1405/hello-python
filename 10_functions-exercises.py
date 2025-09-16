#01
def personalized_greeting(name = "Desconocido"):
    print(f"Hola {name}")

personalized_greeting("Ivan")
personalized_greeting()

#02
def multiply(num1, num2):
    return num1 * num2

print(multiply(3,4))
print(multiply(2,2))

#03
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(3))
    
#04
def convert_to_uppercase(text):
    return text.upper()

print(convert_to_uppercase("Hola"))

#05
def arbitrary_sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(arbitrary_sum(1,2,3))
print(arbitrary_sum(1))

#06
def generate_full_greeting(name, surname):
    return f"Hola {name} {surname}"

print(generate_full_greeting("Ivan", "Fernandez"))
#07
def power(base, exponente):
    return base ** exponente
print(power(2,4))

#08
def calculate_average(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum / 3

print(calculate_average(2,2,5))

#09
def count_characters(text):
    return len(text)
print(count_characters("Hola"))

#10
def display_messages(*texts):
    for text in texts:
        print(text.upper())
display_messages("Hola", "Ivan", "Barbara", "Lucho")
