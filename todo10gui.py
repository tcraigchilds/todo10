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
        lb1 = pyqtwidg.QLabel('To Do List', self)
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
        self.pbm1.clicked.connect(self.readallrecords)

        self.pbm2 = pyqtwidg.QPushButton('Find a Record To Read, Edit or Delete', self)
        self.pbm2.clicked.connect(self.findarecord)

        self.pbm3 = pyqtwidg.QPushButton('Create New Record', self)
        self.pbm3.clicked.connect(self.newrecord)

        qbtn = pyqtwidg.QPushButton('Quit', self)
        qbtn.clicked.connect(pyqtcor.QCoreApplication.instance().quit)
        qbtn.setStyleSheet("background-color: orange; font-size: 30px")

        self.grid = pyqtwidg.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(lb1, 0, 0, 1, 2)
        self.grid.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.verticalLayoutScroll.addWidget(self.pbm1, 1, 0)
        self.verticalLayoutScroll.addWidget(self.pbm2, 2, 0)
        self.verticalLayoutScroll.addWidget(self.pbm3, 3, 0)

        self.grid.addWidget(qbtn, 2, 0, 1, 2)

        self.setLayout(self.grid)
        self.setGeometry(300, 20, 700, 950)
        self.setWindowTitle('Database')
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

    def readallrecords(self):
        self.cleanscrollarea1()
        self.cleanscrollarea2()

        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(False)

        mydf = mon.readallrecords(self)
        self.showrecords(mydf, 0)

    def searchrecord(self):
        self.shost = self.en1.text()
        self.text = self.cb1.currentText()
        
        if self.text == 'recid':
            self.shost = int(self.shost)
        elif self.text != 'recid':
            pass
        
        self.rec1 = {self.text:self.shost}
        self.mydfs = mon.findarecord(self, self.rec1)
        self.showrecords(self.mydfs, 1)

        if len(self.mydfs)==1:
            self.edit1 = pyqtwidg.QPushButton('Edit This Record', self)
            self.edit1.clicked.connect(self.editrecord1)
            self.verticalLayoutScroll2.addWidget(self.edit1, 7, 0, 1, 3)
            self.del1 = pyqtwidg.QPushButton('Delete This Record', self)
            self.del1.clicked.connect(self.finaldelete1)
            self.verticalLayoutScroll2.addWidget(self.del1, 8, 0, 1, 3)
            return
        elif len(self.mydfs)!=1:
            return


    def searchrecord2(self):
        self.shost2 = self.en1.text()
        self.text2 = self.cb1.currentText()
        
        if self.text2 == 'recid':
            self.shost2 = int(self.shost2)
        elif self.text2 != 'recid':
            pass
        
        self.rec1 = {self.text:self.shost}        
        self.rec2 = {self.text: self.shost,self.text2: self.shost2 }
        
        self.mydf2s = mon.findarecord(self, self.rec2)
        self.showrecords(self.mydf2s, 1)

        if len(self.mydf2s)==1:
            self.edit1 = pyqtwidg.QPushButton('Edit This Record', self)
            self.edit1.clicked.connect(self.editrecord2)
            self.verticalLayoutScroll2.addWidget(self.edit1, 7, 0, 1, 3)
            self.del1 = pyqtwidg.QPushButton('Delete This Record', self)
            self.del1.clicked.connect(self.finaldelete2)
            self.verticalLayoutScroll2.addWidget(self.del1, 8, 0, 1, 3)
            return
        elif len(self.mydf2s)!=1:
            return

    def findarecord(self):
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
        self.pb3.clicked.connect(self.searchrecord)

        self.verticalLayoutScroll2.addWidget(self.lb9, 1, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb20, 2, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb4, 3, 0)
        self.verticalLayoutScroll2.addWidget(self.cb1, 3, 1)
        self.verticalLayoutScroll2.addWidget(self.lb3, 4, 0)
        self.verticalLayoutScroll2.addWidget(self.en1, 4, 1)
        self.verticalLayoutScroll2.addWidget(self.pb3, 4, 2)
        self.tya1 = pyqtwidg.QPushButton('Clear Results And Search Again?', self)
        self.tya1.clicked.connect(self.findarecord)
        self.verticalLayoutScroll2.addWidget(self.tya1, 5, 0, 1, 3)
        self.redu = pyqtwidg.QPushButton('Search Within Theses Results', self)
        self.redu.clicked.connect(self.searchrecord2)
        self.verticalLayoutScroll2.addWidget(self.redu, 6, 0, 1, 3)

    def editrecord1(self):
        self.updaterecord( self.mydfs )

    def editrecord2(self):
        self.updaterecord(self.mydf2s)
    
    def finaldelete1(self):
        #read record to be deleted
        for recd in range(0, len(self.mydfs)):
            self.yid = self.mydfs.get_value(recd, '_id')
            self.name = self.mydfs.get_value(recd, 'todoname')
            self.discription = self.mydfs.get_value(recd, 'tododisc')
            self.active = self.mydfs.get_value(recd, 'active')
            self.startdate = self.mydfs.get_value(recd, 'startdate')
            self.enddate = self.mydfs.get_value(recd, 'enddate')
            self.changedate = self.mydfs.get_value(recd, 'changeddate')
            self.createdate = self.mydfs.get_value(recd, 'createdate')
            self.recid = self.mydfs.get_value(recd, 'recid')
            self.deldate = datetime.datetime.now()
        #delete record
        self.recdelbk = {'recid': int(self.recid), 'todoname': str(self.name), 'tododisc':
                         str(self.discription), 'active': str(self.active), 'startdate': str(self.startdate), 'enddate':
                         str(self.enddate), 'changeddate': str(self.changedate), 'createdate': str(self.createdate),
                         'deletedate': str(self.deldate)}
        self.recdel = {'recid': int(self.recid)}
        mydf2 = mon.newrecordbk(self, self.recdelbk)
        self.ans = mon.deleteone(self, self.recdel)
        self.cleanscrollarea1()
        self.cleanscrollarea2()
        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(True)
        self.lb21 = pyqtwidg.QLabel('Record Deleted', self)
        self.verticalLayoutScroll2.addWidget(self.lb21, 1, 0, 1, 3)

    def finaldelete2(self):
        #read record to be deleted
        for recd in range(0, len(self.mydf2s)):
            self.yid = self.mydf2s.get_value(recd, '_id')
            self.name = self.mydf2s.get_value(recd, 'todoname')
            self.discription = self.mydf2s.get_value(recd, 'tododisc')
            self.active = self.mydf2s.get_value(recd, 'active')
            self.startdate = self.mydf2s.get_value(recd, 'startdate')
            self.enddate = self.mydf2s.get_value(recd, 'enddate')
            self.changedate = self.mydf2s.get_value(recd, 'changeddate')
            self.createdate = self.mydf2s.get_value(recd, 'createdate')
            self.recid = self.mydf2s.get_value(recd, 'recid')
            self.deldate = datetime.datetime.now()
        #delete record
        self.recdelbk2 = {'recid': int(self.recid), 'todoname': str(self.name), 'tododisc':
                         str(self.discription), 'active': str(self.active), 'startdate': str(self.startdate), 'enddate':
                         str(self.enddate), 'changeddate': str(self.changedate), 'createdate': str(self.createdate),
                         'deletedate': str(self.deldate)}
        self.recdel2 = {'recid': int(self.recid)}
        mydf2 = mon.newrecordbk(self, self.recdelbk2)
        self.ans = mon.deleteone(self, self.recdel2)    
        self.cleanscrollarea1()
        self.cleanscrollarea2()
        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(True)
        self.lb21 = pyqtwidg.QLabel('Record Deleted', self)
        self.verticalLayoutScroll2.addWidget(self.lb21, 1, 0, 1, 3)
    
    def newrecord(self):
        self.cleanscrollarea1()
        self.cleanscrollarea2()
        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(True)

        self.lb10 = pyqtwidg.QLabel('', self)
        self.lb10.setStyleSheet("background-color: red")
        self.lb10.setFixedHeight(5)
        self.lb21 = pyqtwidg.QLabel('Create A New Record', self)
        #self.lb21.setAlignment(Qt.AlignCenter)
        self.lb5 = pyqtwidg.QLabel('Enter ToDo Name: ', self)
        self.en2 = pyqtwidg.QLineEdit('', self)
        self.lb5a = pyqtwidg.QLabel('Enter Discription: ', self)
        self.en2a = pyqtwidg.QLineEdit('', self)
        self.lb6 = pyqtwidg.QLabel('Enter Start Date: ', self)
        self.en3 = pyqtwidg.QLineEdit('', self)
        self.lb7 = pyqtwidg.QLabel('Enter End Date: ', self)
        self.en4 = pyqtwidg.QLineEdit('', self)
        self.lb8 = pyqtwidg.QLabel('Enter Active State Y/N: ', self)
        self.en5 = pyqtwidg.QLineEdit('', self)
        self.pb6 = pyqtwidg.QPushButton('Click to Save', self)
        self.pb6.clicked.connect(self.saverec)
        self.pb6.setStyleSheet("background-color: red; font-size: 20px")

        self.verticalLayoutScroll2.addWidget(self.lb10, 10, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb21, 11, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb5, 12, 0)
        self.verticalLayoutScroll2.addWidget(self.en2, 12, 1)
        self.verticalLayoutScroll2.addWidget(self.lb5a, 13, 0)
        self.verticalLayoutScroll2.addWidget(self.en2a, 13, 1)
        self.verticalLayoutScroll2.addWidget(self.lb6, 14, 0)
        self.verticalLayoutScroll2.addWidget(self.en3, 14, 1)
        self.verticalLayoutScroll2.addWidget(self.lb7, 15, 0)
        self.verticalLayoutScroll2.addWidget(self.en4, 15, 1)
        self.verticalLayoutScroll2.addWidget(self.lb8, 16, 0)
        self.verticalLayoutScroll2.addWidget(self.en5, 16, 1)
        self.verticalLayoutScroll2.addWidget(self.pb6, 17, 0, 1, 3)

    def saverec(self):
        #savenewrecord
        rex = mon.findlastrecid(self)   
        rex = int(rex) +1
        recid1 = rex
        recid = 'recid'
        todoname = 'todoname'
        todoname1 = self.en2.text()
        tododisc = 'tododisc'
        tododisc1 = self.en2a.text()
        startdate = 'startdate'
        startdate1 = self.en3.text()
        enddate = 'enddate'
        enddate1 = self.en4.text()
        active = 'active'
        active1 = self.en5.text()
        changeddate = 'changeddate'
        changeddate1 = str(tdaytime)
        createdate = 'createdate'
        createdate1 = str(tdaytime)
        deletedate = 'deletedate'
        deletedate1 = " "
        # create new record
        self.rec1 = {recid:recid1, todoname:todoname1, tododisc:tododisc1, startdate:startdate1, enddate:enddate1, active:active1, changeddate:changeddate1, createdate:createdate1, deletedate:deletedate1}
        # add new record to mongodb
        mydf = mon.newrecord(self, self.rec1)
        mydfbk = mon.newrecordbk(self, self.rec1)
        df=mon.findarecord(self, self.rec1)
        self.showrecords(df, 0)
        #self.lb2.setText('Record Saved')
        self.scrollarea1.setVisible(True)
        self.scrollarea2.setVisible(False)

    def updaterecord(self, df):
        self.cleanscrollarea2()
        #edit current record
        mydf = df
        self.t = len(mydf)
        x = 0
        #read record
        for rec in range(0, self.t):
            self.yid = mydf.get_value(rec, '_id')
            self.ans0 = 'ID = ' + str(self.yid)
            
            self.yname = mydf.get_value(rec, 'todoname')
            ans5 = 'Name = ' + str(self.yname)

            self.ydiscription = mydf.get_value(rec, 'tododisc')
            ams6 = 'Discription = ' + str(self.ydiscription)

            self.yactive = mydf.get_value(rec, 'active')
            ans1 = 'Active? = ' + str(self.yactive)

            self.ystartdate = mydf.get_value(rec, 'startdate')
            ans2 = 'Start Date = ' + str(self.ystartdate)

            self.yenddate = mydf.get_value(rec, 'enddate')
            ans3 = 'End Date = ' + str(self.yenddate)

            self.ychangedate = mydf.get_value(rec, 'changeddate')
            ans4 = 'Most Recent Record Change Date = ' + str(self.ychangedate)
            self.changedate2 = str(tdaytime)
            
            self.createdate2 = mydf.get_value(rec, 'createdate')
            self.recid = mydf.get_value(rec, 'recid')
            self.recid = int(self.recid)
            self.deldate = mydf.get_value(rec, 'deletedate')
            
        #show record to be edited
        self.lb10 = pyqtwidg.QLabel('', self)
        self.lb10.setStyleSheet("background-color: red")
        self.lb10.setFixedHeight(5)
        self.lb21 = pyqtwidg.QLabel('Edit This Record', self)
        # self.lb21.setAlignment(Qt.AlignCenter)
        self.lb5 = pyqtwidg.QLabel('ToDo Name: ', self)
        self.en2 = pyqtwidg.QLineEdit(self.yname, self)
        self.lb5a = pyqtwidg.QLabel('Discription: ', self)
        self.en2a = pyqtwidg.QLineEdit(self.ydiscription, self)
        self.lb6 = pyqtwidg.QLabel('Start Date: ', self)
        self.en3 = pyqtwidg.QLineEdit(self.ystartdate, self)
        self.lb7 = pyqtwidg.QLabel('End Date: ', self)
        self.en4 = pyqtwidg.QLineEdit(self.yenddate, self)
        self.lb8 = pyqtwidg.QLabel('Active State Y/N: ', self)
        self.en5 = pyqtwidg.QLineEdit(self.yactive, self)
        self.pb6 = pyqtwidg.QPushButton('Click to Update', self)
        self.pb6.clicked.connect(self.saveupdate)
        self.pb6.setStyleSheet("background-color: red; font-size: 20px")

        self.verticalLayoutScroll2.addWidget(self.lb10, 10, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb21, 11, 0, 1, 3)
        self.verticalLayoutScroll2.addWidget(self.lb5, 12, 0)
        self.verticalLayoutScroll2.addWidget(self.en2, 12, 1)
        self.verticalLayoutScroll2.addWidget(self.lb5a, 13, 0)
        self.verticalLayoutScroll2.addWidget(self.en2a, 13, 1)
        self.verticalLayoutScroll2.addWidget(self.lb6, 14, 0)
        self.verticalLayoutScroll2.addWidget(self.en3, 14, 1)
        self.verticalLayoutScroll2.addWidget(self.lb7, 15, 0)
        self.verticalLayoutScroll2.addWidget(self.en4, 15, 1)
        self.verticalLayoutScroll2.addWidget(self.lb8, 16, 0)
        self.verticalLayoutScroll2.addWidget(self.en5, 16, 1)
        self.verticalLayoutScroll2.addWidget(self.pb6, 17, 0, 1, 3)

    def saveupdate(self):
        #read edit changes
        id = self.yid
        
        self.name = self.en2.text()
        self.description = self.en2a.text()
        self.startdate = self.en3.text()
        self.enddate = self.en4.text()
        self.active = self.en5.text()
        self.changedate = self.changedate2
        self.createdate = self.createdate2

        self.recU = {'_id': self.yid, 'recid': self.recid, 'todoname': self.name, 'tododisc': self.description, 'active': self.active, 'startdate': self.startdate, 'enddate': self.enddate, 'changeddate': self.changedate, 'createdate': self.createdate, 'deletedate': self.deldate}
        self.recU1 = {'recid': self.recid, 'todoname': self.name, 'tododisc': self.description, 'active': self.active, 'startdate': self.startdate, 'enddate': self.enddate, 'changeddate': self.changedate, 'createdate': self.createdate, 'deletedate': self.deldate}
        mydf = mon.updateone(self, self.recU)
        mydf2 = mon.newrecordbk(self, self.recU1)
        df=mon.findarecord(self, self.recU)
        self.showrecords(df, 0)  


if __name__ == '__main__':
    app = pyqtwidg.QApplication(sys.argv)
    tdate = datetime.date.today()
    tdaytime = datetime.datetime.now()
    mon = tdd.Mongo
    ex = ToDoGui()
    sys.exit(app.exec_())