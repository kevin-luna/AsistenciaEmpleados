# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VentanaInicioSesion.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaInicioSesion(object):
    def setupUi(self, VentanaInicioSesion):
        VentanaInicioSesion.setObjectName("VentanaInicioSesion")
        VentanaInicioSesion.resize(400, 400)
        VentanaInicioSesion.setMinimumSize(QtCore.QSize(300, 300))
        VentanaInicioSesion.setMaximumSize(QtCore.QSize(400, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(VentanaInicioSesion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(VentanaInicioSesion)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("media/jeb.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.panelNorte = QtWidgets.QWidget(VentanaInicioSesion)
        self.panelNorte.setObjectName("panelNorte")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.panelNorte)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.etiquetaContrasena = QtWidgets.QLabel(self.panelNorte)
        self.etiquetaContrasena.setObjectName("etiquetaContrasena")
        self.gridLayout_2.addWidget(self.etiquetaContrasena, 3, 0, 1, 1)
        self.etiquetaUsuario = QtWidgets.QLabel(self.panelNorte)
        self.etiquetaUsuario.setObjectName("etiquetaUsuario")
        self.gridLayout_2.addWidget(self.etiquetaUsuario, 1, 0, 1, 1)
        self.campoContrasena = QtWidgets.QLineEdit(self.panelNorte)
        self.campoContrasena.setStyleSheet("QLineEdit{\n"
"    border-radius: 10px;\n"
"    padding: 8px 20px;\n"
"    border: 2px solid #161d41;\n"
"}\n"
"")
        self.campoContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campoContrasena.setObjectName("campoContrasena")
        self.gridLayout_2.addWidget(self.campoContrasena, 4, 0, 1, 1)
        self.campoUsuario = QtWidgets.QLineEdit(self.panelNorte)
        self.campoUsuario.setStyleSheet("QLineEdit{\n"
"    border-radius: 10px;\n"
"    padding: 8px 20px;\n"
"    border: 2px solid #161d41;\n"
"}\n"
"")
        self.campoUsuario.setObjectName("campoUsuario")
        self.gridLayout_2.addWidget(self.campoUsuario, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.panelNorte)
        self.panelSur = QtWidgets.QWidget(VentanaInicioSesion)
        self.panelSur.setObjectName("panelSur")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.panelSur)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.botonIniciarSesion = QtWidgets.QPushButton(self.panelSur)
        self.botonIniciarSesion.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Redondea los bordes del botón */\n"
"    background-color: #615298; /* Color de fondo en estado base */\n"
"    color: white; /* Color del texto */\n"
"    padding: 10px 20px; /* Espaciado interno */\n"
"    border: 2px solid #161d41; /* Borde del botón */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9769bb; /* Color de fondo cuando el mouse está encima */\n"
"    border: 2px solid #5266d3; /* Color del borde cuando el mouse está encima */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #36356c; /* Color de fondo cuando el botón está presionado */\n"
"    border: 2px solid #161d41; /* Color del borde cuando el botón está presionado */\n"
"}")
        self.botonIniciarSesion.setObjectName("botonIniciarSesion")
        self.gridLayout_3.addWidget(self.botonIniciarSesion, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.panelSur)

        self.retranslateUi(VentanaInicioSesion)
        QtCore.QMetaObject.connectSlotsByName(VentanaInicioSesion)

    def retranslateUi(self, VentanaInicioSesion):
        _translate = QtCore.QCoreApplication.translate
        VentanaInicioSesion.setWindowTitle(_translate("VentanaInicioSesion", "JEB - Iniciar sesión"))
        self.etiquetaContrasena.setText(_translate("VentanaInicioSesion", "Contraseña:"))
        self.etiquetaUsuario.setText(_translate("VentanaInicioSesion", "Usuario:"))
        self.botonIniciarSesion.setText(_translate("VentanaInicioSesion", "Iniciar sesión"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaInicioSesion = QtWidgets.QWidget()
    ui = Ui_VentanaInicioSesion()
    ui.setupUi(VentanaInicioSesion)
    VentanaInicioSesion.show()
    sys.exit(app.exec_())
