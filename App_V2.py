#App v2

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtCore import QDateTime, Qt, QTimer


#Widgets

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()
 
        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        self.createTopLeftGroupBox()
        self.createTopRightTabWidget()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        styleComboBox.activated[str].connect(self.changeStyle)

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        grid = QGridLayout()
        grid.setColumnStretch(1, 4)
        grid.setColumnStretch(2, 4)
        
        grid.addLayout(topLayout, 0, 0, 1, 1)
        grid.addWidget(self.topLeftGroupBox, 1, 0, 1, 4)
        grid.addWidget(self.topRightTabWidget, 2, 3)
        grid.addWidget(self.bottomLeftTabWidget, 2, 0, 2, 3)
        grid.addWidget(self.bottomRightGroupBox, 3, 3)

        
        grid.setRowStretch(1, 4)
        grid.setRowStretch(2, 4)
        self.setLayout(grid)


        self.resize(850, 500)

        self.setWindowTitle("STARS by MapleMaker")
        self.changeStyle('Fusion')

        
    def changeStyle(self, Fusion):
        QApplication.setStyle(QStyleFactory.create(Fusion))


    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QLabel(self) 
        pixmap = QPixmap('C:/Users/lucas/OneDrive/Área de Trabalho/Imagem.jpg')
        self.topLeftGroupBox.setPixmap(pixmap)


    def createTopRightTabWidget(self):
        self.topRightTabWidget = QTabWidget()

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("1.")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.topRightTabWidget.addTab(tab2, "Anotações")

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget = QTabWidget()
        
        tab1 = QWidget()
        tab2 = QWidget()
    
        tableWidget = QTableWidget(250, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tableWidget2 = QTableWidget(250, 10)
        
        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(tableWidget2)
        tab2.setLayout(tab2hbox)
        
        
        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "&Table 02")
   
    

        
    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Gráficos")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
