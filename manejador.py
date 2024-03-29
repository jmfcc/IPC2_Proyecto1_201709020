from os import path
from time import sleep
from LectorXML import leerxml
from Listas_Nodos import ListaPrincipal
from procesadorMatriz import procesaMatriz
from generarXML import generaResultado
from generarGrafo import grafo

listaPrueba = ListaPrincipal()

def getLista():
    global listaPrueba
    return listaPrueba

def agregaEnLista(nombre, fil, cols, matriz):
    global listaPrueba
    listaPrueba.agregaFinal(nombre, fil, cols, matriz)

def cargarArchivo():
    global listaPrueba
    if not listaPrueba.estaVacia():
        print(" >>> Los registros anteriores han sido borrados...")
        listaPrueba = ListaPrincipal()
    print(" _______________________________________________________________________________")
    print(" _______________________________________________________________________________")
    print()
    ruta = input(" >>> Ingresa la ruta del archivo: ")
    if ruta:
        if path.isfile(ruta):
            ph, fh = path.split(ruta)
            nombre, extension = path.splitext(fh)
            if extension == ".xml":
                try:
                    leerxml(ruta, nombre+extension)
                    print(" >>> Lectura de archivo completa\n")
                except:
                    print("\n >>> Error: La lectura no se completo correctamente, verifique su archivo de entrada\n")
            else:
                print(" >>> El archivo no es de extensión XML")
        else:
            print(" >>> Fichero no encontrado")
        #listaPrueba.muestraLista()
    else:
        print(" >>> Debe ingresar una ruta!!!")
    
    stop = input(" >>> Presione ENTER para continuar...")

#Crear lista temporal de NodoMatriz para Matriz binaria
def procesarArchivo():
    if listaPrueba.estaVacia():
        print(" >>> Error: No hay registros en memoria")
    else:
        aux = listaPrueba.getInicio()
        while True:
            print()
            print(" >>> PROCESANDO MATRIZ " + aux.getNombre() + "...")
            #procesaMatriz(aux.getFilas(), aux.getColumnas(), aux.getMatriz()) #listaMatrizPatron
            matrizRedu, grupos = procesaMatriz(aux.getFilas(), aux.getColumnas(), aux.getMatriz()) #listaMatrizPatron
            aux.setMatrizRedu(matrizRedu)
            aux.setGrupos(grupos)
            if aux.getSiguiente() == listaPrueba.getInicio():
                break
            else:
                aux = aux.getSiguiente()
        print()
        #listaPrueba.muestraLista()
        listaPrueba.yaProcesado()

def escribeSalida():
    global listaPrueba
    if listaPrueba.estaProcesado():
        print(" _______________________________________________________________________________")
        print(" _______________________________________________________________________________")
        print()
        ruta = input(" >>> Ingresa la ruta de salida del archivo: ")
        if ruta:
            try:
                ph, fh = path.split(ruta)
                nombre, extension = path.splitext(fh)
                if extension == ".xml":
                    file = open(ruta, "w+")
                    aux = listaPrueba.getInicio()
                    file.write("<?xml version=\"1.0\" ?>")
                    file.write("\n<matrices>")
                    while True:
                        formatoXML = generaResultado(aux.getNombre(), aux.getColumnas(), aux.getGrupos(), aux.getMatrizRedu())
                        file.write(formatoXML.replace("<?xml version=\"1.0\" ?>",""))
                        if aux.getSiguiente() == listaPrueba.getInicio():
                            break
                        else:
                            aux = aux.getSiguiente()
                    file.write("</matrices>")
                    file. close()
                    #print(" >>> Archivo Cargado -- ", nombre + extension,"\n")
                    print(" >>> Salida generada exitosamente\n")
                else:
                    print(" >>> El archivo no es de extensión XML")
            except:
                print(" >>> Error: La dirección no existe o falta nombre del archivo\n")
            #listaPrueba.muestraLista()
        else:
            print(" >>> Debe ingresar una ruta!!!")
        
        stop = input(" >>> Presione ENTER para continuar...")
    else:
        if listaPrueba.estaVacia():
            print(" >>> Error: No hay registros en memoria")
        else:
            print(" >>> Aviso: Las matrices no han sido procesadas")

def generaGrafoMatriz():
    global listaPrueba
    if listaPrueba.estaVacia():
        print(" >>> Error: No hay registros en memoria")
    else:
        print(" _______________________________________________________________________________")
        print(" _______________________________________________________________________________")
        print()
        listaPrueba.muestraNombres()
        seleccion = input(" >>> Ingresa el nombre de la matriz para generar su grafo: ")
        if seleccion:
            if listaPrueba.existeNombre(seleccion):
                nodoMatriz = listaPrueba.dameNodo(seleccion)
                grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getMatriz())
                #print(nodoMatriz.getMatriz().dameMatrizEnFormato())
            else:
                print(" >>> Selección inválida")
        else:
            print(" >>> Aviso: Debes elegir una opción")

def datosEstudiante():
    print("Jaime Efraín Chiroy Chavez")
    print("201709020")
    print("Introducción a la Programación y Computación 2 Sección D")
    print("Ingeniería en Ciencias y Sistemas")
    print("4to. Semestre")

    stop = input("\n >>> Presione ENTER para continuar...")