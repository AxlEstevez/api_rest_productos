<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1">
    <xsl:output method="html"/>
    <xsl:template match="/">
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
                    <section id="anaquel">
                        <h1 class="titulo">Productos</h1>
                        <xsl:for-each select="anaquel/producto">
                            <article class="productos">
                                <form action="/getProducto" method="POST">
                                    <input style="display: none;" type="text" value="{codigoBarras}" name="codigo"/>
                                    <button class="boton">
                                        <img src="{imagen/@url}" class="icon"/>
                                    </button>
                                </form>
                            </article>
                        </xsl:for-each>
                    </section>
                </main>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>