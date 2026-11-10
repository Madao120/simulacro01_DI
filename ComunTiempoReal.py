import sys
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import *
from  PyQt6.QtGui import QColor, QPalette


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro Pokemon")

        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)

        layout_principal = QGridLayout()

        comun = QGridLayout()

        self.cnombre = QLineEdit()
        self.ctipo1 = QRadioButton()
        self.ctipo2 = QRadioButton()

        self.generacion = QComboBox()
        self.generacion.addItems(["1", "2", "3", "4"])

        self.descripcion = QTextEdit()
        self.etapas_evolutivas = QComboBox()
        self.etapas_evolutivas.addItems(["Primera", "Segunda", "Tercera"])

        self.nombre = QLabel("Nombre: ...")
        comun.addWidget(self.nombre, 0, 0)
        comun.addWidget(self.cnombre, 0, 1)

        self.tipo1 = QLabel("Numero de Tipos:")
        comun.addWidget(self.tipo1, 1, 0)
        comun.addWidget(self.ctipo1, 1, 1)
        comun.addWidget(self.ctipo2, 1, 2)

        self.generacion_label = QLabel("Generacion: ...")
        comun.addWidget(self.generacion_label , 3, 0)
        comun.addWidget(self.generacion, 3, 1)

        self.descripcion_label = QLabel("Descripcion: ...")
        comun.addWidget(self.descripcion_label, 4, 0)
        comun.addWidget(self.descripcion, 4, 1)

        self.etapas_evolutivas_label = QLabel("Etapas Evolutivas:...")
        comun.addWidget(self.etapas_evolutivas_label, 5, 0)
        comun.addWidget(self.etapas_evolutivas, 5, 1)


        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar)
        comun.addWidget(self.btn_actualizar, 6, 0, 1, 2)

        widget_comun = QWidget()
        widget_comun.setLayout(comun)

        layout_principal.addWidget(widget_comun, 0, 0)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

    def actualizar(self):
        self.nombre.setText("Nombre: " + self.cnombre.text())
        if self.ctipo1.isChecked():
            self.tipo1.setText("Tipos: 1")
        if self.ctipo2.isChecked():
            self.tipo1.setText("Tipos: 2")
        self.generacion_label.setText("Generacion: " + self.generacion.currentText())
        self.descripcion_label.setText("Descripcion: " + self.descripcion.toPlainText())
        self.etapas_evolutivas_label.setText("Etapas: " + self.etapas_evolutivas.currentText())



if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()