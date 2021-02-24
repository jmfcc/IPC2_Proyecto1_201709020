from Listas_Nodos import ListaSimpleCircular
from Listas_Nodos import ListaGrupo
from time import sleep

def procesaMatriz(filas, columnas, matriz):
    #print(matriz.dameMatrizEnFormato())
    print(" >>> Calculando matriz binaria... ")
    sleep(1)
    listaTemp = ListaSimpleCircular()
    listaTemp.generaListaDeDimension(filas,columnas)
    aux = matriz.getInicio()
    while True:
        if aux.getValor() == 0:
            listaTemp.reemplazaDatos(aux.getFila()+1, aux.getColumna()+1, 0)
        else:
            listaTemp.reemplazaDatos(aux.getFila()+1, aux.getColumna()+1, 1)
        if aux.getSiguiente() == matriz.getInicio():
            break
        else:
            aux = aux.getSiguiente()
    if listaTemp.evaluaLista():
        #print(listaTemp.dameMatrizEnFormato())
        return analizaPatrones(filas, columnas, matriz, listaTemp)

def analizaPatrones(filas, columnas, matriz, mapaPatron):
    print(" >>> Analizando patrones binarios... ")
    sleep(1)
    groupsTemps = ListaGrupo()
    counterGroup = 1
    for i in range(0, filas-1):
        if not groupsTemps.buscaEnGrupo(i):
            groupsTemps.agregaFinal(counterGroup, i)
            for j in range(i+1, filas):
                esigual = True
                for k in range(0, columnas):
                    if mapaPatron.dameDatos(i+1, k+1) != mapaPatron.dameDatos(j+1, k+1):
                        esigual = False
                        break
                if esigual:
                    groupsTemps.agregaFinal(counterGroup, j)
            groupsTemps.setGruposTot(counterGroup)
            counterGroup += 1
    if not groupsTemps.buscaEnGrupo(filas-1):
        groupsTemps.agregaFinal(counterGroup, filas-1)
        groupsTemps.setGruposTot(counterGroup)
    #print(groupsTemps.getInfo())
    return reduceMatriz(filas, columnas, matriz, groupsTemps)

def reduceMatriz(filas, columnas, matriz, groupsTemps):
    print(" >>> Suma de tuplas y reducción de matriz... ")
    sleep(1)
    if filas == groupsTemps.getGruposTot():
        #print(matriz.dameMatrizEnFormato())
        return matriz, groupsTemps
    else:
        listaTemp = ListaSimpleCircular()
        listaTemp.generaListaDeDimension(groupsTemps.getGruposTot(), columnas)
        for i in range(0, groupsTemps.getGruposTot()):
            for j in range(0, columnas):
                suma = 0
                aux = groupsTemps.getInicio()
                while True:
                    if aux.getGrupo()-1 == i:
                        suma = suma + matriz.dameDatos(aux.getFila() + 1, j + 1)
                    if aux.getSiguiente() == groupsTemps.getInicio():
                        break
                    else:
                        aux = aux.getSiguiente()
                listaTemp.reemplazaDatos(i+1,j+1,suma)
        #print(listaTemp.dameMatrizEnFormato())
        return listaTemp, groupsTemps
