"""
Descripcion: Programa que maneja archivos de recetas.
En este programa tienes la opción de:
Crear una receta y guardarla en una ruta especifica
Leer la receta del archivo existente,
Borrar una receta existente en una categoria
Crear una nueva categoria en un directorio donde
se almacenarán los archivos
Eliminar una categoría ya sea que tenga archivos
o no.
En este programa se hace lectura y escritura de
archivos planos y de directorios con los metodos
de Python para tales operaciones
Desarrollado por: Sebastian Ponce Vidal
Fecha: 24/02/2025
Modificado: 27/05/2025
Razón: Se lee de un archivo de la base la ruta
de las recetas. La idea de este ajuste es tratar en
lo posible de no dejar quemada la ruta, se usa el
archivo Directorio_Recetas.txt el cual contiene esta
ruta previamente colocada en este archivo
"""
import os
from pathlib import Path, PureWindowsPath
from os import system
from os import remove
from shutil import rmtree

asterisco = "*"
str_dir_receta = "Directorio_Recetas.txt"

def obtener_directorio_recetas(p_file):
    base = Path.home()
    carpeta = Path(str(base)+'/'+p_file)
    if not carpeta.exists():
       return "El archivo o carpeta no existen"
    else:
       return carpeta.read_text()

def mostrar_bienvenida(p_mensaje):

    for i in range(1,2):
        print(asterisco * 92)
    print(asterisco*30+" "+p_mensaje+" "+asterisco*34)

    for i in range(1,2):
        print(asterisco * 92)

def obtener_ruta_receta_cantidad(p_path):

    if not p_path.exists():
        return "No existe la carpeta",0
    else:
        ruta_win = PureWindowsPath(p_path)
        contador_archivos = 0

        for txt in Path(ruta_win).glob("**/*.txt"):
            if txt !='':
                contador_archivos += 1

        return ruta_win,contador_archivos

def mostrar_menu():
    opc_01 = "1 Elige una categoría para leer una receta"
    print(f"{asterisco*20} {opc_01} {asterisco*27}")
    opc_02 = "2 Elige una categoría para crear una receta"
    print(f"{asterisco * 20} {opc_02} {asterisco * 26}")
    opc_03 = "3 Crea una nueva categoría"
    print(f"{asterisco * 20} {opc_03} {asterisco * 43}")
    opc_04 = "4 Elige una categoría para borrar una receta"
    print(f"{asterisco * 20} {opc_04} {asterisco * 25}")
    opc_05 = "5 Borrar una categoría"
    print(f"{asterisco * 20} {opc_05} {asterisco * 47}")
    opc_06 = "6 Salir del recetario"
    print(f"{asterisco * 20} {opc_06} {asterisco * 48}")

def pedir_opc_usuario():
    mi_opc = input("Elige tu opción en el menú: ")

    while not mi_opc.isnumeric():
        print("Opción inválida, recuerda que debes ingresar un valor numérico")
        mi_opc = input("Elige tu opción en el menú: ")
    else:
        opcion_num = int(mi_opc)

        while opcion_num not in range (1,7):
            print("Opción inexistente, intenta de nuevo con las opciones "
                  "que están en el menú")
            mi_opc = input("Elige tu opción en el menú: ")
            opcion_num = int(mi_opc)

    return opcion_num

def validar_menu(p_opc):
    dir_base = obtener_directorio_recetas(str_dir_receta)

    match p_opc:
        case 1:
            print(f"{asterisco*15} Categorías{asterisco*15}")
            mostrar_categorias(dir_base)
            categoria = input("Escribe la categoría a consultar puedes copiarla y pegarla: ")
            leer_categoria(categoria,dir_base,1)
        case 2:
            print(f"{asterisco * 15} Categorías{asterisco * 15}")
            mostrar_categorias(dir_base)
            categoria = input("Escribe la categoría a consultar puedes copiarla y pegarla: ")
            leer_categoria(categoria, dir_base, 2)
        case 3:
            categoria = input("Escribe el nombre de la categoría que deseas crear: ")
            crear_categoria(categoria,dir_base)
        case 4:
            print(f"{asterisco * 15} Categorías{asterisco * 15}")
            mostrar_categorias(dir_base)
            categoria = input("Escribe la categoría a consultar puedes copiarla y pegarla: ")
            leer_categoria(categoria, dir_base, 3)
        case 5:
            print(f"{asterisco * 15} Categorías{asterisco * 15}")
            mostrar_categorias(dir_base)
            categoria = input("Escribe el nombre de la categoría que deseas borrar: ")
            eliminar_categoria(categoria,dir_base)
        case _:
            salir_aplicacion()

def mostrar_recetas(p_dir_base_recetas):
    contador_recetas = 0

    for txt in Path(p_dir_base_recetas).glob("**/*.txt"):
        print(txt.name)
        contador_recetas +=1

    return contador_recetas

