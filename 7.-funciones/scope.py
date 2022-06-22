animal = 'Leon'     # ->variable global -> se puede usar en Funcion, Condicion, Ciclo
color = 'verde'
def imprimir_animal():
    animal = 'Ballena'      # -> para python animal son variables diferentes pq estan en scope diferentes
    tipo = 'Mamifero'       # Variable local -> solo se puede usar dentro de la funcion
    global color            # -> modifica la variable global 
    color = 'azul'
    print(animal)

imprimir_animal()

print(animal)
print(tipo)     # Me va a dar un error pq tipo solo se puede usar en la funcion imprimir_animal()