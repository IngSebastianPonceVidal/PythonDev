"""
Descripcion: Modulo principal que despliega
el menu principal teniendo en cuenta que solo
procesara las opciones en pantalla
Fecha: 03/03/2025
"""
def mostrar_bienvenida(p_simbolo):

    print(p_simbolo * 92)
    print(f"{p_simbolo*30} Bienvenido a la Tienda Python {p_simbolo* 31}")
    print(f"{p_simbolo*30} Nos complace atenderte {p_simbolo * 38}")
    print(p_simbolo * 92)


def desplegar_menu_tienda(p_simbolo):

    opcion_menu = 'x'

    while not opcion_menu.isnumeric() or int(opcion_menu) not in range(1,5):
        print("Elíge una opción para atenderte: ")
        opc_01 = "1 Perfumería"
        print(f"{p_simbolo * 20} {opc_01} {p_simbolo * 32}")
        opc_02 = "2 Farmacia"
        print(f"{p_simbolo * 20} {opc_02} {p_simbolo * 34}")
        opc_03 = "3 Cosmética"
        print(f"{p_simbolo * 20} {opc_03} {p_simbolo * 33}")
        opc_04 = "4 Salir"
        print(f"{p_simbolo * 20} {opc_04} {p_simbolo * 37}")

        try:
            opcion_menu = int(input())
        except ValueError:
            print("No se permiten letras ni caracteres especiales. Intenta de nuevo")
        else:
            if int(opcion_menu) not in range(1, 5):
                print("Opción inválida, escoge las que aparecen en pantalla")
                opcion_menu = 'x'
            else:
                break

    return int(opcion_menu)