import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# Validar la longitud de la contraseña
while True:
    try:
        min_length = int(input("Agrega la cantidad de caracteres para la contraseña: "))

        if min_length > 0:
            break
        else:
            print("❌ La cantidad debe ser mayor que 0.")
    except ValueError:
        print("❌ Solo puedes ingresar números.")

# Validar si desea incluir números
while True:
    respuesta = input("¿Desea incluir números en la contraseña? (s/n): ").lower()

    if respuesta == "s":
        has_number = True
        break
    elif respuesta == "n":
        has_number = False
        break
    else:
        print("❌ Solo puedes escribir 's' o 'n'.")

# Validar si desea incluir caracteres especiales
while True:
    respuesta = input("¿Desea incluir caracteres especiales en la contraseña? (s/n): ").lower()

    if respuesta == "s":
        has_special = True
        break
    elif respuesta == "n":
        has_special = False
        break
    else:
        print("❌ Solo puedes escribir 's' o 'n'.")

# Generar contraseña
pwd = generate_password(min_length, has_number, has_special)
print("La contraseña creada es:", pwd)