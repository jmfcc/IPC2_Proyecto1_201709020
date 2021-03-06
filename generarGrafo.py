from os import system
from os import path
import time

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #print("lo que obtengo ",ruta)
    return ruta

def mimetodo(di):
    try:
        time.sleep(2)
        system (di)
    except:
        print("Error al generar png")
    
def grafo(nombreM, filas, columnas, matriz):
    ruta = getsource()
    nombre = ruta + "\\DiagramaMatriz"
    file = open(nombre + ".dot", "w")
    file.close()
    
    escrituranorm("digraph d{", nombre)
    #escrituranorm("\trankdir = LR", nombre)
    escrituranorm("\tgraph [dpi = 300];", nombre)
    escrituranorm("\tnode [shape = box];", nombre)
    escrituranorm("\tcompound=true;\n", nombre)
    
    #CREACION DE NODOS
    log = "\tnodeStart[shape=oval,label=\"Matrices\"];"
    escrituranorm(log, nombre)
    log = "\tnodeName[shape=oval,label=\""+nombreM+"\"];"
    escrituranorm(log, nombre)
    #shape=doublecircle
    log = "\tnodeFil[shape=oval,label=\"Filas: " + str(filas) +"\"];"
    escrituranorm(log, nombre)
    log = "\tnodeCol[shape=oval,label=\"Columnas: " + str(columnas) +"\"];"
    escrituranorm(log, nombre)

    log = "\tnodeStart -> nodeName;"
    escrituranorm(log, nombre)
    log = "\tnodeName -> nodeFil;"
    escrituranorm(log, nombre)
    log = "\tnodeName -> nodeCol;"
    escrituranorm(log, nombre)

    nombreNodo = ""
    listaNodos = ListNode()
    listaEnlaces = ListNode()
    toShow = columnas//2
    for c in range(0, columnas):
        init = True
        for f in range(0, filas):
            valor = matriz.dameDatos(f+1, c+1)
            if init:
                nombreNodo = "node" + str(f+1) + str(c+1)
                log = "\tnode" + str(f+1) + str(c+1) + "[label=\"" + str(valor) + "\"];"
                listaNodos.agregaFinal(log)
                #escrituranorm(log, nombre)
                if c == toShow:
                    log = "\tnodeName -> " + nombreNodo + "[lhead=cluster_1];"
                else:
                    log = "\tnodeName -> " + nombreNodo + "[style=invis];"
                listaEnlaces.agregaFinal(log)
                #escrituranorm(log, nombre)
                init = False
            else:
                log = "\tnode" + str(f+1) + str(c+1) + "[label=\"" + str(valor) + "\"];"
                listaNodos.agregaFinal(log)
                #escrituranorm(log, nombre)
                log = "\t" + nombreNodo + " -> node" + str(f+1) + str(c+1) + "[style=invis];"
                listaEnlaces.agregaFinal(log)
                #escrituranorm(log, nombre)
                nombreNodo = "node" + str(f+1) + str(c+1)

    log = "\n\tsubgraph cluster_1 {"                
    escrituranorm(log, nombre)
    log = "\t\tlabel = \"Matriz\";"                
    escrituranorm(log, nombre)
    #listaNodos.reverse()
    aux = listaNodos.fin
    while aux != None:
        escrituranorm("\t" + aux.string1, nombre)
        aux = aux.anterior
    log = "\t}\n"
    escrituranorm(log, nombre)
    #listaEnlaces.reverse()
    aux = listaEnlaces.fin
    while aux != None:
        escrituranorm("\t" + aux.string1, nombre)
        aux = aux.anterior
    log = "}"
    escrituranorm(log, nombre)
    
    generagraf(nombre)
    
def generagraf(nombre):
    di = "dot -Tpng " +  nombre + ".dot -o " + nombre + "-grafo.png"
    #print(di)
    mimetodo(di)
    openGraf(nombre)

    
def escrituranorm(log, nombre):
    file = open(nombre + ".dot", "a")
    file. write(log + "\n")
    file. close()

def openGraf(name):
    di = "start " + name + "-grafo.png"
    try:
        time.sleep(2)
        system (di)
    except:
        print("Error al abrir grafo")


class Node():

    def __init__(self, string1):
        self.string1 = string1
        self.anterior = None
class ListNode():

    def __init__(self):
        self.fin = None

    def estaVacia(self):
        return self.fin == None
    
    def agregaFinal(self, string1):
        if self.estaVacia():
            self.fin = Node(string1)
        else:
            nodeTmp = Node(string1)
            nodeTmp.anterior = self.fin
            self.fin = nodeTmp
