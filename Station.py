'''
Created on Dec 16, 2020

@author: Yashas
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import MySQLdb as sql
from datetime import datetime as dt
import sys, os, threading, webbrowser, calendar
from PyQt5 import QtCore, QtGui, QtWidgets
import BGResource_rc
import IconResource_rc

ui,_ = loadUiType('Station.ui')

class Station(QMainWindow, ui):
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        #### Initial functions
        
        self.setTheme()
        self.handleButton()
        self.handleUI()
        self.showEndStationCombobox()
        self.showRouteCombobox()
        self.showTrainCombobox()
        self.signalTable()
        self.routeTable()
        self.trainTable()
        self.stationTable()
        self.dateDay()
        
        #### DO NOT MODIFY : Timer
        
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        
    def handleUI(self):
        
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)
        
    def handleButton(self):
        
        #### Login window
        
        self.pushButton_28.clicked.connect(self.loginUser)
        self.pushButton_29.clicked.connect(self.exitApp)
        
        self.pushButton_62.clicked.connect(self.openInstaVaishnavi)
        self.pushButton_63.clicked.connect(self.openInstaYashas)
        self.pushButton_64.clicked.connect(self.openLinkedInVaishnavi)
        self.pushButton_65.clicked.connect(self.openLinkedInYashas)
        
        #### Station window
        
        self.pushButton.clicked.connect(self.openStation)
        self.pushButton_2.clicked.connect(self.openRoute)
        self.pushButton_3.clicked.connect(self.openTicket)
        self.pushButton_4.clicked.connect(self.openSetting)
        
        self.pushButton_7.clicked.connect(self.setProceed)
        self.pushButton_8.clicked.connect(self.setCaution)
        self.pushButton_9.clicked.connect(self.setDanger)
        self.pushButton_31.clicked.connect(self.resetCircuit)
        self.pushButton_30.clicked.connect(self.setSignal)
        self.pushButton_51.clicked.connect(self.openLogsFolder)
        
        self.pushButton_6.clicked.connect(self.logoutUser)
        self.pushButton_5.clicked.connect(self.exitApp)
        
        #### Route window
    
        self.pushButton_15.clicked.connect(self.openStation)
        self.pushButton_13.clicked.connect(self.openRoute)
        self.pushButton_14.clicked.connect(self.openTicket)
        self.pushButton_10.clicked.connect(self.openSetting)
        
        self.pushButton_50.clicked.connect(self.addRoute)
        self.pushButton_37.clicked.connect(self.searchRoute)
        self.pushButton_38.clicked.connect(self.editRoute)
        self.pushButton_39.clicked.connect(self.deleteRoute)
        
        
        self.pushButton_11.clicked.connect(self.logoutUser)
        self.pushButton_12.clicked.connect(self.exitApp)
        
        #### Ticket window
        
        self.pushButton_21.clicked.connect(self.openStation)
        self.pushButton_19.clicked.connect(self.openRoute)
        self.pushButton_20.clicked.connect(self.openTicket)
        self.pushButton_16.clicked.connect(self.openSetting)
        
        self.pushButton_44.clicked.connect(self.ticket)
        self.pushButton_45.clicked.connect(self.createTicketClear)
        self.pushButton_49.clicked.connect(self.generatedTicketClear)
        self.pushButton_46.clicked.connect(self.exportTicket)
        self.pushButton_70.clicked.connect(self.fetchEarnings)
        self.pushButton_71.clicked.connect(self.clearTicketDB)
        
        self.pushButton_17.clicked.connect(self.logoutUser)
        self.pushButton_18.clicked.connect(self.exitApp)
        
        #### Settings window
        
        self.pushButton_27.clicked.connect(self.openStation)
        self.pushButton_25.clicked.connect(self.openRoute)
        self.pushButton_26.clicked.connect(self.openTicket)
        self.pushButton_22.clicked.connect(self.openSetting)
        
        self.pushButton_52.clicked.connect(self.switchSignal)
        self.pushButton_53.clicked.connect(self.switchTrains)
        self.pushButton_60.clicked.connect(self.switchStations)
        self.pushButton_56.clicked.connect(self.switchUsers)
        
        self.pushButton_32.clicked.connect(self.addSignal)
        self.pushButton_33.clicked.connect(self.searchSignal)
        self.pushButton_35.clicked.connect(self.deleteSignal)
        self.pushButton_34.clicked.connect(self.editSignal)
        
        self.pushButton_36.clicked.connect(self.addTrain)
        self.pushButton_59.clicked.connect(self.searchTrain)
        self.pushButton_58.clicked.connect(self.editTrain)
        self.pushButton_57.clicked.connect(self.deleteTrain)
        
        self.pushButton_40.clicked.connect(self.addStation)
        self.pushButton_41.clicked.connect(self.searchStation)
        self.pushButton_42.clicked.connect(self.editStation)
        self.pushButton_43.clicked.connect(self.deleteStation)
        
        self.pushButton_48.clicked.connect(self.verifyUser)
        self.pushButton_47.clicked.connect(self.addUser)
        self.pushButton_54.clicked.connect(self.editUser)
        self.pushButton_55.clicked.connect(self.deleteUser)
        
        self.pushButton_66.clicked.connect(self.openSetting)
        self.pushButton_61.clicked.connect(self.openHelp)
        
        self.pushButton_23.clicked.connect(self.logoutUser)
        self.pushButton_24.clicked.connect(self.exitApp)
        
    def openStation(self):
        
        self.tabWidget.setCurrentIndex(1)
        
    def openRoute(self):
        
        self.tabWidget.setCurrentIndex(2)
        
    def openTicket(self):
        
        self.tabWidget.setCurrentIndex(3)
        
    def switchSignal(self):
        
        self.tabWidget_3.setCurrentIndex(0)
        
    def switchTrains(self):
        
        self.tabWidget_3.setCurrentIndex(1)
        
    def switchStations(self):
        
        self.tabWidget_3.setCurrentIndex(2)
        
    def switchUsers(self):
        
        self.tabWidget_3.setCurrentIndex(3)
        
    def openSetting(self):
        
        self.tabWidget.setCurrentIndex(4)
        
    def openHelp(self):
    
        self.tabWidget.setCurrentIndex(5)
        
    def setTheme(self):
        
        style = open('Themes/darkstyle.css')
        style = style.read()
        self.setStyleSheet(style)
        
    #### Signal operations
        
    def setProceed(self):
        
        self.label_5.setStyleSheet("background-color: green")
        self.label_6.setStyleSheet("background-color: green")
        self.label_7.setStyleSheet("background-color: green")
        self.label_8.setStyleSheet("background-color: green")
        self.label_9.setStyleSheet("background-color: green")
        self.label_10.setStyleSheet("background-color: green")
        self.label_11.setStyleSheet("background-color: green")
        self.label_12.setStyleSheet("background-color: green")
        self.label_13.setStyleSheet("background-color: green")
        self.label_14.setStyleSheet("background-color: green")
    
    def setCaution(self):
        
        self.label_5.setStyleSheet("background-color: gold")
        self.label_6.setStyleSheet("background-color: gold")
        self.label_7.setStyleSheet("background-color: gold")
        self.label_8.setStyleSheet("background-color: gold")
        self.label_9.setStyleSheet("background-color: gold")
        self.label_10.setStyleSheet("background-color: gold")
        self.label_11.setStyleSheet("background-color: gold")
        self.label_12.setStyleSheet("background-color: gold")
        self.label_13.setStyleSheet("background-color: gold")
        self.label_14.setStyleSheet("background-color: gold")
    
    def setDanger(self):
        
        self.label_5.setStyleSheet("background-color: red")
        self.label_6.setStyleSheet("background-color: red")
        self.label_7.setStyleSheet("background-color: red")
        self.label_8.setStyleSheet("background-color: red")
        self.label_9.setStyleSheet("background-color: red")
        self.label_10.setStyleSheet("background-color: red")
        self.label_11.setStyleSheet("background-color: red")
        self.label_12.setStyleSheet("background-color: red")
        self.label_13.setStyleSheet("background-color: red")
        self.label_14.setStyleSheet("background-color: red")
        
    def resetCircuit(self):
        
        self.label_5.setStyleSheet("background-color: red")
        self.label_6.setStyleSheet("background-color: red")
        self.label_7.setStyleSheet("background-color: red")
        self.label_8.setStyleSheet("background-color: red")
        self.label_9.setStyleSheet("background-color: red")
        self.label_10.setStyleSheet("background-color: red")
        self.label_11.setStyleSheet("background-color: red")
        self.label_12.setStyleSheet("background-color: red")
        self.label_13.setStyleSheet("background-color: red")
        self.label_14.setStyleSheet("background-color: red")
        self.label_103.setText('')
        self.label_104.setText('') 
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        
    def openLogsFolder(self):
        
        path = ("Logs")
        path = os.path.realpath(path)
        os.startfile(path)
        
    def fetchSignalName(self, rRoad):
        
        sRoad = 'Road ' + rRoad
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select sName from signals where sRoad=%s''',[sRoad])
            sName = self.cur.fetchone()
            
            return sName[0]
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve signal data')
        
    def setSignalS1Home(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + 'S1 Home' + ' set;'
        self.writeToFile(text)
        self.label_29.setText(str(rRoad))
        color = "background-color: " + aspect 
        self.label_6.setStyleSheet(color)
        self.setOccupancy(rRoad)
        
    def resetSignalS1Home(self,aspect):
        
        text = self.label_74.text() + ' ' + 'S1 Home' + ' reset;'
        self.writeToFile(text)
        self.label_29.setText('M')
        color = "background-color: " + aspect 
        self.label_6.setStyleSheet(color)
        
    def setSignalS2Home(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + 'S2 Home' + ' set;'
        self.writeToFile(text)
        self.label_30.setText(str(rRoad))
        color = "background-color: " + aspect 
        self.label_13.setStyleSheet(color)
        self.setOccupancy(rRoad)
        
    def resetSignalS2Home(self,aspect):
        
        self.label_30.setText('M')
        text = self.label_74.text() + ' ' + 'S2 Home' + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_13.setStyleSheet(color)
    
    def setSignalS3Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_9.setStyleSheet(color)
        
    def resetSignalS3Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_9.setStyleSheet(color)
        
    def setSignalS4Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_7.setStyleSheet(color)
        
    def resetSignalS4Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_7.setStyleSheet(color)
        
    def setSignalS5AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_10.setStyleSheet(color)
        
    def resetSignalS5AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Up') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_10.setStyleSheet(color)
        
    def setSignalS3AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_12.setStyleSheet(color)
        
    def resetSignalS3AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_12.setStyleSheet(color)
        
    def setSignalS4AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_8.setStyleSheet(color)
        
    def resetSignalS4AStarter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_8.setStyleSheet(color)
        
    def setSignalS5Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_11.setStyleSheet(color)
        
    def resetSignalS5Starter(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + self.fetchSignalName(str(rRoad) + ' Dn') + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_11.setStyleSheet(color)
    
    def setSignalS2ALSS(self,aspect):
        
        text = self.label_74.text() + ' ' + 'S2A Advanced' + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_14.setStyleSheet(color)
        
    def resetSignalS2ALSS(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + 'S2A Advanced' + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_14.setStyleSheet(color)
        self.resetOccupancy(rRoad)
        
    def setSignalS1ALSS(self,aspect):
        
        text = self.label_74.text() + ' ' + 'S1A Advanced' + ' set;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_5.setStyleSheet(color)
        
    def resetSignalS1ALSS(self,aspect,rRoad):
        
        text = self.label_74.text() + ' ' + 'S1A Advanced' + ' reset;'
        self.writeToFile(text)
        color = "background-color: " + aspect 
        self.label_5.setStyleSheet(color)
        self.resetOccupancy(rRoad)
        
    def setUpHome(self, delay, aspect, rRoad): 
    
        setS1 = threading.Timer(delay, self.setSignalS1Home, [aspect, rRoad])
        setS1.start()
    
    def setUpLSS(self, delay, aspect, rRoad):
    
        setS2A = threading.Timer(delay, self.setSignalS2ALSS, [aspect])
        setS2A.start()

    def resetUpHome(self, delay, aspect, rRoad):
        
        resetS1 = threading.Timer(delay, self.resetSignalS1Home, [aspect])
        resetS1.start()

    def resetUpLSS(self, delay, aspect, rRoad):
        
        resetS2A = threading.Timer(delay, self.resetSignalS2ALSS, [aspect, rRoad])
        resetS2A.start()

    def setUpStarter(self, road, delay, aspect):
    
        if road == 2:
        
            self.setRoad2UpStarter(delay, aspect, road)

        elif road == 1:

            self.setRoad1UpStarter(delay, aspect, road)

        else:
    
            self.setRoad3UpStarter(delay, aspect, road)
            
    def resetUpStarter(self, road, delay, aspect):
    
        if road == 2:
        
            self.resetRoad2UpStarter(delay, aspect, road)

        elif road == 1:

            self.resetRoad1UpStarter(delay, aspect, road)

        else:
    
            self.resetRoad3UpStarter(delay, aspect, road)
        
    def setRoad1UpStarter(self, delay, aspect, rRoad):
    
        setS4 = threading.Timer(delay, self.setSignalS4Starter, [aspect, rRoad])
        setS4.start()

    def setRoad2UpStarter(self, delay, aspect, rRoad):
    
        setS3 = threading.Timer(delay, self.setSignalS3Starter, [aspect, rRoad])
        setS3.start()

    def setRoad3UpStarter(self, delay, aspect, rRoad):
    
        setS5A = threading.Timer(delay, self.setSignalS5AStarter, [aspect, rRoad])
        setS5A.start()
        
    def resetRoad1UpStarter(self, delay, aspect, rRoad):
    
        resetS4 = threading.Timer(delay, self.resetSignalS4Starter, [aspect, rRoad])
        resetS4.start()

    def resetRoad2UpStarter(self, delay, aspect, rRoad):
    
        resetS3 = threading.Timer(delay, self.resetSignalS3Starter, [aspect, rRoad])
        resetS3.start()

    def resetRoad3UpStarter(self, delay, aspect, rRoad):
    
        resetS5A = threading.Timer(delay, self.resetSignalS5AStarter, [aspect, rRoad])
        resetS5A.start()
        
    def setDnHome(self, delay, aspect, rRoad): 
    
        setS1 = threading.Timer(delay, self.setSignalS2Home, [aspect, rRoad])
        setS1.start()
    
    def setDnLSS(self, delay, aspect, rRoad):
    
        setS2A = threading.Timer(delay, self.setSignalS1ALSS, [aspect])
        setS2A.start()

    def resetDnHome(self, delay, aspect, rRoad):
        
        resetS1 = threading.Timer(delay, self.resetSignalS2Home, [aspect])
        resetS1.start()

    def resetDnLSS(self, delay, aspect, rRoad):
    
        resetS2A = threading.Timer(delay, self.resetSignalS1ALSS, [aspect, rRoad])
        resetS2A.start()

    def setDnStarter(self, road, delay, aspect):
    
        if road == 2:
        
            self.setRoad2DnStarter(delay, aspect, road)

        elif road == 1:

            self.setRoad1DnStarter(delay, aspect, road)

        else:
    
            self.setRoad3DnStarter(delay, aspect, road)
            
    def resetDnStarter(self, road, delay, aspect):
    
        if road == 2:
        
            self.resetRoad2DnStarter(delay, aspect, road)

        elif road == 1:

            self.resetRoad1DnStarter(delay, aspect, road)

        else:
    
            self.resetRoad3DnStarter(delay, aspect, road)
        
    def setRoad1DnStarter(self, delay, aspect, rRoad):
    
        setS4 = threading.Timer(delay, self.setSignalS4AStarter, [aspect, rRoad])
        setS4.start()

    def setRoad2DnStarter(self, delay, aspect, rRoad):
    
        setS3 = threading.Timer(delay, self.setSignalS3AStarter, [aspect, rRoad])
        setS3.start()

    def setRoad3DnStarter(self, delay, aspect, rRoad):
    
        setS5A = threading.Timer(delay, self.setSignalS5Starter, [aspect, rRoad])
        setS5A.start()
        
    def resetRoad1DnStarter(self, delay, aspect, rRoad):
    
        resetS4 = threading.Timer(delay, self.resetSignalS4AStarter, [aspect, rRoad])
        resetS4.start()

    def resetRoad2DnStarter(self, delay, aspect, rRoad):
    
        resetS3 = threading.Timer(delay, self.resetSignalS3AStarter, [aspect, rRoad])
        resetS3.start()

    def resetRoad3DnStarter(self, delay, aspect, rRoad):
    
        resetS5A = threading.Timer(delay, self.resetSignalS5Starter, [aspect, rRoad])
        resetS5A.start()

    def setUpDirnSignal(self, rRoad, rTime):
        
        if rTime == 'Skip':
        
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'
                
            self.setUpHome(1, 'green', rRoad)
            self.setUpStarter(rRoad, 1, aspect)    
            self.setUpLSS(1, 'green', rRoad)

            self.resetUpHome(10, 'red', rRoad)
            self.resetUpStarter(rRoad, 60, 'red')
            self.resetUpLSS(80, 'red', rRoad)

        elif rTime == 'Stop Express':
            
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'

            self.setUpHome(1, 'gold', rRoad)
            self.setUpStarter(rRoad, 60, aspect)
            self.setUpLSS(60, 'green', rRoad)
            
            self.resetUpHome(10, 'red', rRoad)
            self.resetUpStarter(rRoad, 80, 'red')
            self.resetUpLSS(160, 'red', rRoad)
        
        else:
            
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'

            self.setUpHome(1, 'gold', rRoad)
            self.setUpStarter(rRoad, 90, aspect)
            self.setUpLSS(90, 'green', rRoad)
            
            self.resetUpHome(10, 'red', rRoad)
            self.resetUpStarter(rRoad, 110, 'red')
            self.resetUpLSS(190, 'red', rRoad)
            
    def setDnDirnSignal(self, rRoad, rTime):
        
        if rTime == 'Skip':
        
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'
                
            self.setDnHome(1, 'green', rRoad)
            self.setDnStarter(rRoad, 1, aspect)    
            self.setDnLSS(1, 'green', rRoad)

            self.resetDnHome(10, 'red', rRoad)
            self.resetDnStarter(rRoad, 60, 'red')
            self.resetDnLSS(80, 'red', rRoad)

        elif rTime == 'Stop Express':
            
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'

            self.setDnHome(1, 'gold', rRoad)
            self.setDnStarter(rRoad, 60, aspect)
            self.setDnLSS(60, 'green', rRoad)
            
            self.resetDnHome(10, 'red', rRoad)
            self.resetDnStarter(rRoad, 80, 'red')
            self.resetDnLSS(160, 'red', rRoad)
        
        else:
            
            if rRoad == 2:
                
                aspect = 'green'
                
            else:
                
                aspect = 'gold'

            self.setDnHome(1, 'gold', rRoad)
            self.setDnStarter(rRoad, 90, aspect)
            self.setDnLSS(90, 'green', rRoad)
            
            self.resetDnHome(10, 'red', rRoad)
            self.resetDnStarter(rRoad, 110, 'red')
            self.resetDnLSS(190, 'red', rRoad)
            
    def fetchRouteDetails(self, x):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        rDetails = []
        
        try:
            
            self.cur.execute('''select rDirection, rRoad, rTime from routes where rName=%s''',[x])
            rData = self.cur.fetchone()
            
            rDirn = rData[0].split()
            rDirn = rDirn[0]            
            rDetails.append(rDirn)
            rRoad = rData[1].split()
            rRoad = rRoad[-1]           
            rDetails.append(rRoad)
            rTime = rData[2]            
            rDetails.append(rTime)
            
            return rDetails
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve route data')
    
    def setSignal(self):

        try:
            
            self.statusBar().showMessage('')
            routeName = self.comboBox.currentText()
            x = self.fetchRouteDetails(routeName)
            tName = self.comboBox_2.currentText()
        
            self.label_103.setText(tName)
            self.label_104.setText(routeName) 
        
            rDirection = x[0]
            rRoad = int(x[1])
            rTime = x[2]
            cTime = self.label_74.text()
        
            if self.checkOccupancy(rRoad):
                
                self.logSignalDetails(rDirection, rRoad, rTime, tName, cTime)
        
                if rDirection == 'Up':
        
                    self.setUpDirnSignal(rRoad, rTime)

                else:

                    self.setDnDirnSignal(rRoad, rTime)
                    
            else:
                
                self.statusBar().showMessage('Path occupied, please wait')
                self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Please select proper values')
            self.statusBarClear()
            
    def logSignalDetails(self, rDirection, rRoad, rTime, tName, cTime):
        
        self.writeToFile('\n' + cTime + ': Route set: ' + rDirection + '; Train: ' + tName + '; ')
    
    def writeToFile(self, text):
        
        x = dt.now()
        logFileName = 'Log ' + str(x.day) + '-' + str(x.month) + '-' + str(x.year)
        file = open('Logs/' + logFileName + '.txt', 'a')
        file.write(text)
        file.close()
        
    def setOccupancy(self, rRoad):
        
        if rRoad == 1:
            
            self.label_141.setText('Occupied')
            self.label_135.setStyleSheet("background-color: red")
        
        if rRoad == 2:
            
            self.label_142.setText('Occupied')
            self.label_136.setStyleSheet("background-color: red")
        
        if rRoad == 3:
            
            self.label_143.setText('Occupied')
            self.label_137.setStyleSheet("background-color: red")
    
    def resetOccupancy(self, rRoad):
        
        if rRoad == 1:
            
            self.label_141.setText('Free')
            self.label_135.setStyleSheet("background-color: rgb(138, 138, 138);")
        
        if rRoad == 2:
            
            self.label_142.setText('Free')
            self.label_136.setStyleSheet("background-color: rgb(138, 138, 138);")
        
        if rRoad == 3:
            
            self.label_143.setText('Free')
            self.label_137.setStyleSheet("background-color: rgb(138, 138, 138);")
            
    def checkOccupancy(self, rRoad):
        
        if rRoad == 1:
            
            if self.label_141.text() == 'Free':
                
                return True
            
            return False
        
        if rRoad == 2:
            
            if self.label_142.text() == 'Free':
                
                return True
            
            return False
        
        if rRoad == 3:
            
            if self.label_143.text() == 'Free':
                
                return True
            
            return False
    
    #### Route operations
    
    def addRoute(self):
        
        rName = self.lineEdit_5.text()
        rDirection = self.comboBox_10.currentText()
        rWait = self.comboBox_8.currentText()
        rRoad = self.comboBox_14.currentText()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''insert into routes (rName,rDirection,rRoad,rTime) values (%s,%s,%s,%s)''',(rName,rDirection,rRoad,rWait))
            self.con.commit()
            self.lineEdit_5.setText('')
            self.comboBox_10.setCurrentIndex(0)
            self.comboBox_8.setCurrentIndex(0)
            self.comboBox_14.setCurrentIndex(0)
            self.routeTable()
            self.showRouteCombobox()
            self.statusBar().showMessage('Route added successfully')
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to add route')
            self.statusBarClear()
    
    def searchRoute(self):
        
        rName = self.lineEdit_23.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select rName, rDirection, rTime, rRoad from routes''')
            rData = self.cur.fetchall()
            
            for i in rData:
                
                if rName == i[0]:
                    
                    self.label_81.setText(rName)
                    self.lineEdit_6.setText(i[0])
                    self.comboBox_15.setCurrentText(i[1])
                    self.comboBox_16.setCurrentText(i[2])
                    self.comboBox_17.setCurrentText(i[3])
                    self.lineEdit_23.setText('')
                    self.statusBar().showMessage('Route found')
                    self.statusBarClear()
                    break
                
                else:
                    
                    self.statusBar().showMessage('Route not found')
                    self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve route data')
            self.statusBarClear()
    
    def deleteRoute(self):
        
        rName = self.label_81.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            warn = QMessageBox.warning(self, 'Sure to delete?', 'Are you sure you want to delete route?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                
                self.cur.execute('''delete from routes where rName=%s''',[rName])
                self.con.commit()
                self.statusBar().showMessage('Route deleted successfully')
                self.statusBarClear()
                self.label_81.setText('')
                self.lineEdit_6.setText('')
                self.comboBox_15.setCurrentIndex(0)
                self.comboBox_16.setCurrentIndex(0)
                self.comboBox_17.setCurrentIndex(0)
                self.routeTable()
                self.showRouteCombobox()
            
        except:
            
            self.statusBar().showMessage('Unable to retrieve route data')
            self.statusBarClear()
    
    def editRoute(self):
        
        oName = self.label_81.text()
        rName = self.lineEdit_6.text()
        rDirection = self.comboBox_15.currentText()
        rTime = self.comboBox_16.currentText()
        rRoad = self.comboBox_17.currentText()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''update routes set rName=%s, rDirection=%s, rRoad=%s, rTime=%s where rName=%s''',(rName,rDirection,rRoad,rTime,oName))
            self.con.commit()
            self.label_81.setText('')
            self.lineEdit_6.setText('')
            self.comboBox_15.setCurrentIndex(0)
            self.comboBox_16.setCurrentIndex(0)
            self.comboBox_17.setCurrentIndex(0)
            self.routeTable()
            self.showRouteCombobox()
            self.statusBar().showMessage('Route updated successfully')
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve route data')
            self.statusBarClear()
            
    def routeTable(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call selectRoute()''')
            rData = self.cur.fetchall()
            
            if rData:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
                
                for row, form in enumerate(rData):
                    for col, item in enumerate(form):
                        
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    rowPos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPos)
                    
            else:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve route data')
            self.statusBarClear()
            
    def showRouteCombobox(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select rName from routes''')
            rData = self.cur.fetchall()
            self.comboBox.clear()
            self.comboBox.addItem('--Select route--')
            
            for i in rData:
                
                self.comboBox.addItem(i[0])  
        
        except:
            
            self.statusBar().showMessage('Unable to set route combobox')
            self.statusBarClear()
    
    #### Ticket operations
    
    def createTicketClear(self):
        
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        self.lineEdit_9.setText('0')
        self.lineEdit_22.setText('0')
    
    def generatedTicketClear(self):
        
        warn = QMessageBox.warning(self, 'Sure to clear?', 'Are you sure to clear without exporting?', QMessageBox.Yes|QMessageBox.No)
        
        if warn == QMessageBox.Yes:
            
            self.label_51.setText('')
            self.label_52.setText('')
            
    def generateTicketNumber(self, x):
        
        x = x.split(' ')

        y = x[0].split('-')
        z = x[1].split('-')

        ticketNumberList = y + z

        ticketNumber = ''
        ticketNumber = ticketNumber.join(ticketNumberList)
    
        return ticketNumber
            
    def exportTicket(self):
        
        x = self.label_76.text()
        ticketNumber = self.generateTicketNumber(x)
        toStation = self.label_51.text()
        totalPrice = self.label_52.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select tStat,tType,tAdult,tChild,tPrice from tickets where tTime=%s''',[x])
            tData = self.cur.fetchone()
            
            pathOfFile = 'Tickets/TNo-' + str(ticketNumber) + '.txt'
            print(pathOfFile)
            file = open(pathOfFile,'w')
            
            ticketContent = f'INDIAN RAILWAYS \n\nUNRESERVED TICKET \nVALID UPTO 3 HOURS UNTIL DEPARTURE \n\nTicket Number: {ticketNumber} \n\nFrom: Ranibennur \nTo: {toStation} \nTotal Price: {totalPrice} \n\n!INDIAN RAILWAYS RECOVERS ONLY 57% OF THE EARNED REVENUE! \n\nHAVE A HAPPY AND SAFE JOURNEY!'
            file.write(ticketContent)
            self.statusBar().showMessage('Ticket exported successfully')
            self.statusBarClear()
            
            file.close()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve ticket data')
            self.statusBarClear()
    
    def showTicketDetails(self,issuedTime):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select tStat,tPrice from tickets where tTime=%s''',[issuedTime])
            tData = self.cur.fetchone()
            self.label_76.setText(issuedTime)
            self.label_51.setText(tData[0])
            self.label_52.setText(str(tData[1]))
            self.statusBar().showMessage('Ticket generated')
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve ticket data')
            self.statusBarClear()
            
    def findBasePriceType(self, x, y):      
        
        basePrice = 0
        
        if y == '2S Superfast':
                
            basePrice = 45 + self.findBasePriceDistance(x)
            
        elif y == '2S Mail/Express':
                
            basePrice = 35 + self.findBasePriceDistance(x)
            
        else:
                
            basePrice = 10 + self.findBasePriceDistance(x)
            
        basePrice = int(basePrice)
        return basePrice
            
    def findBasePriceDistance(self, x):
        
        if x>=0 and x<36:
            
            basePrice = 0
        
        elif x>=36 and x<72:
            
            basePrice = 10
        
        elif x>=108 and x<144:
            
            basePrice = 18
        
        elif x>=144 and x<180:
            
            basePrice = 26
        
        elif x>=180 and x<210:
            
            basePrice = 34
        
        elif x>=210 and x<252:
            
            basePrice = 42
        
        elif x>=252 and x<288:
            
            basePrice = 50
        
        elif x>=288 and x<324:
            
            basePrice = 58
        
        elif x>=324 and x<360:
            
            basePrice = 66
        
        elif x>=360 and x<396:
            
            basePrice = 64
        
        elif x>=396 and x<432:
            
            basePrice = 72
        
        elif x>=432 and x<468:
            
            basePrice = 80
        
        else:
            
            basePrice = 90
            
        basePrice = int(basePrice)   
        return basePrice
    
    def ticket(self):
        
        endStat = self.comboBox_7.currentText()
        trainType = self.comboBox_9.currentText()
        x = dt.now()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select stDist from stations where stName=%s''',[endStat])
            endStatDist = self.cur.fetchone()
            endStatDist = int(endStatDist[0])
            issuedTime = str(x.day) + '-' + str(x.month) + '-' + str(x.year) + ' ' + str(x.hour) + '-' + str(x.minute) + '-' + str(x.second)
            adultCount = int(self.lineEdit_9.text())
            childCount = int(self.lineEdit_22.text())
            basePrice = self.findBasePriceType(endStatDist, trainType)
            totalPrice = 0
            
            self.cur.execute('''insert into tickets (tStat,tType,tBasePrice,tTime,tAdult,tChild,tPrice) values (%s,%s,%s,%s,%s,%s,%s)''',(endStat,trainType,basePrice,issuedTime,adultCount,childCount,totalPrice))
            self.con.commit()
            
            self.showTicketDetails(issuedTime)
            
            self.statusBar().showMessage('Ticket details added successfully')
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve ticket data')
            self.statusBarClear()
            
    def clearTicketDB(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call resetTicket()''')
            self.statusBar().showMessage('Ticket DB reset')
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve ticket data')
            self.statusBarClear()
    
    def fetchEarnings(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call fetchEarning()''')
            tPrice = self.cur.fetchone()
            tPrice = tPrice[0]
            print(tPrice)
            self.statusBar().showMessage('Total amount earned so far: INR ' + str(tPrice))
            self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve ticket data')
            self.statusBarClear()
        
    #### Signal operations
    
    def addSignal(self):
        
        sName = self.lineEdit_3.text()
        sType = self.comboBox_5.currentText()
        sRoad = self.comboBox_13.currentText()  
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''insert into signals (sName,sRoad,sType) values (%s,%s,%s)''',(sName,sRoad,sType))
            self.con.commit()
            self.statusBar().showMessage('Signal added successfully')
            self.statusBarClear()
            self.signalTable()
            self.lineEdit_3.setText('')
            self.comboBox_5.setCurrentIndex(0)
            self.comboBox_13.setCurrentIndex(0)
            
        except:
            
            self.statusBar().showMessage('Unable to add signal')
            self.statusBarClear()
    
    def searchSignal(self):
        
        sName = self.lineEdit_8.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select sName, sType, sRoad from signals''')
            sData = self.cur.fetchall()
            
            for i in sData:
                
                if sName == i[0]:
                    
                    self.label_87.setText(sName)
                    self.lineEdit_24.setText(i[0])
                    self.comboBox_6.setCurrentText(i[1])
                    self.comboBox_18.setCurrentText(i[2])
                    self.statusBar().showMessage('Signal found')
                    self.statusBarClear()
                    self.lineEdit_8.setText('')
                    break
                
                else:
                    
                    self.statusBar().showMessage('Signal not found')
                    self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve signal data')
    
    def deleteSignal(self):
        
        sName = self.label_87.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            warn = QMessageBox.warning(self, 'Sure to delete?', 'Are you sure you want to delete signal?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                
                self.cur.execute('''delete from signals where sName=%s''',[sName])
                self.con.commit()
                self.statusBar().showMessage('Signal deleted successfully')
                self.statusBarClear()
                self.signalTable()
                self.signalTable()
                self.label_87.setText('')
                self.lineEdit_24.setText('')
                self.comboBox_6.setCurrentIndex(0)
                self.comboBox_18.setCurrentIndex(0)
        
        except:
            
            self.statusBar().showMessage('Unable to delete signal')
            self.statusBarClear()
    
    def editSignal(self):
        
        oName = self.label_87.text()
        sName = self.lineEdit_24.text()
        sType = self.comboBox_6.currentText()
        sRoad = self.comboBox_18.currentText()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''update signals set sName=%s, sRoad=%s, sType=%s where sName=%s''',(sName, sRoad, sType, oName))
            self.con.commit()
            self.statusBar().showMessage('Signal details updated successfully')
            self.statusBarClear()
            self.signalTable()
            self.signalTable()
            self.label_87.setText('')
            self.lineEdit_24.setText('')
            self.comboBox_6.setCurrentIndex(0)
            self.comboBox_18.setCurrentIndex(0)
        
        except:
            
            self.statusBar().showMessage('Unable to update signal data')
            self.statusBarClear()
            
    def signalTable(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call selectSignal()''')
            sData = self.cur.fetchall()
            
            if sData:
                
                self.tableWidget_4.setRowCount(0)
                self.tableWidget_4.insertRow(0)
                
                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        
                        self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    rowPos = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(rowPos)
                    
            else:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve signal data')
            self.statusBarClear()
    
    #### Train operations
    
    def addTrain(self):
        
        tNumber = int(self.lineEdit_4.text())
        tName = self.lineEdit_7.text()
        tType = self.comboBox_11.currentText()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''insert into trains (tNumber,tName,tType) values (%s,%s,%s)''',(tNumber, tName, tType))
            self.con.commit()
            self.statusBar().showMessage('Train added successfully')
            self.statusBarClear()
            self.trainTable()
            self.showTrainCombobox()
            self.lineEdit_4.setText('')
            self.lineEdit_7.setText('')
            self.comboBox_11.setCurrentIndex(0)
        
        except:
            
            self.statusBar().showMessage('Unable to add train')
            self.statusBarClear()
    
    def searchTrain(self):
        
        tCode = self.lineEdit_33.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select tNumber, tName, tType from trains''')
            tData = self.cur.fetchall()
            
            for i in tData:
                
                if tCode == str(i[0]):
                    
                    self.label_39.setText(tCode)
                    self.lineEdit_30.setText(str(i[0]))
                    self.lineEdit_32.setText(i[1])
                    self.comboBox_12.setCurrentText(i[2])
                    self.lineEdit_33.setText('')
                    self.statusBar().showMessage('Train found')
                    self.statusBarClear()
                    break
                
                else:
                    
                    self.statusBar().showMessage('Train not found')
                    self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve train data')
    
    def deleteTrain(self):
        
        tCode = self.label_39.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            warn = QMessageBox.warning(self, 'Sure to delete?', 'Are you sure you want to delete train?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                
                self.cur.execute('''delete from trains where tNumber=%s''',[tCode])
                self.con.commit()
                self.statusBar().showMessage('Train deleted successfully')
                self.statusBarClear()
                self.trainTable()
                self.showTrainCombobox()
                self.label_39.setText('')
                self.lineEdit_30.setText('')
                self.lineEdit_32.setText('')
                self.comboBox_12.setCurrentIndex(0)
        
        except:
            
            self.statusBar().showMessage('Unable to delete train')
            self.statusBarClear()
    
    def editTrain(self):
        
        oCode = self.label_39.text()
        tNumber = self.lineEdit_30.text()
        tName = self.lineEdit_32.text()
        tType = self.comboBox_12.currentText()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''update trains set tNumber=%s, tName=%s, tType=%s where tNumber=%s''',(tNumber, tName, tType, oCode))
            self.con.commit()
            self.statusBar().showMessage('Train details updated successfully')
            self.statusBarClear()
            self.trainTable()
            self.showTrainCombobox()
            self.label_39.setText('')
            self.lineEdit_30.setText('')
            self.lineEdit_32.setText('')
            self.comboBox_12.setCurrentIndex(0)
        
        except:
            
            self.statusBar().showMessage('Unable to update train data')
            self.statusBarClear()
    
    def trainTable(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call selectTrain()    ''')
            tData = self.cur.fetchall()
            
            if tData:
                
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)
                
                for row, form in enumerate(tData):
                    for col, item in enumerate(form):
                        
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    rowPos = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(rowPos)
            
            else:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve train data')
            self.statusBarClear()
            
    def showTrainCombobox(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select tNumber, tName from trains''')
            tData = self.cur.fetchall()
            self.comboBox_2.clear()
            self.comboBox_2.addItem('--Select train--')
            
            for i in tData:
                
                trainName = str(i[0]) + ' ' + i[1]
                self.comboBox_2.addItem(trainName)  
        
        except:
            
            self.statusBar().showMessage('Unable to set train combobox')
            self.statusBarClear()
    
    #### Station operations
    
    def addStation(self):
        
        sName = self.lineEdit_10.text()
        sCode = self.lineEdit_11.text()
        sDist = self.lineEdit_12.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''insert into stations (stName,stCode,stDist) values (%s,%s,%s)''',(sName, sCode, sDist))
            self.con.commit()
            self.statusBar().showMessage('Station added successfully')
            self.statusBarClear()
            self.stationTable()
            self.showEndStationCombobox()
            self.lineEdit_10.setText('')
            self.lineEdit_11.setText('')
            self.lineEdit_12.setText('')
        
        except:
            
            self.statusBar().showMessage('Unable to add station')
            self.statusBarClear()
    
    def searchStation(self):
        
        sCode = self.lineEdit_13.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select stName, stCode, stDist from stations''')
            sData = self.cur.fetchall()
            
            for i in sData:
                
                if sCode == i[1]:
                    
                    self.label_69.setText(sCode)
                    self.lineEdit_16.setText(i[0])
                    self.lineEdit_21.setText(i[1])
                    self.lineEdit_17.setText(str(i[2]))
                    self.lineEdit_13.setText('')
                    self.statusBar().showMessage('Station found')
                    self.statusBarClear()
                    break
                
                else:
                    
                    self.statusBar().showMessage('Station not found')
                    self.statusBarClear()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve station data')
    
    def deleteStation(self):
        
        sCode = self.label_69.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            warn = QMessageBox.warning(self, 'Sure to delete?', 'Are you sure you want to delete station?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                
                self.cur.execute('''delete from stations where stCode=%s''',[sCode])
                self.con.commit()
                self.statusBar().showMessage('Station deleted successfully')
                self.statusBarClear()
                self.stationTable()
                self.showEndStationCombobox()
                self.label_69.setText('')
                self.lineEdit_16.setText('')
                self.lineEdit_21.setText('')
                self.lineEdit_17.setText('')
        
        except:
            
            self.statusBar().showMessage('Unable to delete station')
            self.statusBarClear()
    
    def editStation(self):
        
        oCode = self.label_69.text()
        sName = self.lineEdit_16.text()
        sCode = self.lineEdit_21.text()
        sDist = self.lineEdit_17.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''update stations set stName=%s, stCode=%s, stDist=%s where stCode=%s''',(sName, sCode, sDist, oCode))
            self.con.commit()
            self.statusBar().showMessage('Station details updated successfully')
            self.statusBarClear()
            self.stationTable()
            self.showEndStationCombobox()
            self.lineEdit_16.setText('')
            self.lineEdit_21.setText('')
            self.lineEdit_17.setText('')
        
        except:
            
            self.statusBar().showMessage('Unable to update station data')
            self.statusBarClear()
            
    def stationTable(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''call selectStation()''')
            sData = self.cur.fetchall()
            
            if sData:
                
                self.tableWidget_2.setRowCount(0)
                self.tableWidget_2.insertRow(0)
                
                for row, form in enumerate(sData):
                    for col, item in enumerate(form):
                        
                        self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    rowPos = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(rowPos)
                    
            else:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve station data')
            self.statusBarClear()
            
    def showEndStationCombobox(self):
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select stName from stations''')
            sData = self.cur.fetchall()
            self.comboBox_7.clear()
            self.comboBox_7.addItem('--Select end station--')
            
            for i in sData:
                
                self.comboBox_7.addItem(i[0])  
        
        except:
            
            self.statusBar().showMessage('Unable to set end station combobox')
            self.statusBarClear()
    
    #### User operations
    
    def loginUser(self):
        
        uName = self.lineEdit.text()
        uPass = self.lineEdit_2.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select uName, uPass from users''')
            uData = self.cur.fetchall()
            
            for i in uData:
                
                if uName == i[0] and uPass == i[1]:
                    
                    self.tabWidget.setCurrentIndex(1)
                    self.statusBar().showMessage('Logged in successfully')
                    self.statusBarClear()
                    self.label_60.setText(uName)
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    break
                
                else:
                    
                    self.label_4.setText('Incorrect credentials')
                    self.LabelForUserVerify()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve user data')
            self.statusBarClear()
            
    def logoutUser(self):
        
        warn = QMessageBox.warning(self, 'Sure to log out?', 'Are you sure you want to log out?', QMessageBox.Yes|QMessageBox.No)
        
        if warn == QMessageBox.Yes :
            
            self.statusBar().showMessage('')
            self.groupBox_17.setEnabled(False)
            self.tabWidget.setCurrentIndex(0)
    
    def addUser(self):
        
        uName = self.lineEdit_14.text()
        uPass = self.lineEdit_15.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''insert into users (uName,uPass) values (%s,%s)''',(uName, uPass))   
            self.con.commit()
            self.statusBar().showMessage('User added successfully')
            self.statusBarClear()
            self.lineEdit_14.setText('')
            self.lineEdit_15.setText('')
        
        except:
            
            self.statusBar().showMessage('Unable to add user')
            self.statusBarClear()
    
    def verifyUser(self):
        
        uName = self.label_60.text()
        uPass = self.lineEdit_18.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''select uName, uPass from users''')
            uData = self.cur.fetchall()
            
            for i in uData:
                
                if uName == i[0] and uPass == i[1]:
                    
                    self.statusBar().showMessage('Verified successfully')
                    self.statusBarClear()
                    self.groupBox_17.setEnabled(True)
                    self.lineEdit_19.setText(uName)
                    self.lineEdit_20.setText(uPass)
                    self.lineEdit_18.setText('')
                    break
                
                else:
                    
                    self.label_61.setText('Incorrect password')
                    self.LabelForUserVerify()
        
        except:
            
            self.statusBar().showMessage('Unable to retrieve user data')
    
    def editUser(self):
        
        oName = self.label_60.text()
        uName = self.lineEdit_19.text()
        uPass = self.lineEdit_20.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            self.cur.execute('''update users set uName=%s, uPass=%s where uName=%s''',(uName, uPass, oName))
            self.con.commit()
            print(uName,uPass,oName)
            self.label_60.setText(uName)
            self.lineEdit_19.setText('')
            self.lineEdit_20.setText('')
            self.statusBar().showMessage('User details updated successfully')
            self.statusBarClear()
            
        except:
            
            self.statusBar().showMessage('Unable to update user data')
            self.statusBarClear()
    
    def deleteUser(self):
        
        uName = self.label_60.text()
        
        self.con = sql.connect('localhost', 'root', 'drowssap', 'station')
        self.cur = self.con.cursor()
        
        try:
            
            warn = QMessageBox.warning(self, 'Sure to delete?', 'Are you sure you want to delete?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                
                self.cur.execute('''delete from users where uName=%s''',[uName])
                self.con.commit()
                self.lineEdit_19.setText('')
                self.lineEdit_20.setText('')
                self.statusBar().showMessage('User deleted successfully')
                self.statusBarClear()
                self.tabWidget.setCurrentIndex(0)
            
        except:
            
            self.statusBar().showMessage('Unable to delete user')
            self.statusBarClear()
            
    #### Miscellaneous operations
            
    def exitApp(self):
        
        warn = QMessageBox.warning(self, 'Sure to exit?', 'Are you sure you want to exit?', QMessageBox.Yes|QMessageBox.No)
        
        if warn == QMessageBox.Yes:
            
            sys.exit()
            
    def displayTime(self):
        
        currentTime = QTime.currentTime()
        displayTimeText = currentTime.toString('hh:mm:ss')
        self.label_74.setText(displayTimeText)
        self.label_97.setText(displayTimeText)
        self.label_98.setText(displayTimeText)
        self.label_99.setText(displayTimeText)
        self.label_100.setText(displayTimeText)
        
    def dateDay(self):
        
        x = dt.now()
        y = x.weekday()
        date = str(x.day) + '/' + str(x.month) + '/' + str(x.year)
        self.label_111.setText(date)
        self.label_112.setText(calendar.day_name[y])
        
    def openInstaYashas(self):
        
        webbrowser.open('https://www.instagram.com/yashas1145/')
    
    def openInstaVaishnavi(self):
        
        webbrowser.open('https://www.instagram.com/vyshnavi_upadhya/')
    
    def openLinkedInYashas(self):
        
        webbrowser.open('https://www.linkedin.com/in/yashas-bn-485b6816b/')
    
    def openLinkedInVaishnavi(self):
        
        webbrowser.open('https://www.linkedin.com/in/vaishnavi-upadhya-4563611ba/')
        
    def statusBarClear(self):
        
        clearBar = threading.Timer(3, self.clearStatusBar)
        clearBar.start()
    
    def LabelForUserVerify(self):
        
        clearLabel = threading.Timer(3, self.clearLabelForUserVerify)
        clearLabel.start()
    
    def clearLabelForUserVerify(self):
        
        self.label_4.setText('')
        self.label_61.setText('')
    
    def clearStatusBar(self):
        
        self.statusBar().showMessage('')
        
def main():
    
    Final = QApplication(sys.argv)
    App = Station()
    App.show()
    Final.exec_()

if __name__ == '__main__':
    
    main()
