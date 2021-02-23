class NodoGrupo():
    
    def __init__(self, grupo, fila):
        self.grupo = grupo
        self.fila = fila
        self.siguiente = None
    
    def getFila(self):
        return self.fila

    def getGrupo(self):
        return self.grupo

    def getSiguiente(self):
        return self.siguiente

    def setFila(self, fila):
        self.fila = fila
    
    def setGrupo(self, grupo):
        self.grupo = grupo

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

class ListaGrupo():

    def __init__(self):
        self.inicio = None
        self.gruposTot = 0
    
    def getInicio(self):
        return self.inicio
    
    def getGruposTot(self):
        return self.gruposTot

    def setGruposTot(self, grTot):
        self.gruposTot = grTot

    def estaVacia(self):
        return (self.inicio == None)

    def agregaInicio(self, grupo, filas):
        if self.estaVacia():
            self.inicio = NodoGrupo(grupo, filas)
            self.inicio.setSiguiente(self.inicio)
        else:
            aux = self.inicio
            tmp = NodoGrupo(grupo, filas)
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            tmp.setSiguiente(self.inicio)
            self.inicio = tmp
            aux.setSiguiente(self.inicio)

    def agregaFinal(self, grupo, filas):
        if self.estaVacia():
            self.inicio = NodoGrupo(grupo, filas)
            self.inicio.setSiguiente(self.inicio)
        else:
            tmp = NodoGrupo(grupo, filas)
            aux = self.inicio
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            aux.setSiguiente(tmp)
            tmp.setSiguiente(self.inicio)

    def buscaEnGrupo(self, fila):
        if self.estaVacia():
            return False
        else:
            aux = self.inicio
            while True:
                if aux.getFila() == fila:
                    return True
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            return False

    def getInfo(self):
        info = "GrupTot: " + str(self.getGruposTot()) + "\n\n"
        aux = self.inicio
        while True:
            info = info + "Fila: " + str(aux.getFila()) + "\nGrupo:" + str(aux.getGrupo()) + "\n\n"
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return info


class Nodo():

    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None

    def setFila(self, fila):
        self.fila = fila

    def setColumna(self, columna):
        self.columna = columna
    
    def setValor(self, valor):
        self.valor = valor

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna
    
    def getValor(self):
        return self.valor

    def getSiguiente(self):
        return self.siguiente   

class ListaSimpleCircular():

    def __init__(self):
        self.inicio = None

    def estaVacia(self):
        return (self.inicio == None)

    def agregaInicio(self, fila, columna, valor):
        if self.estaVacia():
            self.inicio = Nodo(fila, columna, valor)
            self.inicio.setSiguiente(self.inicio)
        else:
            aux = self.inicio
            tmp = Nodo(fila, columna, valor)
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            tmp.setSiguiente(self.inicio)
            self.inicio = tmp
            aux.setSiguiente(self.inicio)

    def agregaFinal(self, fila, columna, valor):
        if self.estaVacia():
            self.inicio = Nodo(fila, columna, valor)
            self.inicio.setSiguiente(self.inicio)
        else:
            tmp = Nodo(fila, columna, valor)
            aux = self.inicio
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            aux.setSiguiente(tmp)
            tmp.setSiguiente(self.inicio)

    def getInicio(self):
        return self.inicio

    #Funcion de creación de lista de tamaño x,y
    def generaListaDeDimension(self, filas, columnas):
        for i in range(0, filas):
            for j in range(0, columnas):
                self.agregaFinal(i,j,"#")
                #self.agregaFinal(i,j,str(i)+"-"+str(j))
    #Funcion de validación de lista
    def evaluaLista(self):
        aux = self.inicio
        while True:
            value = str(aux.getValor())
            try:
                int(value)
            except:
                return False
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return True

    def reemplazaDatos(self, fila, columna, valor):
        aux = self.inicio
        while True:
            if aux.getFila() == fila-1 and aux.getColumna() == columna-1:
                aux.setValor(valor)
                return True
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return False

    def dameDatos(self, fila, columna):
        aux = self.inicio
        while True:
            if aux.getFila() == fila-1 and aux.getColumna() == columna-1:
                return aux.getValor()
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return None

    def dameMatrizEnFormato(self):
        txt = ""
        aux = self.inicio
        filaActual = aux.getFila()
        while True:
            if filaActual == aux.getFila():
                txt = txt + str(aux.getValor()) + "   "
            else:
                filaActual = aux.getFila()
                txt = txt + "\n" + str(aux.getValor()) + "   "
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return txt


