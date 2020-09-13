#!/usr/bin/python3
#-*- coding: utf-8 -*-

# importaciones necesarias para poder correr python del lado
# del servidor
from flask import Flask, render_template, redirect, request
import lxml # Se usara para validad documentos xml con su xsd.
import xmlschema # otra libreria para validad xml
# Modulos para poder acceder a los elementos del archivo XML.
import xml.etree.ElementTree as Et
 # Métodos propios para taratar xml. 
from xmlMod import *
# ---------------------------------------------------------
# Se importa la libreria producto solo con el fin
# de crear objetos de tipo producto y tratar de manera
# más fácil la información.
from producto import Producto
# ---------------------------------------------------------
# métodos especificos para este proyecto.
from modules import *

app = Flask(__name__) # Se crea un Objeto flask para poder
# manejar datos y rutas con python desde el servidor.
xml = 'static/xml/productos.xml'# ruta al archivo xml
xsd = 'static/xml/productos.xsd'# ruta al archivo xsd
xslt = 'static/xml/productos.xsl'# ruta al archivo xsl
# ruta al Schema del producto
# ---------------------------------------------------------
# Este Schema se usa para validar que la información 
# enviada por el usuario corresponda a las reglas del xml
# que se usa como "base de datos" para alacenaje de 
# productos.
# ---------------------------------------------------------
productoSchema = 'static/xml/producto.xsd'
productoXML = 'static/xml/producto.xml'


@app.route('/')
def index():
    # ruta del archivo html donde se hará la transformacion
    html = 'templates/index.html'
    # se verifica que el archivo xml este bien formado.
    if validateXML(xml,xsd):
        # se verifica si exiten productos en el archvo xml
        if countElements(xml) > 0:
            # si exite al menos un producto se genera la 
            # vista del archivo xml.
            mkhtml(xslt,xml,html)
        else:
        # Si no existe ningún producto se direcciona a la
        # página inical con un mensaje para "notificar" que
        # no existen productos aún.
            return render_template(
                'indexAux.html',
                message = "Sin elementos agregados"
            )
    else:
        # si el archivo xml esta corrompido o no es valido
        # con su schema correspondiente se le notifica
        # al usuario que hubo un problema al procesar la
        # petición de la página.
        return render_template(
                'indexAux.html',
                message = "Error en al procesar petición."
            )
    return render_template('index.html')

@app.route('/add')
def rutaAgregar():
    return render_template('agrega.html')

@app.route('/add', methods=['POST'])
def agregaProducto():
    if request.method == 'POST':
        # se crea un Objeto de tipo Producto
        # para poder generar el xml correspondiente a
        # un producto y validarlo.
        producto = Producto(
            request.form['nombre'],
            request.form['precio'],
            request.form['descripcion'],
            request.form['marca'],
            request.form['imagen'],
            request.form['codigo']
        )
        # se crea el archivo xml del producto.
        mkXML(producto)
        # se valida que el xml corresponda con lo que se
        # espera recibir.
        if validateXML(productoXML,productoSchema):
            addAnaquel(productoXML,xml)
            if validateXML(xml,xsd):
                return redirect('/')
            else:
                return render_template(
                    'agrega.html',
                    message = 'Erro en la petición'
                )
        else:
            return render_template('agrega.html')

@app.route('/getProducto',methods=['POST'])
def getProducto():
    xsltProducto = 'static/xml/producto.xsl'
    xmlProducto = 'static/xml/producto.xml'
    htmlProduc = 'templates/producto.html'
    if request.method == 'POST':
        # se obtiene los datos del producto que el usuario
        # pide..
        codigo = request.form['codigo']
        producto = getInfo(codigo,xml)
        if producto != None:
            mkXML(producto)
            mkhtml(xsltProducto,xmlProducto,htmlProduc)
            return render_template('producto.html')
        else:
            return render_template(
                'indexAux.html',
                error = 'Error en la petición'
                )
    else:
        return render_template(
            'indexAux.html',
            error = 'Error en la petición'
        )

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        # se elimina el nodo del archivo xml
        restAnaquel(productoXML,xml)
        return redirect('/')
    else:
        return render_template(
            'indexAux.html',
            error = 'error al procesar petición'
        )

@app.route('/update')
def update():
    xsltUp = 'static/xml/productoUpdate.xsl'
    xmlUp = 'static/xml/producto.xml'
    htmlUp = 'templates/update.html'
    mkhtml(xsltUp,xmlUp,htmlUp)
    return render_template('update.html')

@app.route('/update', methods=['POST'])
def updateProducto():
    if request.method == 'POST':
        # Aux como su nombre lo indica es una variable
        # auxiliar en caso que el usuario modifique el
        # código de barras, con esto se tiene un "registro"
        # para posteriormente modificar el producto en el 
        # anaquel.
        codigo = request.form['codigo']
        
        aux = 'static/xml/producto.xml'
        restAnaquel(aux,xml)
        newProdcuto = Producto(
            request.form['nombre'],
            request.form['precio'],
            request.form['descripcion'],
            request.form['marca'],
            request.form['imagen'],
            request.form['codigo']
        )
        mkXML(newProdcuto)
        if validateXML(aux,productoSchema):
            addAnaquel(aux,xml)
        else:
            return render_template(
                'indexAux.html',
                message = 'Error al procesar la petición.'
            )
        return redirect('/')
    else:
        return render_template(
            'indexAux.html',
            message = 'Error al procesar la petición.'
        )

if __name__ == "__main__":
    app.run(port=5000,debug=True)