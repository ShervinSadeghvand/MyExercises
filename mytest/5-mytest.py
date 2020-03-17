from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class window(QtWidgets.QDialog,QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "IMDB"
        self.InitWindow()

    def InitWindow(self):
        #self.setGeometry(self.x, self.y , self.width, self.height)
        self.setMinimumWidth(650)
        self.setMaximumWidth(650)
        self.setMaximumHeight(100)
        self.setMinimumHeight(100)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("imdb.jpg"))
        self.Layout_main()
        self.show()

    def Layout_main(self):
        
        self.GroupBox = QtWidgets.QGroupBox("Choose your Favorite ?")
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()

        button1 = QtWidgets.QPushButton("Movies",self)
        button1.setToolTip("The 2019 best movies")
        button1.setMinimumHeight(40)
        button1.setMaximumWidth(200)
        button1.setMinimumWidth(200)
        button1.clicked.connect(self.movies)
        hbox.addWidget(button1)

        button2 = QtWidgets.QPushButton("Animations",self)
        button2.setToolTip("The 2019 best animations")
        button2.setMinimumHeight(40)
        button2.setMaximumWidth(200)
        button2.setMinimumWidth(200)
        button2.clicked.connect(self.animations)
        hbox.addWidget(button2)

        button3 = QtWidgets.QPushButton("Series",self)
        button3.setToolTip("The 2019 best series")
        button3.setMinimumHeight(40)
        button3.setMaximumWidth(200)
        button3.setMinimumWidth(200)
        button3.clicked.connect(self.series)
        hbox.addWidget(button3)

        self.GroupBox.setLayout(hbox)
        vbox.addWidget(self.GroupBox)
        self.setLayout(vbox)

    def movies(self):
        self.close()
        self.app1 = movie()
        self.app1.show()
        
    def animations(self):
        self.close()
        self.app2 = animation()
        self.app2.show()

    def series(self):
        self.close()
        self.app3 = serie()
        self.app3.show()

class movie(QtWidgets.QDialog,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "2019 MOVIES"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setMaximumHeight(250)
        self.setMinimumHeight(250)
        self.setMaximumWidth(250)
        self.setMinimumWidth(250)
        self.setWindowIcon(QtGui.QIcon("imdb.jpg"))
        self.Layout_APP1()

    def Layout_APP1(self):
        GroupBox = QtWidgets.QGroupBox("The 2019 best Movies")
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()

        button1 = QtWidgets.QPushButton("Parasite",self)
        button1.setMinimumHeight(40)
        button1.setMaximumWidth(200)
        button1.setMinimumWidth(200)
        vbox.addWidget(button1)

        button2 = QtWidgets.QPushButton("1917",self)
        button2.setMinimumHeight(40)
        button2.setMaximumWidth(200)
        button2.setMinimumWidth(200)
        vbox.addWidget(button2)

        button3 = QtWidgets.QPushButton("Le Mans'66",self)
        button3.setMinimumHeight(40)
        button3.setMaximumWidth(200)
        button3.setMinimumWidth(200)
        vbox.addWidget(button3)

        button4 = QtWidgets.QPushButton("Back to MainMenu",self)
        button4.setMinimumHeight(40)
        button4.setMaximumWidth(200)
        button4.setMinimumWidth(200)
        button4.clicked.connect(self.back)
        vbox.addWidget(button4)

        GroupBox.setLayout(vbox)
        hbox.addWidget(GroupBox)
        self.setLayout(hbox)
        

    def back(self):
        self.close()
        self.app1 = window()

class animation(QtWidgets.QDialog,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "2019 Animations"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setMaximumHeight(250)
        self.setMinimumHeight(250)
        self.setMaximumWidth(250)
        self.setMinimumWidth(250)
        self.setWindowIcon(QtGui.QIcon("imdb.jpg"))
        self.Layout_APP2()

    def Layout_APP2(self):
        GroupBox = QtWidgets.QGroupBox("The 2019 best Animations")
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()

        button1 = QtWidgets.QPushButton("Klaus",self)
        button1.setMinimumHeight(40)
        button1.setMaximumWidth(200)
        button1.setMinimumWidth(200)
        vbox.addWidget(button1)

        button2 = QtWidgets.QPushButton("Spiderman into the spider verse",self)
        button2.setMinimumHeight(40)
        button2.setMaximumWidth(200)
        button2.setMinimumWidth(200)
        vbox.addWidget(button2)

        button3 = QtWidgets.QPushButton("coco",self)
        button3.setMinimumHeight(40)
        button3.setMaximumWidth(200)
        button3.setMinimumWidth(200)
        vbox.addWidget(button3)

        button4 = QtWidgets.QPushButton("Back to MainMenu",self)
        button4.setMinimumHeight(40)
        button4.setMaximumWidth(200)
        button4.setMinimumWidth(200)
        button4.clicked.connect(self.back)
        vbox.addWidget(button4)

        GroupBox.setLayout(vbox)
        hbox.addWidget(GroupBox)
        self.setLayout(hbox)
        

    def back(self):
        self.close()
        self.app1 = window()

class serie(QtWidgets.QDialog,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "2019 Series"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setMaximumHeight(250)
        self.setMinimumHeight(250)
        self.setMaximumWidth(250)
        self.setMinimumWidth(250)
        self.setWindowIcon(QtGui.QIcon("imdb.jpg"))
        self.Layout_APP3()

    def Layout_APP3(self):
        GroupBox = QtWidgets.QGroupBox("The 2019 best Series")
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()

        button1 = QtWidgets.QPushButton("GOT finall season",self)
        button1.setMinimumHeight(40)
        button1.setMaximumWidth(200)
        button1.setMinimumWidth(200)
        vbox.addWidget(button1)

        button2 = QtWidgets.QPushButton("Chernobyl",self)
        button2.setMinimumHeight(40)
        button2.setMaximumWidth(200)
        button2.setMinimumWidth(200)
        vbox.addWidget(button2)

        button3 = QtWidgets.QPushButton("Black Mirror",self)
        button3.setMinimumHeight(40)
        button3.setMaximumWidth(200)
        button3.setMinimumWidth(200)
        vbox.addWidget(button3)

        button4 = QtWidgets.QPushButton("Back to MainMenu",self)
        button4.setMinimumHeight(40)
        button4.setMaximumWidth(200)
        button4.setMinimumWidth(200)
        button4.clicked.connect(self.back)
        vbox.addWidget(button4)

        GroupBox.setLayout(vbox)
        hbox.addWidget(GroupBox)
        self.setLayout(hbox)
        
    def back(self):
        self.close()
        self.app1 = window()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    sys.exit(app.exec())