"""
Descripcion: Programa que analiza un texto suministrado
por pantalla. El texto te dirá cuantas veces aparecen
3 letras tambien pedidas en pantalla en el texto,
te dirá la cantidad de palabras en tu texto, te
dirá la primera letra y la última letra del texto,
te mostrará el texto al revés y finalmente, te dice si
la palabra python aparece en tu texto (false/true)
Desarrollado por: Sebastian Ponce Vidal
Fecha: 10/02/2025
Modificado: 26/02/2025
Razón: Validar cuando el usuario no inserta las tres
letras separadas por comas y que no salga la excepcion
del programa y cuando metes un texto en blanco dando enter
"""
texto = input("Inserte un texto de su elección: ")
letras = input("Inserte tres letras cualquiera separadas por comas: ")
texto = texto.strip()
texto_l = texto.lower()
letras_l = letras.lower()
resultado = list(letras_l.split(","))

if texto == '':
    print("No puede insertar un texto en blanco")
else:
    if len(resultado) != 3:
        print("Recuerde que son 3 letras que debe insertar")
    else:
        # Parte 1
        print("La letra " + resultado[0] + " aparece en el texto " + str(texto_l.count(resultado[0])) + " veces")
        print("La letra " + resultado[1] + " aparece en el texto " + str(texto_l.count(resultado[1])) + " veces")
        print("La letra " + resultado[2] + " aparece en el texto " + str(texto_l.count(resultado[2])) + " veces")
        # Parte 2
        texto_a_lista = list(texto_l.split(" "))
        print("Cantidad de palabras en el texto " + str(len(texto_a_lista)))
        # Parte 3
        print(f"La primera letra del texto es '{texto_l[0]}'")
        print(f"La última letra del texto es '{texto_l[len(texto_l) - 1]}'")
        # Parte 4
        texto_original_lista = list(texto.split(" "))
        lista_invertida = texto_original_lista[::-1]
        print(f"El texto al revés se lee así: \"{' '.join(lista_invertida)}\"")
        # Parte 5
        # print("Python" in texto)} Solucion
        buscar_python = 'python' in texto
        dic = {True: "si", False: "no"}
        print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")