class NodoPrincipal():

    def __init__(self, nombre, filas, columnas, matriz):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.grupos = None
        self.matriz = matriz
        self.matrizRedu = None
        self.siguiente = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFilas(self, filas):
        self.filas = filas

    def setColumnas(self, columnas):
        self.columnas = columnas

    def setGrupos(self, grupos):
        self.grupos = grupos

    def setMatriz(self, matriz):
        self.matriz = matriz

    def setMatrizRedu(self, matrizRedu):
        self.matrizRedu = matrizRedu

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getNombre(self):
        return self.nombre

    def getFilas(self):
        return self.filas

    def getColumnas(self):
        return self.columnas

    def getGrupos(self):
        return self.grupos

    def getMatriz(self):
        return self.matriz

    def getMatrizRedu(self):
        return self.matrizRedu

    def getSiguiente(self):
        return self.siguiente

    def getInfo(self):
        if self.matrizRedu == None:
            info = "Nombre: " + self.nombre + "\nFilas: " +  str(self.filas) + "\nColumnas: " + str(self.columnas) + "\nGrupos: " + str(self.grupos) + "\nMatriz Original:\n" + self.matriz.dameMatrizEnFormato() + "\nMatriz Reducida:\n"
        else:
            info = "Nombre: " + self.nombre + "\nFilas: " +  str(self.filas) + "\nColumnas: " + str(self.columnas) + "\nGrupos: " + str(self.grupos) + "\nMatriz Original:\n" + self.matriz.dameMatrizEnFormato() + "\nMatriz Reducida:\n" + self.matrizRedu.dameMatrizEnFormato()
        return info

class ListaPrincipal():

    def __init__(self):
        self.inicio = None
        self.procesado = False

    def yaProcesado(self):
        self.procesado = True

    def estaProcesado(self):
        return self.procesado

    def estaVacia(self):
        return (self.inicio == None)

    def agregaInicio(self, nombre, filas, columnas, matriz):
        if self.estaVacia():
            self.inicio = NodoPrincipal(nombre, filas, columnas, matriz)
            self.inicio.setSiguiente(self.inicio)
        else:
            aux = self.inicio
            tmp = NodoPrincipal(nombre, filas, columnas, matriz)
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            tmp.setSiguiente(self.inicio)
            self.inicio = tmp
            aux.setSiguiente(self.inicio)

    def agregaFinal(self, nombre, filas, columnas, matriz):
        if self.estaVacia():
            self.inicio = NodoPrincipal(nombre, filas, columnas, matriz)
            self.inicio.setSiguiente(self.inicio)
        else:
            tmp = NodoPrincipal(nombre, filas, columnas, matriz)
            aux = self.inicio
            while True:
                if aux.getSiguiente() == self.inicio:
                    break
                else:
                    aux = aux.getSiguiente()
            aux.setSiguiente(tmp)
            tmp.setSiguiente(self.inicio)

    def existeNombre(self, nombre):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                return True
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return False

    def dameNombres(self):
        aux = self.inicio
        listaNombres = []
        while True:
            listaNombres.append(aux.getNombre())
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return listaNombres

    def dameNodo(self,nombre):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                return aux
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()
        return None

    def getInicio(self):
        return self.inicio

    def muestraLista(self):
        aux = self.inicio
        while True:
            i= aux.getInfo()
            print(" ________________________________________")
            print(i)
            if aux.getSiguiente() == self.inicio:
                break
            else:
                aux = aux.getSiguiente()

# listaPrueba = ListaSimpleCircular()
# listaPrueba.generaListaDeDimension(3,4)
# listaPrueba.reemplazaDatos(1,1,1)
# listaPrueba.reemplazaDatos(3,2,10)
# listaPrueba.reemplazaDatos(3,3,11)
# listaPrueba.reemplazaDatos(1,3,3)
# listaPrueba.reemplazaDatos(2,4,5)
# listaPrueba.reemplazaDatos(2,1,8)
# listaPrueba.reemplazaDatos(2,2,7)
# listaPrueba.reemplazaDatos(1,2,2)
# listaPrueba.reemplazaDatos(2,3,6)
# listaPrueba.reemplazaDatos(3,1,9)
# listaPrueba.reemplazaDatos(1,4,4)
# listaPrueba.reemplazaDatos(3,4,12)
# print(listaPrueba.dameMatrizEnFormato())
# print(listaPrueba.evaluaLista())