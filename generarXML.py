import xml.etree.ElementTree as ET
from xml.dom import minidom

def formateo(elem):
    rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def generaResultado(name, cols, groups, matrizReduc):
    #print("entra al modulo")
    matriz = ET.Element("matriz", nombre=name, n=str(groups.getGruposTot()), m=str(cols), g=str(groups.getGruposTot()))
    #dato = ET.SubElement(matriz, 'dato')

    aux = matrizReduc.getInicio()
    while True:
        ET.SubElement(matriz, "dato", x=str(aux.getFila()+1), y=str(aux.getColumna()+1)).text = str(aux.getValor())
        if aux.getSiguiente() == matrizReduc.getInicio():
            break
        else:
            aux = aux.getSiguiente()
    #print("simon llegó hasta donde los grupos -------------")
    for i in range(0, groups.getGruposTot()):
        freq = 0
        aux = groups.getInicio()
        while True:
            if aux.getGrupo() == (i + 1):
                freq += 1
            if aux.getSiguiente() == groups.getInicio():
                break
            else:
                aux = aux.getSiguiente()
        ET.SubElement(matriz, "frecuencia", g=str(i+1)).text = str(freq)

    return(formateo(matriz))

    # file = open("C:/Users/Jaime/Desktop/filename.txt", "w+")
    # file. write(prettify(matriz) + os.linesep)

    # file. close()