def mostrar_categorias(p_dir_base_categorias):
    arr_cat = os.listdir(p_dir_base_categorias)

    for t in arr_cat:
        print(t)

def leer_receta(p_dir_base_cat):
    archivo_selec = input("Escribe la receta que deseas leer del menú, puedes copiarla y pegarla: ")
    dir_arch_sel = Path(p_dir_base_cat+'/'+archivo_selec)

    while not dir_arch_sel.exists():

        c_rec = mostrar_recetas(p_dir_base_cat)

        if c_rec == 0:
            break

        print("El archivo no existe, recuerda escoger los que están en la lista")
        archivo_selec = input("Escribe la receta que deseas leer del menú: ")
        dir_arch_sel = Path(p_dir_base_cat + '/' + archivo_selec)
    else:
        print(dir_arch_sel.read_text())

def escribir_receta(p_dir_base_cat):
    archivo_selec = input("Escribe el nombre del archivo de tu receta: ")
    nom_archivo = p_dir_base_cat+'/'+archivo_selec
    ruta_crear_rec = Path(nom_archivo)

    if ruta_crear_rec.exists():
        print(f"La receta {archivo_selec} ya existe !!!")
    else:
        archivo = open(nom_archivo, 'w')
        contenido_arch = input("Ahora escribe el contenido de tu receta: ")
        archivo.write(contenido_arch)
        archivo.close()
        print("Archivo de receta creado satisfactoriamente !!!!")

def eliminar_receta(p_dir_base_cat):
    archivo_selec = input("Escribe el nombre del archivo de receta que quieres borrar: ")
    nom_archivo = Path(p_dir_base_cat + '/' + archivo_selec)

    if nom_archivo.exists():
        respuesta_f = input("Estás seguro de querer eliminar este archivo ? (s/n): ")
        respuesta_f = respuesta_f.lower()
        if respuesta_f == 's':
            remove(p_dir_base_cat + '/' + archivo_selec)
            print("Tu archivo fue eliminado correctamente !!!")
    else:
        print("El archivo no existe !!!")

def leer_categoria(p_nombre_cat,p_base,p_tip_operacion):
    carpeta_cat = Path(p_base+"/"+p_nombre_cat)

    if not carpeta_cat.exists():
        print(f"Carpeta {carpeta_cat.name} no existe")
    else:
        print(f"{asterisco * 15}Recetas{asterisco * 15}")
        c_rec = mostrar_recetas(carpeta_cat)
        if c_rec > 0:
            if p_tip_operacion == 1:
                leer_receta(p_base + "/" + p_nombre_cat)
            elif p_tip_operacion == 2:
                escribir_receta(p_base + "/" + p_nombre_cat)
            else:
                eliminar_receta(p_base + "/" + p_nombre_cat)
        else:
            if p_tip_operacion == 2:
                escribir_receta(p_base + "/" + p_nombre_cat)

def crear_categoria(p_nombre_cat,p_base):
    ruta_crear = Path(p_base+'/'+p_nombre_cat)

    if not ruta_crear.exists():
        os.makedirs(p_base + '/' + p_nombre_cat)
        print(f"Categoría {p_nombre_cat} creada exitosamente !!!")
    else:
        print("Categoría existente")

def eliminar_categoria(p_nombre_cat,p_base):
    ruta_borrar = Path(p_base+'/'+p_nombre_cat)

    if not ruta_borrar.exists():
        print(f"La categoría {p_nombre_cat} no existe !!!")
    else:
        respuesta_c = input(f"Estás seguro de quieres borrar "
                            f"la categoria {p_nombre_cat} ? (s/n): ")
        respuesta_c = respuesta_c.lower()
        if respuesta_c == 's':
            rmtree(p_base + '/' + p_nombre_cat)
            print(f"Categoría {p_nombre_cat} eliminada exitosamente !!!")

def salir_aplicacion():
    system('cls')

mostrar_bienvenida('Bienvenido(a) al Recetario')
ruta_receta,cantidad_rec = obtener_ruta_receta_cantidad(Path(obtener_directorio_recetas(str_dir_receta)))
print(f"{ruta_receta}")
print(f"Hay {cantidad_rec} receta(s) registrada(s)")

if cantidad_rec > 0:
    mostrar_menu()
    la_opc = pedir_opc_usuario()
    opcion_n = int(la_opc)
    validar_menu(opcion_n)

    if opcion_n < 6:
        continuar = input("Deseas continuar ? (s/n): ")
        continuar = continuar.lower()

        while continuar == 's':
            mostrar_menu()
            la_opc = pedir_opc_usuario()
            opcion_n = int(la_opc)
            validar_menu(opcion_n)

            if opcion_n == 6:
                 break

            continuar = input("Deseas continuar ? (s/n): ")
            continuar = continuar.lower()
        else:
            salir_aplicacion()