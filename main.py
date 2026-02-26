import random
import string

def generator(long):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(long):
        password += random.choice(caracteres)

    return password

def main():
    try:
        long = int(input("ingrese la longitud de su contraseña: "))
        password = generator(long)
        print(f"contraseña generada: {password}")
    except ValueError:
        print("Por favor ingrese un número valido.")


if __name__ == "__main__":
    main()


