# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_grafica.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 309)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:#fff;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 170, 75, 24))
        self.pushButton.setStyleSheet(u"background-color:#ccc;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 49, 151))
        self.label.setPixmap(QPixmap(u"img_1.png"))
        self.lineEdit_x_1 = QLineEdit(self.centralwidget)
        self.lineEdit_x_1.setObjectName(u"lineEdit_x_1")
        self.lineEdit_x_1.setGeometry(QRect(100, 50, 41, 22))
        self.lineEdit_x_1.setStyleSheet(u"background-color:#ccc;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 50, 31, 21))
        self.label_2.setStyleSheet(u"font: 700 12pt \"Arial\";")
        self.lineEdit_y_1 = QLineEdit(self.centralwidget)
        self.lineEdit_y_1.setObjectName(u"lineEdit_y_1")
        self.lineEdit_y_1.setGeometry(QRect(190, 50, 41, 22))
        self.lineEdit_y_1.setStyleSheet(u"background-color:#ccc;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 50, 31, 21))
        self.label_3.setStyleSheet(u"font: 700 12pt \"Arial\";")
        self.lineEdit_eq_1 = QLineEdit(self.centralwidget)
        self.lineEdit_eq_1.setObjectName(u"lineEdit_eq_1")
        self.lineEdit_eq_1.setGeometry(QRect(290, 50, 41, 22))
        self.lineEdit_eq_1.setStyleSheet(u"background-color:#ccc;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 100, 31, 21))
        self.label_4.setStyleSheet(u"font: 700 12pt \"Arial\";")
        self.lineEdit_x_2 = QLineEdit(self.centralwidget)
        self.lineEdit_x_2.setObjectName(u"lineEdit_x_2")
        self.lineEdit_x_2.setGeometry(QRect(100, 100, 41, 22))
        self.lineEdit_x_2.setStyleSheet(u"background-color:#ccc;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 100, 31, 21))
        self.label_5.setStyleSheet(u"font: 700 12pt \"Arial\";")
        self.lineEdit_eq_2 = QLineEdit(self.centralwidget)
        self.lineEdit_eq_2.setObjectName(u"lineEdit_eq_2")
        self.lineEdit_eq_2.setGeometry(QRect(290, 100, 41, 22))
        self.lineEdit_eq_2.setStyleSheet(u"background-color:#ccc;")
        self.lineEdit_y_2 = QLineEdit(self.centralwidget)
        self.lineEdit_y_2.setObjectName(u"lineEdit_y_2")
        self.lineEdit_y_2.setGeometry(QRect(190, 100, 41, 22))
        self.lineEdit_y_2.setStyleSheet(u"background-color:#ccc;")
        self.label_resposta = QLabel(self.centralwidget)
        self.label_resposta.setObjectName(u"label_resposta")
        self.label_resposta.setGeometry(QRect(50, 210, 301, 21))
        self.label_resposta.setStyleSheet(u"font: 9pt \"Arial\";")
        self.label_resposta_2 = QLabel(self.centralwidget)
        self.label_resposta_2.setObjectName(u"label_resposta_2")
        self.label_resposta_2.setGeometry(QRect(50, 250, 301, 21))
        self.label_resposta_2.setStyleSheet(u"font: 9pt \"Arial\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X   +", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y   =", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y   =", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X   +", None))
        self.label_resposta.setText("")
        self.label_resposta_2.setText("")
    # retranslateUi

