import json

print('               --- PLAY WITH DATABASES ---\n')

# Este ejercicio incorpora la logica de entradas de datos usando un archivo JSON para su
# ejecucion e interaccion.

# Aqui definimos la ruta del JSON
filename = 'dbFile.json'

# Encapsulamos el programa en este bucle para jugar con las opciones
while True:
    user = {}

    # Esta funcion valida si los datos son nuevos o ya existentes
    def current_user(new):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            if any(u['name'] == new["name"] or u['email'] == new["email"] for u in data["user"]):
                print('                 -----------')
                print('                      X')
                print('\n         user already exists. Try again')
            else:
                if "user" not in data:
                    data["user"] = []
                data["user"].append(new)
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
                print('                -----------')
                print('          User added successfully')
                print('                -----------')
        except FileNotFoundError:
            print("JSON file not found!")
            new_data = {"user": [new]}
            with open(filename, "w") as new_file:
                json.dump(new_data, new_file, indent=4)
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    # Esta funcion sirve para buscar los resultados por nombre y validar si existen o
    # no en el JSON

    def find_by_name(name):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            found_user = [p for p in data.get("user", []) if p["name"] == name]

            if found_user:
                for u in found_user:
                    print('           --- USER REGISTRED ---')
                    print(
                        f"Name: {u['name']},\n   Age: {u['age']},\n   Email: {u['email']},\n   City: {u['city']}")
            else:
                print('                      X')
                print('              User not found.')
        except FileNotFoundError:
            print("JSON file not found!")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    # Esta funcion sirve para buscar los datos por ciudad y extrae todas las coincidencias
    # que encuentre

    def find_by_city(city):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            found_user = [p for p in data.get("user", []) if p["city"] == city]
            if found_user:
                print(f"                   {len(found_user)} FOUND")
                print('\n')
                for u in found_user:

                    print(f"   Name: {u['name']},  City: {u['city']}")
            else:
                print('                      X')
                print('             Location not found.')
        except FileNotFoundError:
            print("JSON file not found!")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    # Esta funcion sirve para eliminar datos de la base de datos, usando el email del
    # usuario  como identificador

    def delete_user(email):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            # Filtramos los usuarios, quedándonos con todos los que NO tengan el email a eliminar
            users = data.get("user", [])
            updated_users = [user for user in users if user["email"] != email]
            if len(updated_users) == len(users):
                print('                      X')
                print("              User not found.")
            else:
                data["user"] = updated_users
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
                print('                -----------')
                print("          User deleted successfully")
                print('                -----------')
        except FileNotFoundError:
            print("JSON file not found!")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    # Dentro de esta funcion validamos toda la ejecucion de las funciones anteriores,
    # usando un modelo de opciones a elegir

    def main():
        while True:
            print('   Select an option:\n')
            print('1. Input User')
            print('2. Search by name')
            print('3. Search by city')
            print('4. Delete user')
            print('5. Exit\n')

            option = input('   Write the number for your option: ')
            print("\n")

            if option == "1":

                user_name = input('write a name: ')
                user_age = input('write an age: ')
                user_email = input('write an email: ')

                while "@" not in user_email or "." not in user_email:
                    print('Email must be a valid format.')
                    user_email = input('write the email correctly: ')

                user_city = input('write a city: ')

                new_user = {"name": user_name, "age": user_age,
                            "email": user_email, "city": user_city}

                current_user(new_user)

            elif option == "2":
                name = input('write a name to search: ')
                print('                 -----------')
                find_by_name(name)
                print('                 -----------\n')

            elif option == "3":
                city = input('write the city to search: ')
                print('                 -----------')
                find_by_city(city)
                print('                 -----------\n')

            elif option == "4":
                email_to_delete = input(
                    'write the email of the user to delete: ')
                print('                 -----------')
                delete_user(email_to_delete)
                print('                 -----------\n')

            elif option == "5":
                break

            else:
                print('Invalid. Please select a correct option.')

    if __name__ == "__main__":
        main()

    # Solo para efectos practicos, usamos esta validacion para decidir si continuamos
    # usando el programa o no
    options = input("   ¿Do you want to keep using the aplication?: ")
    print("                 -----------")
    if options == 'si' or options == 's':
        continue
    elif options == 'yes' or options == 'y':
        continue
    else:
        print(input("press ENTER to exit: "))
        exit()
