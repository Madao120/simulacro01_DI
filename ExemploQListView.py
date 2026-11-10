import sys
import math

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QListView)
from PyQt6.QtGui import QColor, QPalette

from ModeloTarefas import ModeloTarefas


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("exemplo QListView")

        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        self.listaTarefas = [(True, "Ir o centro DC"), (False, "Ir o ximnasio"), (False, "Ir a compra"),(False, "Outra")]

        self.modelo = ModeloTarefas(self.listaTarefas)

        caixaV = QVBoxLayout()

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.SingleSelection)
        caixaV.addWidget(self.lstTarefas)

        caixaBotons = QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.on_btnBorrar_clicked)
        btnFeito = QPushButton("Feito")
        btnFeito.clicked.connect(self.on_btnFeito_clicked)

        caixaBotons.addWidget(btnBorrar)
        caixaBotons.addWidget(btnFeito)

        caixaV.addLayout(caixaBotons)

        self.txtTarefa = QLineEdit()
        caixaV.addWidget(self.txtTarefa)
        btnEngadir = QPushButton("Engadir Tarefa")
        btnEngadir.clicked.connect(self.on_btnEngadir_clicked)
        caixaBotons.addWidget(btnEngadir)


        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

    def on_btnBorrar_clicked(self):

        pos = self.lstTarefas.selectedIndexes()

        if pos:
            for indice in sorted (pos, reverse = True):
                del(self.modelo.tarefas [indice.row()])

        self.modelo.layoutChanged.emit()
        self.lstTarefas.clearSelection()

    def on_btnFeito_clicked(self):

        pos = self.lstTarefas.selectedIndexes()

        for indice in pos:
            self.listaTarefas[indice.row()]

            for indice in pos:
                fila = indice.row()
                _, texto = self.listaTarefas[fila]

                self.listaTarefas[fila] = (True, texto)

        self.modelo.layoutChanged.emit()
        self.lstTarefas.clearSelection()


    def on_btnEngadir_clicked(self):
        txt = self.txtTarefa.text()

        if txt != "":
            self.listaTarefas.append((False, txt))
            self.txtTarefa.clear()
            self.modelo.layoutChanged.emit()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()