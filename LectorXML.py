from xml.dom import minidom
#import os
import time
import manejador
from Listas_Nodos import ListaSimpleCircular

def leerxml(ruta, nArchivo): 
    print(" >>> Obteniendo archivo de ", ruta)
    time.sleep(0.6)
    archivo = minidom.parse(ruta)
    print(" >>> Lectura de "+ nArchivo +"\n")
    for matrix in archivo.getElementsByTagName("matrices"):
        for matriz in matrix.getElementsByTagName("matriz"):
            taBien = True
            nombre = matriz.getAttribute("nombre")
            # Validar nombre
            if validaNombre(nombre):
                print(" >>> Error: Se encontró una matriz con el nombre " + nombre)
                break
            try:
                n = int(matriz.getAttribute("n"))
                m = int(matriz.getAttribute("m"))
            except:
                print(" >>> Error: Se ha detectado un valor no numérico")
                break
            
            for datos in matriz.getElementsByTagName("dato"):
                try:
                    x = int(datos.getAttribute("x"))
                    y = int(datos.getAttribute("y"))
                    attr = int(datos.firstChild.data)
                except:
                    print(" >>> Error: Se ha detectado un valor no numérico para la matriz " + nombre)
                    taBien = False
                    break
                if x > n and y > m:
                    print(" >>> Error: Se ha detectado un indice fuera de rango para la matriz " + nombre)
                    taBien = False
                    break               
            
            if taBien:
                listaTemporal = ListaSimpleCircular()
                listaTemporal.generaListaDeDimension(n,m)
                for datos in matriz.getElementsByTagName("dato"):
                    try:
                        x = int(datos.getAttribute("x"))
                        y = int(datos.getAttribute("y"))
                        attr = int(datos.firstChild.data)
                        listaTemporal.reemplazaDatos(x,y,attr)
                    except:
                        print(" >>> Error: Se detectaron problemas al crear la matriz")
                        taBien = False
                        break
                if listaTemporal.evaluaLista():
                    #print(listaTemporal.dameMatrizEnFormato())
                    manejador.agregaEnLista(nombre, n, m, listaTemporal)

    time.sleep(1)

def validaNombre(nombre):
    lista = manejador.getLista()
    if not lista.estaVacia():
        return lista.existeNombre(nombre)
    return False
   

#leerxml("C:/Users/Jaime/Documents/DEVELOP/PYTHON/2021_1S/IPC/archivo.xml","archivo1")
#leerxml()