# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bilgiler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
kullaniciListe= ["","","","","","","","",""]
from  openpyxl import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bilgiler(object):
    def setupUi(self, Bilgiler):
        Bilgiler.setObjectName("MainWindow")
        Bilgiler.resize(493, 691)
        self.centralwidget = QtWidgets.QWidget(Bilgiler)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 401, 591))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Resim = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Resim.setObjectName("Resim")
        self.horizontalLayout.addWidget(self.Resim)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelisim = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelisim.setObjectName("labelisim")
        self.verticalLayout.addWidget(self.labelisim)
        self.labelSoyad = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelSoyad.setObjectName("labelSoyad")
        self.verticalLayout.addWidget(self.labelSoyad)
        self.labelTc = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTc.setObjectName("labelTc")
        self.verticalLayout.addWidget(self.labelTc)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.textBrowserBilgiler = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserBilgiler.sizePolicy().hasHeightForWidth())
        self.textBrowserBilgiler.setSizePolicy(sizePolicy)
        self.textBrowserBilgiler.setObjectName("textBrowserBilgiler")
        self.verticalLayout_2.addWidget(self.textBrowserBilgiler)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelDers = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDers.setObjectName("labelDers")
        self.verticalLayout_3.addWidget(self.labelDers)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.labelDogruSayisi = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDogruSayisi.setObjectName("labelDogruSayisi")
        self.horizontalLayout_2.addWidget(self.labelDogruSayisi)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.labelYanlisSayisi = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelYanlisSayisi.setObjectName("labelYanlisSayisi")
        self.horizontalLayout_3.addWidget(self.labelYanlisSayisi)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.labelPuan = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelPuan.setObjectName("labelPuan")
        self.verticalLayout_3.addWidget(self.labelPuan)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        Bilgiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bilgiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 23))
        self.menubar.setObjectName("menubar")
        Bilgiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bilgiler)
        self.statusbar.setObjectName("statusbar")
        Bilgiler.setStatusBar(self.statusbar)
        self.retranslateUi(Bilgiler)
        QtCore.QMetaObject.connectSlotsByName(Bilgiler)
        
#        self.Resim.setPixmap(QtGui.QPixmap("ogrenci1.jpg"))  
        login = load_workbook("Login.xlsx")
        sheet=login.active
        say=0
        for row in sheet.iter_rows(min_row=2, min_col=1, max_row=2, max_col=9):
            for cell in row:
                kullaniciListe[say]=cell.value
                say=say+1
        login.close()
        self.labelisim.setText(str(kullaniciListe[1]))
        self.labelSoyad.setText(str(kullaniciListe[2]))
        self.labelTc.setText(str(kullaniciListe[0]))
        self.Resim.setPixmap(QtGui.QPixmap(str(kullaniciListe[4])))
        print(str(kullaniciListe[4]))
        self.labelDogruSayisi.setText(str(kullaniciListe[5]))
        self.labelYanlisSayisi.setText(str(kullaniciListe[6]))
        self.textBrowserBilgiler.setText(str(kullaniciListe[7]))
        self.labelDers.setText(str(kullaniciListe[8]))
    def retranslateUi(self, Bilgiler):
        _translate = QtCore.QCoreApplication.translate
        Bilgiler.setWindowTitle(_translate("Bilgiler", "Bilgiler"))
        self.labelisim.setText(_translate("Bilgiler", "AAAAAAAAAAAAAAAAAAAAAAAAA"))
        self.labelSoyad.setText(_translate("Bilgiler", "SoyisAAAAAAAAAAAAAAAAAAAim"))
        self.labelTc.setText(_translate("Bilgiler", "Tc"))
        self.labelDers.setText(_translate("Bilgiler", "Test Adı"))
        self.label_6.setText(_translate("Bilgiler", "Doğru Cevap Sayısı:"))
        self.labelDogruSayisi.setText(_translate("Bilgiler", "a"))
        self.label_7.setText(_translate("Bilgiler", "Yanlış Cevap Sayısı:"))
        self.labelYanlisSayisi.setText(_translate("Bilgiler", "a"))
        self.labelPuan.setText(_translate("Bilgiler", "Puan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bilgiler = QtWidgets.QMainWindow()
    ui = Ui_Bilgiler()
    ui.setupUi(Bilgiler)
    Bilgiler.show()
    sys.exit(app.exec_())

