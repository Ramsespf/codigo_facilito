nombre = 'Eduardo Ismael'
apellido = 'Garcia'

nombre_completo = nombre + '' + apellido # -> Eduardo Ismael Garcia

nombre_completo2 = '%s %s' %(nombre, apellido) # -> Eduardo Ismael Garcia

nombre_completo3 = '{} {} {}'.format(nombre, apellido, 'Perez') # -> Eduardo Ismael Garcia Perez

nombre_completo4 = '{nombre} {primer_apellido} {segundo_apellido}'.format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = 'Perez'
)

nombre_completo5 = f'{nombre} {apellido} '

print(nombre_completo5)

