
from PyQt5 import QtCore, QtGui, QtWidgets
import przegladanie
import os
import pandas as pd
import znajdz_puste_foldery
import usun_z_pliku

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 450, 31))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QLabel:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"font-size:16px;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.label.setText( os.getcwd())
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 251, 31))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QLabel:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"font-size:16px;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(38, 120, 431, 31))
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QComboBox:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"font-size:16px;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")

        self.comboBox_dysk = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dysk.setGeometry(QtCore.QRect(700, 20, 50, 30))
        self.comboBox_dysk.setStyleSheet("QComboBox{\n"
                                    "background-color: rgb(75, 255, 249);\n"
                                    "}\n"
                                    "QComboBox:hover{\n"
                                    "background-color: rgb(75, 255, 249);\n"
                                    "border: 2px solid rgb(255,0,0);\n"
                                    "font-size:16px;\n"
                                    "}\n"
                                    "")
        self.comboBox_dysk.setObjectName("comboBox_dysk")
        

        self.pushButton_dysk = QtWidgets.QPushButton(self.centralwidget,
                                                     clicked=lambda: self.zmiana_dysku(self.comboBox_dysk.currentText()))
        self.pushButton_dysk.setGeometry(QtCore.QRect(700, 60, 50, 30))
        self.pushButton_dysk.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(75, 255, 249);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgb(75, 255, 249);\n"
                                         "border: 2px solid rgb(255,0,0);\n"
                                         "font-size:16px;\n"
                                         "}\n"
                                         "")
        self.pushButton_dysk.setObjectName("pushButton_dysk")

        # ############### przyciski
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked=lambda: self.duplikaty() )
        self.pushButton_4.setGeometry(QtCore.QRect(40, 480, 84, 35))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 18px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.usun_duplikaty())
        self.pushButton_4_4.setGeometry(QtCore.QRect(40, 520, 84, 35))
        self.pushButton_4_4.setStyleSheet("QPushButton{\n"
                                   "alignment: center;\n"
                                   "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(75, 255, 249);\n"
                                   "font-size: 18px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(255, 25, 29);\n"
                                   "border: 2px solid rgb(255,0,0);\n"
                                   "font-size: 20px;\n"
                                   "}\n"
                                   "")
        self.pushButton_4_4.setObjectName("label_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.kopia_w_nazwie(self.label.text()))
        self.pushButton_5.setGeometry(QtCore.QRect(129, 480, 84, 35))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 18px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.usun_elemety_z_kopia_w_nazwie())
        self.pushButton_5_5.setGeometry(QtCore.QRect(129, 520, 84, 35))
        self.pushButton_5_5.setStyleSheet("QPushButton{\n"
                                   # "    text-decoration: underline;\n"
                                   "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(75, 255, 249);\n"
                                   "font-size: 18px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(255, 25, 29);\n"
                                   "border: 2px solid rgb(255,0,0);\n"
                                   "font-size: 20px;\n"
                                   "}\n"
                                   "")
        self.pushButton_5_5.setObjectName("label_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked= lambda: self.puste_foldery(self.label.text()))
        self.pushButton_6.setGeometry(QtCore.QRect(218, 480, 84, 35))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 14px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 16px;\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.usun_puste_foldery())
        self.pushButton_6_6.setGeometry(QtCore.QRect(218, 520, 84, 35))
        self.pushButton_6_6.setStyleSheet("QPushButton{\n"
                                   "    text-decoration: underline;\n"
                                   "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(75, 255, 249);\n"
                                   "font-size: 18px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(255, 25, 29);\n"
                                   "border: 2px solid rgb(255,0,0);\n"
                                   "font-size: 20px;\n"
                                   "}\n"
                                   "")
        self.pushButton_6_6.setObjectName("label_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(307, 480, 84, 35))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 18px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "")
        self.pushButton_7.setObjectName("pushButton_7")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(307, 520, 84, 35))
        self.label_7.setStyleSheet("QLabel{\n"
                                   "    text-decoration: underline;\n"
                                   "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(75, 255, 249);\n"
                                   "font-size: 18px;\n"
                                   "}\n"
                                   "QLabel:hover{\n"
                                   "background-color: rgb(255, 25, 29);\n"
                                   "border: 2px solid rgb(255,0,0);\n"
                                   "font-size: 20px;\n"
                                   "}\n"
                                   "")
        self.label_7.setObjectName("label_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(396, 480, 84, 35))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 18px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "")
        self.pushButton_8.setObjectName("pushButton_8")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(396, 520, 84, 35))
        self.label_8.setStyleSheet("QLabel{\n"
                                   "    text-decoration: underline;\n"
                                   "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(75, 255, 249);\n"
                                   "font-size: 18px;\n"
                                   "}\n"
                                   "QLabel:hover{\n"
                                   "background-color: rgb(255, 25, 29);\n"
                                   "border: 2px solid rgb(255,0,0);\n"
                                   "font-size: 20px;\n"
                                   "}\n"
                                   "")
        self.label_8.setObjectName("label_8")

        #########################################################
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked=lambda: self.przejdz_do_folderu(self.comboBox.currentText()))
        self.pushButton_3.setGeometry(QtCore.QRect(490, 120, 150, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    text-decoration: underline;\n"
                                        "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(75, 255, 249);\n"
                                        "font-size: 18px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 25, 29);\n"
                                        "border: 2px solid rgb(255,0,0);\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.pokaz1( self.comboBox.currentText()))
        self.pushButton_2.setGeometry(QtCore.QRect(490, 180, 150, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    text-decoration: underline;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 255, 249);\n"
"font-size: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 25, 29);\n"
"border: 2px solid rgb(255,0,0);\n"
"font-size: 20px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 170, 431, 301))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"background-color: rgb(208, 208, 208)\n"
"}\n"
"QTextBrowser:hover{\n"
"background-color: rgb(198, 198, 198);\n"
"border: 2px solid rgb(255,0,0);\n"
"}\n"
"")
        self.textBrowser.setObjectName("textBrowser")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(490, 230, 91, 41))
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QLCDNumber:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"}\n"
"")
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(490, 290, 91, 41))
        self.lcdNumber_2.setStyleSheet("QLCDNumber{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QLCDNumber:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"}\n"
