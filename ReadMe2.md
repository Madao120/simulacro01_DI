------------------------------------------------------------------------

# 7. Errores habituales que debes evitar

  -----------------------------------------------------------------------
  Error                               Forma correcta / explicación
  ----------------------------------- -----------------------------------
  Olvidar `super().__init__()`        Inicializar la clase padre dentro
                                      de `__init__()`

  Usar `QMainWindow` como si fuera un Crear un `QWidget` central y usar
  `QWidget` normal                    `setCentralWidget()`

  Olvidar asignar el layout           Usar `setLayout()` en el widget
                                      correspondiente

  Usar `addWidget()` para añadir un   Usar `addLayout()`
  layout                              

  Usar `addLayout()` para añadir un   Usar `addWidget()`
  botón                               

  Escribir `connect(mi_funcion())`    Normalmente conectar con
                                      `connect(mi_funcion)`

  Usar `.text()` en un `QTextEdit`    Usar `.toPlainText()`

  Pensar que el primer índice es 1    Los índices de filas, columnas y
                                      páginas empiezan en 0

  Crear un widget como variable local Guardarlo como atributo, por
  y necesitarlo en otro método        ejemplo `self.nombre`

  Olvidar `app.exec()`                Es necesario iniciar el bucle de
                                      eventos
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 8. Chuleta rápida para el examen

## Crear la aplicación

``` python
app = QApplication(sys.argv)
```

## Crear una ventana

``` python
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
```

## Crear el widget central

``` python
central = QWidget()
self.setCentralWidget(central)
```

## Crear layouts

``` python
vbox = QVBoxLayout()
hbox = QHBoxLayout()
grid = QGridLayout()
```

## Añadir widgets y layouts

``` python
grid.addWidget(widget, fila, columna)
grid.addLayout(layout, fila, columna)
```

## Conectar un botón

``` python
boton.clicked.connect(mi_funcion)
```

## Obtener información

``` python
nombre.text()
descripcion.toPlainText()
combo.currentText()
radio.isChecked()
casilla.isChecked()
numero.value()
```

## Cambiar un QLabel

``` python
resultado.setText("Nuevo texto")
```

## Borrar contenido

``` python
nombre.clear()
descripcion.clear()
```

## Crear y utilizar un Stack

``` python
stack = QStackedLayout()
stack.addWidget(pagina1)
stack.addWidget(pagina2)
stack.setCurrentIndex(1)
```

## Conectar un selector con el Stack

``` python
combo.currentIndexChanged.connect(stack.setCurrentIndex)
```

## Finalizar el programa

``` python
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
```

------------------------------------------------------------------------

# 9. Ejercicio de repaso tipo examen

Intenta plantear un programa que cumpla estos requisitos:

1.  Crear una ventana utilizando una clase que herede de `QMainWindow`.
2.  Organizar los elementos mediante `QGridLayout`.
3.  Añadir un `QComboBox` con tres opciones: Datos personales, Estudios
    y Dirección.
4.  Crear un `QStackedLayout` con tres páginas, una para cada opción.
5.  En la primera página, incluir un `QLineEdit` para el nombre y un
    `QLineEdit` para los apellidos.
6.  En la segunda página, incluir un `QComboBox` para seleccionar un
    curso y dos `QRadioButton` para elegir Sí o No.
7.  En la tercera página, incluir un `QTextEdit` para escribir una
    dirección.
8.  Añadir un botón «Mostrar» que recoja los datos y los muestre en un
    `QLabel`.
9.  Añadir un botón «Limpiar» que borre los campos.

**Pistas:**

-   Para cambiar de página:
    `combo.currentIndexChanged.connect(stack.setCurrentIndex)`.
-   Para obtener el nombre: `nombre.text()`.
-   Para obtener la dirección: `direccion.toPlainText()`.
-   Para obtener el curso: `curso.currentText()`.
-   Para comprobar un radio: `radio_si.isChecked()`.
-   Para borrar un campo: `campo.clear()`.

**Consejo de estudio:** aprende primero a crear una ventana y colocar
widgets; después practica cómo obtener sus valores y conectarlos a
funciones. Cuando eso esté claro, `QStackedLayout` será mucho más fácil
de entender.