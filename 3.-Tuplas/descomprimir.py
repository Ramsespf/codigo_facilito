numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro = numeros #-> agrega a  uno = 1 a dos = 2 y asi a cada valor d la tupla

uno, dos, tres, cuatro, *resto_valores = numeros #-> *resto_valores lo q hace es crear una lista y coger todos los demas valores d la tupla q no fueron desempaquetados

# _ -> se usa para Omitir valor

uno, dos, tres, cuatro, *_ = numeros

uno, dos, tres, cuatro, *_, nueve, diez = numeros #-> Python sabe q esos dos ultimos elemntos si los va a asignar al q les corresponde


