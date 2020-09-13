#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Producto(object):
    """Clase Producto.

    Una representación básica para representar un producto.

    Atributos:
    Nombre -- tipo string
    precio -- tipo float
    descripcion -- tipo string
    marca -- tipo string
    imagen -- tipo string (url de la imagen)
    código -- tipo string
    """
    def __init__(self,nombre,precio,descripcion,marca,
        imagen,codigo):
        
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.marca = marca
        self.imagen = imagen
        self.codigo = codigo
    
    def __str__(self):
        state = ("Nombre: " + self.nombre + ", Precio: " +
        self.precio + ", Descripción:" + self.descripcion +
        " Marca: " + self.marca + " Imagen: " + self.imagen +
        " Código: " + self.codigo)
        
        return state

    # -----------------------------------------------------
    # métodos setters de la clase.
    # -----------------------------------------------------
    def setNombre(self,nombre):
        self.nombre = nombre

    def setPrecio(self,precio):
        if precio > 0:
            self.precio = precio

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setMarca(self,marca):
        self.marca = marca

    def setImagen(self,imagen):
        self.imagen = imagen

    def setCodigo(self,codigo):
        self.codigo = codigo

    