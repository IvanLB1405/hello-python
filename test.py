def generate_full_greeting(dict):
    lista = dict.values()
    name, surname = lista
    return f"Hola {name} {surname}"
    

print(generate_full_greeting({"name":"Ivan", "surname":"fernandez"}))

