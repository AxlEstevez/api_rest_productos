<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1">
    <xsl:output method="html"/>
    <xsl:template match="/producto">
        <html lang="es">
        <head>
            <meta charset="UTF-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            <link rel="stylesheet" href="./static/css/main.css"/>
            <title>actualizar producto</title>
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
                    <article class="view">
                        <div id="image">
                            <img src="{imagen/@url}" class="icon" id="{codigoBarras}"/>
                        </div>
                    </article>
                    <div id="info">
                        <form action="/update" method="post" id="for-update">
                            <input type="text" name="id" id="aux" value="{codigoBarras}"/>
                            <br/>
                            <input type="text" name="nombre" value="{nombre}"/>
                            <br/>
                            <input type="text" name="codigo" value="{codigoBarras}"/>
                            <br/>
                            <input type="text" name="precio" value="{precio}"/>
                            <br/>
                            <input type="text" name="descripcion" value="{descripcion}"/>
                            <br/>
                            <input type="text" name="marca" value="{marca}"/>
                            <br/>
                            <input type="text" name="imagen" value="{imagen/@url}"/>
                            <br/>
                            <input type="submit" value="Guardar" id="update"/>
                            <a href="/" id="eliminar">Cancelar</a>
                        </form>
                    </div>
                </section>
            </main>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>