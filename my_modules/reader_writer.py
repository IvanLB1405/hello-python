def lectura(filename):
    try:
        with open(filename, 'r')  as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print(f"Ha ocurrido un error --> {e}")

def escritura(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except FileNotFoundError as e:
        print(f"Ha ocurrido un error {e}")
