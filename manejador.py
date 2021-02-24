from os import linesep
from os import path
from time import sleep
from LectorXML import leerxml
from Listas_Nodos import ListaPrincipal
from procesadorMatriz import procesaMatriz
#from GenerarXML import generaResultado
#from generarGrafo import grafo

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
                leerxml(ruta, nombre+extension)
                print(" >>> Lectura de archivo completa\n")
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