"")
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(490, 350, 91, 41))
        self.lcdNumber_3.setStyleSheet("QLCDNumber{\n"
"background-color: rgb(75, 255, 249);\n"
"}\n"
"QLCDNumber:hover{\n"
"background-color: rgb(75, 255, 249);\n"
"border: 2px solid rgb(255,0,0);\n"
"}\n"
"")
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 410, 131, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    text-decoration: underline;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 255, 249);\n"
"font-size: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 25, 29);\n"
"border: 2px solid rgb(255,0,0);\n"
"font-size: 22px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def combo(self, sciezka  ):
        # sciezka_ = os.path.abspath( self.comboBox.currentText() )
        return self.comboBox.addItems( przegladanie.folder(sciezka)[0])

    def pokaz1(self, pressed ): # NIE PRZEKAZUJE CALEJ SCIEZKI !!!!!!!
        if os.path.isdir( self.comboBox.currentText() ): # NIE DZIALA LCD DLA FOLDERO
            self.textBrowser.setText(przegladanie.trescfolderu(self.comboBox.currentText()))
            self.lcdNumber_2.display(przegladanie.policz_pliki( self.comboBox.currentText() ))
        else:
            self.textBrowser.setText( przegladanie.trescpliku(self.comboBox.currentText()))

    def gdzie_jestem(self, sciezka = os.getcwd()):
        return sciezka

    def przejdz_do_folderu(self,pressed ):
        if os.path.isdir( self.comboBox.currentText() ) and pressed == '.\\':
            folder = os.path.abspath(pressed)
            parent = os.path.join(folder, os.pardir)
            os.chdir(parent)
            self.label.setText( os.getcwd() )
            self.lcdNumber.display(przegladanie.policz_foldery(self.label.text()))
            self.lcdNumber_2.display(przegladanie.policz_pliki(self.label.text()))

        if os.path.isdir( self.comboBox.currentText() ):
            folder = os.path.abspath(pressed)
            os.chdir(folder)
            self.comboBox.clear()
            self.label.setText(os.getcwd())
            self.comboBox.addItems( przegladanie.folder( self.label.text())[0])
            self.lcdNumber.display(przegladanie.policz_foldery(self.label.text()))
            self.lcdNumber_2.display(przegladanie.policz_pliki(self.label.text()))

    def zmiana_dysku(self, pressed):
        print(  przegladanie.folder(self.comboBox_dysk.currentText())[0])
        self.przejdz_do_folderu(pressed)
        
    def duplikaty(self):
        self.textBrowser.setText(f'duplikaty\n , {self.label.currency()}')
        self.duplikaty_do_pliku()

    def duplikaty_do_pliku(self):
        pass
        # self.textBrowser.setText(' duplikaty do pliku ')

    def kopia_w_nazwie(self,pressed):
        # print( f'pliki z - kopia w nazwie ')
        # print( pressed )
        przegladanie.szukaj_kopia(pressed)

    def kopia_do_pliku(self):
        print(f'pliki z - kopia w nazwie do pliku ')

    def funkcja_na_probe(self,pressed):
        print( f'jestem funkcja na probe {pressed}')

    def puste_foldery(self, pressed):
        lista_pustych_folderow = znajdz_puste_foldery.folder(pressed)
        self.textBrowser.setText('ma pokazac puste foldery najlepiej z pliku puste_foldery.txt')
        # DORABIANIE SKASOWANIA PLIKU puste_foldery.txt jeśli istnieje
        print( lista_pustych_folderow)
        print( f'puste foldery znajdz_puste_foldery.folder(pressed){pressed}')

    def usun_duplikaty(self):
        print( f'funkcja usuwa duplikaty znalezione i pobiera info z jakiegos pliku')
        # funckcja po znalezieniu duplikatow usuwa je
        # usun_z_pliku.usuwanie(plik)  # DO SPRAWDZENIA

    def usun_puste_foldery(self):
        plik = 'foldery_puste.txt'
        print( f'funkcja ma usunac puste foldery, pobiera dane z pliku {plik}')
        # usun_z_pliku.usuwanie(plik)  # DO SPRAWDZENIA

    def usun_elemety_z_kopia_w_nazwie(self):
        plik = 'obiekty_z_kopia_w_nazwie.txt'
        print( f'funkcja ma usunac pliki lub foldery z kopia w nazwie, pobiera dane z {plik}')
        # usun_z_pliku.usuwanie(plik)  # DO SPRAWDZENIA

    def lcd1(self,sciezka):
        print( przegladanie.policz_foldery( sciezka ) )
    def lcd2(self,sciezka):
        print( przegladanie.policz_pliki( sciezka ) )
    def lcd3(self,sciezka):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", os.getcwd()))
        self.label_2.setText(_translate("MainWindow", "poniżej wybierz do którego folderu zajrzeć"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "Pokaż zawartość"))
        self.pushButton_3.setText(_translate("MainWindow", "Przejdź do folderu"))
        self.comboBox.addItems( przegladanie.folder(self.label.text() )[0])
        self.lcdNumber.display( przegladanie.policz_foldery( self.label.text() ) )
        self.lcdNumber_2.display( przegladanie.policz_pliki( self.label.text() ) )
        self.lcdNumber_3.display( 0 )
        self.comboBox_dysk.addItems(przegladanie.get_disks())
        self.pushButton_dysk.setText(_translate("MainWindow", "dysk"))
        self.pushButton_4.setText(_translate("MainWindow", "duplikaty"))
        self.pushButton_4_4.setText(_translate("MainWindow", "skasuj dup"))
        self.pushButton_5.setText(_translate("MainWindow", " kopia "))
        self.pushButton_5_5.setText(_translate("MainWindow", " sk kopie "))
        self.pushButton_6.setText(_translate("MainWindow", " puste foldery "))
        self.pushButton_6_6.setText(_translate("MainWindow", "sk puste"))
        self.pushButton_7.setText(_translate("MainWindow", " 7 "))
        self.label_7.setText(_translate("MainWindow", "      7 "))
        self.pushButton_8.setText(_translate("MainWindow", " 8 "))
        self.label_8.setText(_translate("MainWindow", "      8 "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
