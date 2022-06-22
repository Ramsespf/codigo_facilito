from posixpath import split


lenguajes = 'Python Ruby Java Rust C++ C'

listado_lenguajes = lenguajes.split() #-> crea un listado q se crea por el espaciado, si pones en el argumento un caracter el dividira x ese caracter


lenguajes2 = ['Python', 'Ruby', 'Java', 'Rust']

lenguajes2_string = ' '.join(lenguajes2) # -> retorna un  string 