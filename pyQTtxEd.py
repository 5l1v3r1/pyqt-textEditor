#! python3
#[I] Date: 2019/2/10
#[N] Simple TextEditor Using PyQt5 Library
#[F] Coded By: Oseid Aldary
#[O] Thanks For Usage :)
########################################### 
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon
import webbrowser,os

class pyQTtxEd(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.copiedtext=""
        self.initUI()
        
    def initUI(self):               
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


        exitAction = QAction(QIcon("ICONS"+os.sep+"exit.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        newAction=QAction(QIcon("ICONS"+os.sep+"new.png"),'New',self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New Application')
        newAction.triggered.connect(self.__init__)
        
        openAction=QAction(QIcon("ICONS"+os.sep+"open.png"),'Open',self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Application')
        openAction.triggered.connect(self.openo)
        
        saveAction=QAction(QIcon("ICONS"+os.sep+"save.png"),'Save',self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Application')
        saveAction.triggered.connect(self.save)
        
        undoAction=QAction(QIcon("ICONS"+os.sep+"undo.png"),'Undo',self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.setStatusTip('Undo')
        undoAction.triggered.connect(self.textEdit.undo)
        
        redoAction=QAction(QIcon("ICONS"+os.sep+"redo.png"),'Redo',self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.setStatusTip('Undo')
        redoAction.triggered.connect(self.textEdit.redo)
        
        copyAction=QAction(QIcon("ICONS"+os.sep+"copy.png"),'Copy',self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.setStatusTip('Copy')
        copyAction.triggered.connect(self.copy)
        
        pasteAction=QAction(QIcon("ICONS"+os.sep+"paste.png"),'Paste',self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.setStatusTip('Paste')
        pasteAction.triggered.connect(self.paste)
        
        cutAction=QAction(QIcon("ICONS"+os.sep+"cut.png"),'Cut',self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut')
        cutAction.triggered.connect(self.cut)
        
        aboutAction=QAction('About',self)
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.about)
        
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        fileMenu2=menubar.addMenu('&Edit')
        fileMenu2.addAction(undoAction)
        fileMenu2.addAction(redoAction)
        fileMenu2.addAction(cutAction)
        fileMenu2.addAction(copyAction)
        fileMenu2.addAction(pasteAction)
        fileMenu3=menubar.addMenu('&Help')
        fileMenu3.addAction(aboutAction)
        
        tb1 = self.addToolBar('File')
        tb1.addAction(newAction)
        tb1.addAction(openAction)
        tb1.addAction(saveAction)
        
        tb2 = self.addToolBar('Edit')
        tb2.addAction(undoAction)
        tb2.addAction(redoAction)
        tb2.addAction(cutAction)
        tb2.addAction(copyAction)
        tb2.addAction(pasteAction)
        
        tb3 = self.addToolBar('Exit')
        tb3.addAction(exitAction)
        
        self.setGeometry(0,0,600,600)
        self.setWindowTitle('pyQTtxEd - Text Editor')    
        self.setWindowIcon(QIcon("ICONS"+os.sep+"icon.png")) 
        self.show()
    
        
    def closeEvent(self, event):
        if self.textEdit.document().isEmpty() == True:
            self.statusBar().showMessage('Quiting...')
            event.accept()
        else:
            reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit without Saving?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.statusBar().showMessage('Quiting...')
                event.accept()
            else:
                event.ignore()
            
    def openo(self):
        self.statusBar().showMessage('Open Text Files ')
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), "*.txt")[0]
        self.statusBar().showMessage('Open File')
        if fname =="":
            return
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)

    def save(self):
        self.statusBar().showMessage('Add extension to file name')
        fname =QFileDialog.getSaveFileName(self, 'Save File', os.getcwd(), "*.txt")[0]
        data=self.textEdit.toPlainText()
        if fname !="":
            if not fname.endswith(".txt"):fname=fname+".txt"
            file=open(fname,'w')
            file.write(data)
            file.close()
    
    def copy(self):
        cursor=self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedtext=textSelected
        self.textEdit.copy()
    def paste(self):
        self.textEdit.append(self.textEdit.paste())
    
    def cut(self):
        cursor=self.textEdit.textCursor()
        textSelected=cursor.selectedText()
        self.copiedtext=textSelected
        self.textEdit.cut()
    
    def about(self):
        url ="https://en.wikipedia.org/wiki/Text_editor"
        self.statusBar().showMessage('Loading url...')
        webbrowser.open(url) 
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = pyQTtxEd()
    sys.exit(app.exec_())
