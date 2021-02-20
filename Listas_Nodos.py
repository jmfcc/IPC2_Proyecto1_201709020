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
