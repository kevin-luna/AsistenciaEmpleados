# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VentanaControlAsistencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaControlAsistencia(object):
    def setupUi(self, VentanaControlAsistencia):
        VentanaControlAsistencia.setObjectName("VentanaControlAsistencia")
        VentanaControlAsistencia.resize(456, 344)
        self.verticalLayout = QtWidgets.QVBoxLayout(VentanaControlAsistencia)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botonRegistrarLlegada = QtWidgets.QPushButton(VentanaControlAsistencia)
        self.botonRegistrarLlegada.setStyleSheet("QPushButton {\n"
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
        self.botonRegistrarLlegada.setObjectName("botonRegistrarLlegada")
        self.verticalLayout.addWidget(self.botonRegistrarLlegada)
        self.botonRegistrarSalida = QtWidgets.QPushButton(VentanaControlAsistencia)
        self.botonRegistrarSalida.setStyleSheet("QPushButton {\n"
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
        self.botonRegistrarSalida.setObjectName("botonRegistrarSalida")
        self.verticalLayout.addWidget(self.botonRegistrarSalida)
        self.botonSalir = QtWidgets.QPushButton(VentanaControlAsistencia)
        self.botonSalir.setStyleSheet("QPushButton {\n"
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
        self.botonSalir.setObjectName("botonSalir")
        self.verticalLayout.addWidget(self.botonSalir)

        self.retranslateUi(VentanaControlAsistencia)
        QtCore.QMetaObject.connectSlotsByName(VentanaControlAsistencia)

    def retranslateUi(self, VentanaControlAsistencia):
        _translate = QtCore.QCoreApplication.translate
        VentanaControlAsistencia.setWindowTitle(_translate("VentanaControlAsistencia", "JEB - Control de asistencia"))
        self.botonRegistrarLlegada.setText(_translate("VentanaControlAsistencia", "Registrar llegada"))
        self.botonRegistrarSalida.setText(_translate("VentanaControlAsistencia", "Registrar salida"))
        self.botonSalir.setText(_translate("VentanaControlAsistencia", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaControlAsistencia = QtWidgets.QWidget()
    ui = Ui_VentanaControlAsistencia()
    ui.setupUi(VentanaControlAsistencia)
    VentanaControlAsistencia.show()
    sys.exit(app.exec_())
