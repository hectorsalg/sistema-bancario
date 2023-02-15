# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaconta.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaConta(object):
    """
    Essa classe representa a tela Conta
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelConta = QtWidgets.QLabel(self.centralwidget)
        self.labelConta.setGeometry(QtCore.QRect(330, 40, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelConta.setFont(font)
        self.labelConta.setObjectName("labelConta")
        self.btnDepositar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDepositar.setGeometry(QtCore.QRect(250, 200, 91, 31))
        self.btnDepositar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDepositar.setObjectName("btnDepositar")
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setGeometry(QtCore.QRect(40, 450, 91, 31))
        self.btnSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSair.setObjectName("btnSair")
        self.btnSacar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSacar.setGeometry(QtCore.QRect(600, 200, 91, 31))
        self.btnSacar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSacar.setObjectName("btnSacar")
        self.btnTransferir = QtWidgets.QPushButton(self.centralwidget)
        self.btnTransferir.setGeometry(QtCore.QRect(250, 300, 91, 31))
        self.btnTransferir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTransferir.setObjectName("btnTransferir")
        self.btnExtrato = QtWidgets.QPushButton(self.centralwidget)
        self.btnExtrato.setGeometry(QtCore.QRect(600, 300, 91, 31))
        self.btnExtrato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExtrato.setObjectName("btnExtrato")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(40, 400, 91, 31))
        self.btnVoltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVoltar.setObjectName("btnVoltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelConta.setText(_translate("MainWindow", "Sua Conta"))
        self.btnDepositar.setText(_translate("MainWindow", "Depositar"))
        self.btnSair.setText(_translate("MainWindow", "Sair"))
        self.btnSacar.setText(_translate("MainWindow", "Sacar"))
        self.btnTransferir.setText(_translate("MainWindow", "Transferir"))
        self.btnExtrato.setText(_translate("MainWindow", "Extrato"))
        self.btnVoltar.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaConta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
