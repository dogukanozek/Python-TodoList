a Pencerenin özellikleri
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-todo-list-50.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        #Ortalama Widgetı
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Taskları tutan listeWidget
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(480, 140, 451, 501))
        self.listWidget.setObjectName("listWidget")

        self.file_ekle()
          


        #Labelı tutan widget
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 100, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
       #Labelı tutan widget
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 16, 921, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        #Task ekleme butonu
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 300, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.ekle)
        self.pushButton.setObjectName("pushButton")
        #Task yazma yeri
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 220, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        #Task silme butonu
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 390, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2") 
        self.pushButton_2.clicked.connect(self.sil)
        #Taskların hepsini silme butonu
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 480, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.hepsinisil)
        #Exit butonu
        self.pushButton_4 = QtWidgets.QPush