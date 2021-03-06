import manejador

def main():
    #Menu Principal
    while True:
        print(" _______________________________________________________________________________")
        print(" _______________________________________________________________________________")
        print()
        print(" [1] - Cargar archivo")
        print(" [2] - Procesar archivo")
        print(" [3] - Escribir archivo de salida")
        print(" [4] - Mostrar datos del estudiante")
        print(" [5] - Generar gráfica")
        print(" [6] - Salir")
        print()
        opcion = input(" >>> Seleccione una opción: ")
        if opcion:
            if opcion == "1":
                print("\n")
                manejador.cargarArchivo()
            elif opcion == "2":
                print("\n")
                manejador.procesarArchivo()
            elif opcion == "3":
                print("\n")
                manejador.escribeSalida()
            elif opcion == "4":
                print()
                #manejador.datosEstudiante()
            elif opcion == "5":
                print()
                #manejador.generaGrafoMatriz()
            elif opcion == "6":
                print("\n >>> Saliendo del programa...")
                break
            else:
                print("\n >>> Opción inválida !!!")
            print()
            print()
        else:
            print(" >>> Aviso: Debes elegir una opción")
main()