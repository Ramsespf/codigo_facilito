lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
lista_cursos_2 = ['C', 'C++', 'Docker']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

lista_cursos[4] = 'Rust'    #-> reemplaza Java por Rust

#[star:end] el indice final no se toma en cuenta
#[start:] -> obtenemos los ultimos elementos de la lista
#[:end] -> obtenemos los primeros elementos de la lista
#[star:end:skip] -> toma los valores pero saltando por la cantidad de saltos
                                
sub_lista = lista_cursos[0:3]
sub_lista_inv = lista_cursos[::-1]  #d esta manera logro invertir la lista ya q los saltos son -1

lista_cursos.append('MongoDB')
lista_cursos.append('C#')

len(lista_cursos)   #-> longitud de la lista

lista_cursos.insert(1, 'Rails') #-> inserta Rails en la posicion del indice 1

lista_cursos.extend(lista_cursos_2) #-> inserta la otra lista dentro d la otra

lista_cursos.remove('MongoDB') #-> elimina MongoDB

del lista_cursos[0] #-> elimina lo q exista en el indice

lista_cursos.clear() #-> Elimina todos los elementos d la lista