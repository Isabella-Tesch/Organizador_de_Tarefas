import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QCalendarWidget

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
        
        EventArquivo = QAction('Nova Tarefa', self)
        EventArquivo.triggered.connect(self.Schedule)
        ItemMenu.addAction(EventArquivo)

        menubar.setObjectName('ItemMenuArquivo')

        self.applyStylesheet(menubar, "Organizador_de_Tarefas/StyleSchedule.css")

        self.calendar = QCalendarWidget(self)

        self.calendar.setGeometry(10, 50, 200, 200)
        
        self.calendar.setStyleSheet('background-color: lightblue; color: black;')

        self.calendar.selectionChanged.connect(self.Schedule)

        self.label = QLabel(self)
        self.label.setGeometry(300, 50, 200, 200)
    
    def Schedule(self):
        SelectDate = self.calendar.selectedDate()
        
        Day = SelectDate.day()
        Month = SelectDate.month()
        Year = SelectDate.year()

        self.label.setText(f'{Day}/{Month}/{Year}')
        print(Day, Month, Year)
    
    def applyStylesheet(self, widget, filename):
        with open(filename, "r") as f:
            widget.setStyleSheet(f.read())
        


def Main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()