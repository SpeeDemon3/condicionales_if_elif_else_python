### Condicionales ###
warrior = 'Antonio'
print("Is warrior == 'Antonio'? I predict True")
print(warrior == 'Antonio') ## Es igual

print("Is warrior == 'Chula'? I predict False")
print(warrior != 'Chula') ## NO es igual

### Pruebas condicionales ###
# Prueba con cadenas
chain_1 = 'Hello'
chain_2 = 'Bye'
print(chain_1 == chain_2) # False
print(chain_1 != chain_2) # True
chain_3 = 'bye'
print(chain_1.lower() == chain_3.lower()) # False
print(chain_2.lower() == chain_3.lower()) # True

# Prueba con enteros
int_x = 3
int_y = 90
int_z = 22
print(int_x >= int_y and int_x <= int_z) # False, se deben cumplir las 2 condiciones para que sea True
print(int_x < int_y or int_x > int_y) # True, con que una de las 2 condiciones sea cierta devolvera True
print(int_x != int_y) # True, no es igual
print(int_y >= int_z) # True
print(int_z >= int_y) # False

# Prueba con listas para comprobar si contienen un valor especifico
number_list = [1, 3, 45, 33, 100]
num = 3
print(num in number_list) # True, el valor esta dentro de la lista

char_list = ['a', 'b', 'c']
char_a = 'a'
char_i = 'i'
print('e' in char_list) # False 'e' no esta dentro de la lista
print(char_a not in char_list) # False, char_a si esta dentro de la lista
print(char_i not in char_list) # True, char_i no esta dentro de la lista


### Condicional IF ###

names = ['ferrari', 'bmw', 'nissan', 'tesla'] # Lista de valores
for name in names: # Recorremmos la lista utilizando un bucle for
    if name == 'bmw': # Condicional que comprueba si el valor es igual a 'bmw
        print(name.upper()) # De ser asi, se imprime el valor en letras mayusculas
    else: # Si no
        print(name.title()) # Solo se imprime la primera letra en mayuscula

### Condicional if-elif-else ###
age = 136

if age < 4: # Si es menor a 4
    price = 0 # Variable que contiene el precio dependiendo de la condicion
elif age < 18: # Si es menos a 18
    price = 25
elif age >= 65:
    price = 10
else: # Si tiene 18 o mas
    price = 50

print(f"\tYour admission cost is {price}€")


favorite_color = "red"

if favorite_color == "red":
    print(f"Your favorite color is {favorite_color.upper()}")
elif favorite_color == 'green':
    print("Your favorite color is green")
elif favorite_color == 'yelow':
    print("Your favorite color is yellow")

if favorite_color == "blue":
    print()


age = 4
if age < 2: # Si es menor de 2
    print('You are baby')
elif age > 2 and age < 4: # Si es mayor a 2 y menor a 4
    print('You are childish')
elif age >= 4 and age <= 13: # Si es mayor o igual a 4 y menor o igual a 13
    print('You are a child')
elif age >= 13 and age < 20: # Si es mayor o igual a 13 y menor a 20
    print('You are a teen')
elif age >= 20 and age < 65: # Si es mayor o igual a 20 y menor a 65
    print('You are an adult')
else: # Si es mayor o igual a 65
    print('You are old man')

favorite_fruits = ['banana', 'orange', 'apple', 'melon']

if 'banana' in favorite_fruits:
    print(favorite_fruits[0])

if 'watermelon' in favorite_fruits:
    print()

if 'orango' not in favorite_fruits:
    print('True')

### Sentencias if con listas
cars = ["audi", "seat", "mustang", "ferrari", "tesla"]
for car in cars:
    if car  == "audi": # Si la marca es audi se informa de que no estan disponibles
        print("Sorry, we don´t have audis right now")
    else: # En caso contrario se informa de las marcas disponibles
        print(f"We have the brand {car.title()} available")

### Comprobar si una lista esta vacia
requested_toppings = []

if requested_toppings: # Utilizando el nombre de una lista en una sentencia if python devuelve True si la lista contiene al menos un elemento
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFisnished making your pizza!.') # Como la lista esta vacia imprimira este mensaje
else:
    print('\nAre you sure you want a plain pizza?')


# Hola, admin
users_web = ['admin', 'user1', 'user2', 'user3'] # Lista de usuarios y administrador

if users_web: # Compruebo si la lista esta vacia
    for user in users_web: # Con un bucle for recorro todos los elementos de la lista
        if user == 'admin': # Si el usuario es el administrador
            print(f'Hello {user.title()} Do you want to see a status report?') # Se imprimira un mensaje especial
        else: # Si no
            print(f"Hello {user.title()}!!! Thanks for coming back.") # Imprimo un saludo para cada usuario
else:
    print("There aren't users")

# Comprobar nombres de usuario
current_users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7'] # Lista de usuarios

new_users = ['user8', 'user9', 'user1', 'user2'] # Lista de nuevos usuarios

if new_users:
    for new_user in new_users:
        if new_user in current_users: # Si el nombre del nuevo usuario ya esta usandose en la lista de usuarios
            print('You have to enter another name.')  # Se informa de que debe escoger otro nombre
        else:  # Si el nombre no se esta usando, esta disponible
            print('Username is available.')

# Numeros ordinales
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista de numeros

for num in numbers_list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")