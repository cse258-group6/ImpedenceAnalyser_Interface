'''
Created on 05-Feb-2015

@author: Husain Haidery
'''


import sys
from PyQt4 import QtGui, QtCore

class Guiclass(QtGui.QMainWindow):
    
    def __init__(self):
        super(Guiclass, self).__init__()
        self.initUI()
                
    def initUI(self):               
        
        exitAction = QtGui.QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        menubar = self.menuBar()
        FMenu = menubar.addMenu('&File')
        CMenu = menubar.addMenu('&Connect')
        FMenu.addAction(exitAction)
        entry1 = CMenu.addAction('Connect')
        entry2 = CMenu.addAction('&con')
        self.connect(entry1,QtCore.SIGNAL('triggered()'),  lambda: self.connectionfunc())
        self.connect(entry2,QtCore.SIGNAL('triggered()'),  lambda: self.connectionfunc2())
        CMenu.addAction(entry1)
        CMenu.addAction(entry2)
        
        self.setWindowTitle('Interface:IA')    
        self.showMaximized()
        self.show()
    
    def connectionfunc(self):
        print('husain')    
    
    def connectionfunc2(self):
        print('hhhusain')    
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Guiclass()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  