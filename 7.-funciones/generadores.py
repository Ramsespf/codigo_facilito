

def pares():    # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        yield numero    # la funcion suspende su ejecucion

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break