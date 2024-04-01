import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ConfigUI()
    
    def ConfigUI(self):
        self.setWindowTitle('Schedule :)')
        
        self.setFixedSize(800, 600)
        
        menubar = self.menuBar()
        
        menubar.setFixedHeight(30)
        
        ItemMenu = menubar.addMenu('Arquivo')
        font = QFont("Times New Roman")
        
        font.setPointSize(12)
        
        font.setBold(True)
        
        menubar.setFont(font)
        
        EventArquivo = QAction('Nova Tarefa', self)
        EventArquivo.triggered.connect(self.x)
        ItemMenu.addAction(EventArquivo)
        
        
        
        #EventArquivo.setFont(font)
    
    def x(self):
        print('oi')
        
        


def Main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()