"""
a -> La funcion principal (Decorador)
b -> La funcion a decorar
c -> La funcion decorada

a(b) -> c
"""



def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
        print('>>> Antes del llamado')

        resultado = funcion_b(*args, **kwargs)        

        print('>> Despues del llamado')

        return resultado        
    
    return funcion_c

@funcion_a
def suma(num1, num2):
    return num1 + num2

resultado = suma(40, 20)
print(resultado)

    