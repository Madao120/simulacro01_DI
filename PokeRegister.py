import sys
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import *
from  PyQt6.QtGui import QColor, QPalette

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro Pokemon")

        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 600)

        layout_principal = QGridLayout()
        self.categoria = QComboBox()
        self.categoria.addItems(["Comun", "Legendario", "Mítico"])
        self.categoria.setCurrentIndex(-1)

        layout_principal.addWidget(self.categoria, 0, 0)

        comun = QGridLayout()

        self.cnombre = QLineEdit()
        self.ctipo1 = QRadioButton()
        self.ctipo2 = QRadioButton()

        self.generacion = QComboBox()
        self.generacion.addItems(["1", "2", "3", "4"])

        self.descripcion = QTextEdit()
        self.etapas_evolutivas = QComboBox()
        self.etapas_evolutivas.addItems(["Primera", "Segunda", "Tercera"])

        comun.addWidget(QLabel("Nombre:"), 0, 0)
        comun.addWidget(self.cnombre, 0, 1)
        comun.addWidget(QLabel("1 Tipo:"), 1, 0)
        comun.addWidget(self.ctipo1, 1, 1)
        comun.addWidget(QLabel("2 Tipos:"), 2, 0)
        comun.addWidget(self.ctipo2, 2, 1)
        comun.addWidget(QLabel("Generación:"), 3, 0)
        comun.addWidget(self.generacion, 3, 1)
        comun.addWidget(QLabel("Descripción:"), 4, 0)
        comun.addWidget(self.descripcion, 4, 1)
        comun.addWidget(QLabel("Etapas Evolutivas:"), 5, 0)
        comun.addWidget(self.etapas_evolutivas, 5, 1)

        legendario = QGridLayout()
        self.lnombre = QLineEdit()
        self.ltipo1 = QRadioButton()
        self.ltipo2 = QRadioButton()
        self.lgeneracion = QComboBox()
        self.lgeneracion.addItems(["1", "2", "3", "4"])
        self.ldescripcion = QTextEdit()
        self.legendario_mayor = QCheckBox("Legendario Mayor")

        legendario.addWidget(QLabel("Nombre:"), 0, 0)
        legendario.addWidget(self.lnombre, 0, 1)
        legendario.addWidget(QLabel("1 Tipo:"), 1, 0)
        legendario.addWidget(self.ltipo1, 1, 1)
        legendario.addWidget(QLabel("2 Tipos:"), 2, 0 )
        legendario.addWidget(self.ltipo2, 2, 1)
        legendario.addWidget(QLabel("Generación:"), 3, 0)
        legendario.addWidget(self.lgeneracion, 3, 1)
        legendario.addWidget(QLabel("Descripción:"), 4, 0)
        legendario.addWidget(self.ldescripcion, 4, 1)
        legendario.addWidget(self.legendario_mayor, 5, 0, 1, 2)

        mitico = QGridLayout()
        self.mnombre = QLineEdit()
        self.mtipo1 = QRadioButton()
        self.mtipo2 = QRadioButton()
        self.mgeneracion = QComboBox()
        self.mgeneracion.addItems(["1", "2", "3", "4"])
        self.mdescripcion = QTextEdit()
        self.mevento = QCheckBox("Evento")

        mitico.addWidget(QLabel("Nombre:"), 0, 0)
        mitico.addWidget(self.mnombre, 0, 1)
        mitico.addWidget(QLabel("1 Tipo:"), 1, 0)
        mitico.addWidget(self.mtipo1, 1, 1)
        mitico.addWidget(QLabel("2 Tipos:"), 2, 0)
        mitico.addWidget(self.mtipo2, 2, 1)
        mitico.addWidget(QLabel("Generación:"), 3, 0)
        mitico.addWidget(self.mgeneracion, 3, 1)
        mitico.addWidget(QLabel("Descripción:"), 4, 0)
        mitico.addWidget(self.mdescripcion, 4, 1)
        mitico.addWidget(self.mevento, 5, 0, 1, 2)

        self.tarxetas = QStackedLayout()

        self.widget_comun = QWidget()
        self.widget_comun.setLayout(comun)

        self.widget_legendario = QWidget()
        self.widget_legendario.setLayout(legendario)

        self.widget_mitico = QWidget()
        self.widget_mitico.setLayout(mitico)

        self.tarxetas.addWidget(self.widget_comun)
        self.tarxetas.addWidget(self.widget_legendario)
        self.tarxetas.addWidget(self.widget_mitico)

        layout_principal.addLayout(self.tarxetas, 1, 0, 1, 2)

        self.categoria.currentIndexChanged.connect(
            self.tarxetas.setCurrentIndex
        )

        self.tarxetas.setCurrentIndex(0)
        self.categoria.setCurrentIndex(0)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        self.enviar = QPushButton("Enviar")
        self.enviar.clicked.connect(self.borrar_todo)
        layout_principal.addWidget(self.enviar, 6, 0, 1, 2)

    def cambiar_formulario(self, indice):
        if indice >= 0:
            self.tarxetas.setCurrentIndex(indice)

    def desmarcar_radio_buttons(self, *botones):
        for boton in botones:
            boton.setAutoExclusive(False)

        for boton in botones:
            boton.setChecked(False)

        for boton in botones:
            boton.setAutoExclusive(True)

    def borrar_todo(self):
        self.cnombre.clear()
        self.desmarcar_radio_buttons(self.ctipo1, self.ctipo2)
        self.generacion.setCurrentIndex(-1)
        self.descripcion.clear()
        self.etapas_evolutivas.setCurrentIndex(-1)

        self.lnombre.clear()
        self.desmarcar_radio_buttons(self.ltipo1, self.ltipo2)
        self.lgeneracion.setCurrentIndex(-1)
        self.ldescripcion.clear()
        self.legendario_mayor.setChecked(False)

        self.mnombre.clear()
        self.desmarcar_radio_buttons(self.mtipo1, self.mtipo2)
        self.mgeneracion.setCurrentIndex(-1)
        self.mdescripcion.clear()
        self.mevento.setChecked(False)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()