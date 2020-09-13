<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1">
    <xsl:output method="html"/>
    <xsl:template match="/producto">
        <html lang="es">
            <head>
                <meta charset="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <link rel="stylesheet" href="./static/css/main.css"/>
                <title>Inicio</title>
            </head>
            <body>
                <header>
                    <div class="contenedor">
                        <nav class="menu">
                            <a href="/">inicio</a>
                            <a href="/add">Agregar</a>
                        </nav>
                    </div>
                </header>
                <main>
                    <section id="product-view">
                        <article id="view">
                            <div id="image">
                                <img src="{imagen/@url}" class="icon" id="{codigoBarras}"/>
                            </div>
                            <div id="info">
                                <form action="/delete" method="POST">
                                    <input type="text" name="codigo" value="{codigoBarras}" id="aux"/>
                                    <table id="info-view">
                                        <tr>
                                            <th>Nombre: </th>
                                            <td>
                                                <xsl:value-of select="nombre"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <th>Precio: </th>
                                            <td>
                                                <xsl:value-of select="precio"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <th>Descripción: </th>
                                            <td>
                                                <xsl:value-of select="descripcion"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <th>Marca: </th>
                                            <td>
                                                <xsl:value-of select="marca"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <th>Código de barras: </th>
                                            <td>
                                                <xsl:value-of select="codigoBarras"/>
                                            </td>
                                        </tr>
                                    </table>
                                    <input type="submit" value="Eliminar" id="eliminar"/>
                                    <a href="/update" id="update">Modificar</a>
                                </form>
                            </div>
                        </article>
                    </section>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>