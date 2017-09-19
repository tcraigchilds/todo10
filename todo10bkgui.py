#!/usr/bin/env python
import datetime
import sys
import PyQt5.QtWidgets as pyqtwidg
import PyQt5.QtCore as pyqtcor
import tododb10 as tdd


class ToDoGui(pyqtwidg.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Build Main Form
        lb1 = pyqtwidg.QLabel('Back Up For The To Do List', self)
        lb1.setAlignment(pyqtcor.Qt.AlignCenter)
        lb1.setStyleSheet('font-weight: Bold')
        lb1.setFixedHeight(20)

        # build Scroll Area - Menu
        self.scrollArea = pyqtwidg.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMaximumHeight(150)
        self.scrollAreaWidgetContents = pyqtwidg.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(pyqtcor.QRect(0, 0, 300, 70))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutScroll = pyqtwidg.QGridLayout(self.scrollAreaWidgetContents)

        self.pbm1 = pyqtwidg.QPushButton('Read All', self)
        self.pbm1.clicked.connect(self.readallrecordsbk)

        self.pbm2 = pyqtwidg.QPushButton('Find a Record To Read', self)
        self.pbm2.clicked.connect(self.findarecordbk)

        qbtn = pyqtwidg.QPushButton('Quit', self)
        qbtn.clicked.connect(pyqtcor.QCoreApplication.instance().quit)
        qbtn.setStyleSheet("background-color: orange; font-size: 30px")

        self.grid = pyqtwidg.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(lb1, 0, 0, 1, 2)
        self.grid.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.verticalLayoutScroll.addWidget(self.pbm1, 1, 0)
        self.verticalLayoutScroll.addWidget(self.pbm2, 2, 0)

        self.grid.addWidget(qbtn, 2, 0, 1, 2)

        self.setLayout(self.grid)
        self.setGeometry(300, 20, 700, 950)
        self.setWindowTitle('Back Up Database')
        self.show()

        self.cleanscrollarea1()
        self.cleanscrollarea2()

    def showrecords(self, df, tat):
        self.cleanscrollarea1()

        mydf = df
        self.tat = tat
        self.t = len(mydf)
        x = 0

        for rec in range(0,self.t):
            yx = mydf.get_value(rec, '_id')
            self.ans0 = 'ID = ' + str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(self.ans0)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)
            
            yx = mydf.get_value(rec, 'recid')
            self.ans0 = 'RecID = ' + str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(self.ans0)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)            

            yx = mydf.get_value(rec, 'todoname')
            ans5 = 'Name = ' + str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans5)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'tododisc')
            ams6 = 'Discription = ' + str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ams6)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'active')
            ans1 = 'Active? = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans1)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'startdate')
            ans2 = 'Start Date = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans2)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'enddate')
            ans3 ='End Date = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans3)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'changeddate')
            ans4 = 'Most Recent Record Change Date = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans4)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

            yx = mydf.get_value(rec, 'createdate')
            ans4 = 'Create date = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans4)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0) 
            
            yx = mydf.get_value(rec, 'deletedate')
            ans4 = 'Delete Date = '+ str(yx)
            x += 1
            self.lb21rec = pyqtwidg.QLabel('', self)
            self.lb21rec.setText(ans4)
            self.lb21rec.adjustSize()
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)             

            self.lb21rec = pyqtwidg.QLabel('', self)
            x += 1
            bln = 'X'*20
            self.lb21rec.setText(bln)
            self.lb21rec.adjustSize()
            self.lb21rec.setStyleSheet("background-color: orange; font-size: 12px")
            self.verticalLayoutScroll1.addWidget(self.lb21rec, x, 0)

    def cleanscrollarea1(self):
        # Scroll Area 1 - Search Results
        self.scrollarea1 = pyqtwidg.QScrollArea(self)
        self.scrollarea1.setWidgetResizable(True)
        self.scrollarea1.setMinimumHeight(100)
        self.scrollarea1.setMaximumHeight(300)
        self.scrollarea1WidgetContents = pyqtwidg.QWidget(self.scrollarea1)
        self.scrollarea1WidgetContents.setGeometry(pyqtcor.QRect(0, 0, 700, 450))
        self.scrollarea1.setWidget(self.scrollarea1WidgetContents)
        self.verticalLayoutScroll1 = pyqtwidg.QGridLayout(self.scrollarea1WidgetContents)
        self.grid.addWidget(self.scrollarea1, 3, 0, 1, 2)
        return

    def cleanscrollarea2(self):
        # Scroll Area 2 - Find A record
        self.scrollarea2 = pyqtwidg.QScrollArea(self)
        self.scrollarea2.setWidgetResizable(True)
        self.scrollarea2.setMinimumHeight(300)
        self.scrollarea2.setMaximumHeight(400)
        self.scrollarea2WidgetContents = pyqtwidg.QWidget(self.scrollarea2)
        self.scrollarea2WidgetContents.setGeometry(pyqtcor.QRect(0, 0, 700, 450))
        self.scrollarea2.setWidget(self.scrollarea2WidgetContents)
        self.verticalLayoutScroll2 = pyqtwidg.QGridLayout(self.scrollarea2WidgetContents)
        self.grid.addWidget(self.scrollarea2, 6, 0, 1, 2)
        return

    def readallrecordsbk(self):
        self.cleanscrollarea1()
        self.cleanscrollarea2()

        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(False)

        mydf = mon.readallrecordsbk(self)
        self.showrecords(mydf, 0)

    def searchrecordbk(self):
        self.shost = self.en1.text()
        self.text = self.cb1.currentText()
        
        if self.text == 'recid':
            self.shost = int(self.shost)
        elif self.text != 'recid':
            pass
        
        self.rec1 = {self.text:self.shost}        
        #self.rec1 = {self.text:self.shost}
        self.mydf = mon.findarecordbk(self, self.rec1)
        self.showrecords(self.mydf, 1)

    def searchrecord2bk(self):
        self.shost2 = self.en1.text()
        self.text2 = self.cb1.currentText()
        
        if self.text2 == 'recid':
            self.shost2 = int(self.shost2)
        elif self.text2 != 'recid':
            pass
        
        self.rec2 = {self.text: self.shost,self.text2: self.shost2 }
        self.mydf2 = mon.findarecordbk(self, self.rec2)
        self.showrecords(self.mydf2, 1)

    def findarecordbk(self):
        self.cleanscrollarea1()
        self.cleanscrollarea2()

        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(True)

        self.lb9 = pyqtwidg.QLabel('', self)
        self.lb9.setStyleSheet("background-color: red")
        self.lb9.setFixedHeight(5)

        self.lb20 = pyqtwidg.QLabel('Find A Record', self)
        self.lb20.setAlignment(pyqtcor.Qt.AlignCenter)
        self.lb20.setStyleSheet("font-size: 20px; font-weight: bold")

        self.lb4 = pyqtwidg.QLabel('Choose a key', self)
        self.cb1 = pyqtwidg.QComboBox(self)
        self.cb1.addItem('recid')
        self.cb1.addItem('todoname')
        self.cb1.addItem('startdate')
        self.cb1.addItem('enddate')
        self.cb1.addItem('changeddate')
        self.cb1.addItem('active')

        self.lb3 = pyqtwidg.QLabel('Enter a Value', self)
        self.en1 = pyqtwidg.QLineEdit('', self)
        self.pb3 = pyqtwidg.QPushButton('Push to Search', self)
        self.pb3.clicked.connect(self.searchrecordbk)

        self.verticalLayoutScroll2.addWidget(self.lb9, 1, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb20, 2, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb4, 3, 0)
        self.verticalLayoutScroll2.addWidget(self.cb1, 3, 1)
        self.verticalLayoutScroll2.addWidget(self.lb3, 4, 0)
        self.verticalLayoutScroll2.addWidget(self.en1, 4, 1)
        self.verticalLayoutScroll2.addWidget(self.pb3, 4, 2)
        self.tya1 = pyqtwidg.QPushButton('Clear Results And Search Again?', self)
        self.tya1.clicked.connect(self.findarecordbk)
        self.verticalLayoutScroll2.addWidget(self.tya1, 5, 0, 1, 3)
        self.redu = pyqtwidg.QPushButton('Search Within Theses Results', self)
        self.redu.clicked.connect(self.searchrecord2bk)
        self.verticalLayoutScroll2.addWidget(self.redu, 6, 0, 1, 3)


if __name__ == '__main__':
    app = pyqtwidg.QApplication(sys.argv)
    tdate = datetime.date.today()
    tdaytime = datetime.datetime.now()
    mon = tdd.Mongo
    ex = ToDoGui()
    sys.exit(app.exec_())