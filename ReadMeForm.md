# Formulario y resultados con `QStackedLayout` en PyQt6

Este programa utiliza **`QStackedLayout` de verdad** para alternar entre dos páginas:
- Índice `0`: formulario.
- Índice `1`: página con los datos introducidos.

Al pulsar **Enviar**, se leen los campos, se actualiza un `QLabel` de la segunda página y se cambia a esa página con `setCurrentIndex(1)`. El botón **Volver** regresa al formulario con `setCurrentIndex(0)`.

## Código completo

```python
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QStackedLayout,
    QLabel, QLineEdit, QCheckBox,
    QRadioButton, QComboBox, QPushButton
)


class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario con QStackedLayout")
        self.setFixedSize(400, 300)

        # QMainWindow necesita un widget central.
        central = QWidget()
        self.setCentralWidget(central)

        # ESTE ES EL QSTACKEDLAYOUT:
        # contendrá las dos páginas y mostrará una cada vez.
        self.stack = QStackedLayout()
        central.setLayout(self.stack)

        # Crear las dos páginas.
        self.crear_formulario()
        self.crear_resultados()

        # Añadir los QWidget al QStackedLayout.
        # El orden determina sus índices: formulario=0, resultados=1.
        self.stack.addWidget(self.pagina_formulario)
        self.stack.addWidget(self.pagina_resultados)

        # Empezar mostrando el formulario.
        self.stack.setCurrentIndex(0)

    def crear_formulario(self):
        self.pagina_formulario = QWidget()
        grid = QGridLayout()

        # Nombre
        grid.addWidget(QLabel("Nombre:"), 0, 0)
        self.nombre = QLineEdit()
        grid.addWidget(self.nombre, 0, 1)

        # Checkbox: mayoría de edad
        self.mayor_edad = QCheckBox("Soy mayor de edad")
        grid.addWidget(self.mayor_edad, 1, 0, 1, 2)

        # Radio buttons: hombre o mujer
        grid.addWidget(QLabel("Sexo:"), 2, 0)
        self.hombre = QRadioButton("Hombre")
        self.mujer = QRadioButton("Mujer")
        grid.addWidget(self.hombre, 2, 1)
        grid.addWidget(self.mujer, 3, 1)

        # Select de provincias
        grid.addWidget(QLabel("Provincia:"), 4, 0)
        self.provincia = QComboBox()
        self.provincia.addItems([
            "Pontevedra", "A Coruña", "Ourense", "Lugo"
        ])
        grid.addWidget(self.provincia, 4, 1)

        # Botón Enviar
        enviar = QPushButton("Enviar")
        grid.addWidget(enviar, 5, 0, 1, 2)

        # Al pulsarlo, ejecuta la función mostrar_resultados.
        enviar.clicked.connect(self.mostrar_resultados)

        self.pagina_formulario.setLayout(grid)

    def crear_resultados(self):
        self.pagina_resultados = QWidget()
        grid = QGridLayout()

        grid.addWidget(QLabel("Datos introducidos:"), 0, 0)

        # Este QLabel mostrará los datos del formulario.
        self.resultado = QLabel()
        grid.addWidget(self.resultado, 1, 0)

        volver = QPushButton("Volver al formulario")
        grid.addWidget(volver, 2, 0)

        volver.clicked.connect(self.volver)

        self.pagina_resultados.setLayout(grid)

    def mostrar_resultados(self):
        # Obtener el contenido de cada widget.
        nombre = self.nombre.text()

        if self.mayor_edad.isChecked():
            edad = "Sí"
        else:
            edad = "No"

        if self.hombre.isChecked():
            sexo = "Hombre"
        elif self.mujer.isChecked():
            sexo = "Mujer"
        else:
            sexo = "No seleccionado"

        provincia = self.provincia.currentText()

        # Escribir los datos en el QLabel de la segunda página.
        self.resultado.setText(
            f"Nombre: {nombre}\n"
            f"Mayor de edad: {edad}\n"
            f"Sexo: {sexo}\n"
            f"Provincia: {provincia}"
        )

        # CAMBIAR DE PÁGINA USANDO QSTACKEDLAYOUT.
        self.stack.setCurrentIndex(1)

    def volver(self):
        # Volver a la página del formulario.
        self.stack.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
```

## Cómo reconocer el uso de `QStackedLayout`

Estas son las líneas esenciales del cambio de páginas:

```python
# 1. Crear el Stack
self.stack = QStackedLayout()
central.setLayout(self.stack)

# 2. Añadir las páginas
self.stack.addWidget(self.pagina_formulario)  # índice 0
self.stack.addWidget(self.pagina_resultados)  # índice 1

# 3. Mostrar el formulario al iniciar
self.stack.setCurrentIndex(0)

# 4. Mostrar resultados al pulsar Enviar
self.stack.setCurrentIndex(1)

# 5. Volver al formulario
self.stack.setCurrentIndex(0)
```

**No se utiliza `show()` ni `hide()` para alternar las páginas.** El `QStackedLayout` administra qué página está visible.

## Métodos utilizados en el formulario

| Widget | Obtener el dato |
|---|---|
| `QLineEdit` | `self.nombre.text()` |
| `QCheckBox` | `self.mayor_edad.isChecked()` |
| `QRadioButton` | `self.hombre.isChecked()` |
| `QComboBox` | `self.provincia.currentText()` |
| `QLabel` | `self.resultado.setText("...")` |

## Orden para estudiarlo

1. Crear `QMainWindow` y el widget central.
2. Crear `QStackedLayout` y asignarlo al widget central.
3. Crear cada página como un `QWidget`.
4. Crear un `QGridLayout` dentro de cada página.
5. Añadir los widgets a sus respectivos grids.
6. Añadir las páginas al Stack con `addWidget()`.
7. Conectar Enviar con la función que recoge y muestra los datos.
8. Cambiar a la página de resultados con `setCurrentIndex(1)`.
