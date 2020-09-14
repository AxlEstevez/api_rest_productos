#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Libreria para la manipulación de Documentos XML
from xml.dom.minidom import Document
from producto import Producto
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element


def prettify(elem):
    string = ET.tostring(elem, 'utf-8','xml')
    re = minidom.parseString(string)
    return re.toprettyxml(indent='\t', newl='\r',encoding="utf-8")

def mkXML(producto):
    """Crea un documento XML producto.
    
    Con la ayuda de la libreria de minidom de xml se crea
    un documento xml de la informacion de un producto.

    Parámetros:
    producto -- objeto producto que contiene la informacion
    del mismo.
    """
    # Se crea un Objeto Document con el cual se creara un XML
    XMLDoc = Document()
    # se crean las etiquetas de los atributos del objeto.
    # producto.
    productoTag = XMLDoc.createElement('producto')
    nombreProdTag = XMLDoc.createElement('nombre')
    precioProdTag = XMLDoc.createElement('precio')
    desProdTag = XMLDoc.createElement('descripcion')
    marcaProdTag = XMLDoc.createElement('marca')
    imagenProdTag = XMLDoc.createElement('imagen')
    codigoProdTag = XMLDoc.createElement('codigoBarras')
    # se agrega los elementos creados al documento XML.
    XMLDoc.appendChild(productoTag) # raiz del documento.
    # se agrega los nodos a la raiz producto.
    productoTag.appendChild(nombreProdTag)
    productoTag.appendChild(precioProdTag)
    productoTag.appendChild(desProdTag)
    productoTag.appendChild(marcaProdTag)
    productoTag.appendChild(imagenProdTag)
    productoTag.appendChild(codigoProdTag)
    # se les asigna el texto a los nodos creados.
    nombreText = XMLDoc.createTextNode(producto.nombre)
    precioText = XMLDoc.createTextNode(str(producto.precio))
    desText = XMLDoc.createTextNode(producto.descripcion)
    marcaText = XMLDoc.createTextNode(producto.marca)
    codigoText = XMLDoc.createTextNode(producto.codigo)
    # se le asigna el atributo y el valor al elemento imagen.
    imagenProdTag.setAttribute('url',producto.imagen)
    # se colocan los nodos de texto a las etiquetas.
    nombreProdTag.appendChild(nombreText)
    precioProdTag.appendChild(precioText)
    desProdTag.appendChild(desText)
    marcaProdTag.appendChild(marcaText)
    codigoProdTag.appendChild(codigoText)
    # se genera el output del documento.
    XMLOutput = XMLDoc.toprettyxml(indent='\t',encoding='UTF-8')
    XMLFile = open('static/xml/producto.xml','wb')
    XMLFile.write(XMLOutput)
    XMLFile.close()

def addAnaquel(XMLnodo,XMLdoc):
    # -----------------------------------------------------
    # Agrega un nuevo nodo "producto" al archivo XML 
    # productos.
    # <anaquel>
    #   <producto>
    #       .....
    #   </producto>
    #   ....
    #   <producto"n">
    #       ....
    #   </producto"n">
    # </anaquel>
    # Parámetros:
    # XMLnodo -- ruta del archivo XMLproducto
    # XMLdoc -- ruta del archivo XMLanaquel
    # -----------------------------------------------------
    # Arbol XML para producto y anaquel
    
    # creamos los objetos "arbol" de los documentos xml
    treeNodo = ET.parse(XMLnodo)
    treeDoc = ET.parse(XMLdoc)
    # se accede a la raíz de cada arbol
    rootNode = treeNodo.getroot()
    rootDoc = treeDoc.getroot()
    # se crea un nuevo nodo "raíz" para agregar a la ríaz
    # del documento "anaquel" (XMLdoc)
    newNode = Element(rootNode.tag)
    # se obtienen los datos (hijos) del nuevo nodo que se
    # desea insertar en el documento anaquel.
    childNode = rootNode.getchildren()

    # ciclo para agregar los elementos hijo al nuevo 
    # elemento creado (newNode)
    for i in range(len(childNode)):
        newNode.append(childNode[i])
    # se agrega el nuevo nodo a documento "anaquel"
    rootDoc.append(newNode)
    output = prettify(rootDoc)
    #print(output)
    XMLFile = open(XMLdoc,'wb')
    XMLFile.write(output)
    XMLFile.close

def getInfo(codigo,xml):
    """Busca un producto en XML BD.
    Busca un producto por su codigo y regresa un objeto de
    tipo producto si encuentra el codigo en BD.

    Parámetros;
    codigo -- Código del producto que se deseá buscar.
    xml -- ruta del archivo donde se buscará el producto.
    """
    tree = ET.parse(xml) # se accesa al arbol XML
    root = tree.getroot() # se obtiene la raíz
    childs = root.getchildren() # se obtiene los nodo producto.
    i = 0
    if codigo != '0':
        # Mientras existan productos en el anaquel
        # se buscara el código del producto solicitado.
        while i < len(childs):
            if codigo == childs[i].find('codigoBarras').text:
                producto = Producto(
                    childs[i].find('nombre').text,
                    childs[i].find('precio').text,
                    childs[i].find('descripcion').text,
                    childs[i].find('marca').text,
                    childs[i].find('imagen').get('url'),
                    childs[i].find('codigoBarras').text
                )
                return producto
                
            
            i+=1
    else:
        print("Código no puede ser 0")
        return None
        
    return None

def restAnaquel(XMLnodo,XMLdoc):
    # -----------------------------------------------------
    # quita un nodo "producto" del archivo XML 
    # productos.
    # <anaquel>
    #   <producto>
    #       .....
    #   </producto>
    #   ....
    #   <producto"n">
    #       ....
    #   </producto"n">
    # </anaquel>
    # Parámetros:
    # XMLnodo -- ruta del archivo XMLproducto
    # XMLdoc -- ruta del archivo XMLanaquel
    # -----------------------------------------------------
    # Arbol XML para producto y anaquel
    
    # creamos los objetos "arbol" de los documentos xml
    treeNodo = ET.parse(XMLnodo)
    treeDoc = ET.parse(XMLdoc)
    # se accede a la raíz de cada arbol
    rootNode = treeNodo.getroot()
    rootDoc = treeDoc.getroot()
    # se obtienen los datos (hijos) del documento al que
    # se le desea quitar el nodo.
    childNode = rootDoc.getchildren()
    code = rootNode.find('codigoBarras').text
    # ciclo para buscar el nodo a quitar.
    for i in range(len(childNode)):
        # si se ecuentra el nodo deseado, se elimina.
        if code == childNode[i].find('codigoBarras').text:
            rootDoc.remove(childNode[i])
    # se agrega el nuevo nodo a documento "anaquel"
    output = prettify(rootDoc)
    #print(output)
    XMLFile = open(XMLdoc,'wb')
    XMLFile.write(output)
    XMLFile.close