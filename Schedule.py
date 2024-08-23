import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QCalendarWidget, QTableWidget, QHeaderView, QTableWidgetItem
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ConfigUI()
    
    def ConfigUI(self):
        self.setWindowTitle('Schedule')
        
        self.setFixedSize(1200, 600)
        
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

        self.calendar.selectionChanged.connect(self.GetDates)
        

        self.label = QLabel(self)
        self.label.setGeometry(240, 30, 550, 50)

        self.LabelPreviousDays = QLabel(self)
        self.LabelPreviousDays.setGeometry(250, 100, 200, 50)

        self.LabelNextDays = QLabel(self)
        self.LabelNextDays.setGeometry(600, 100, 200, 50)

        self.LabelSelectDay = QLabel(self)
        self.LabelSelectDay.setGeometry(500, 100, 50, 50)
        
        self.gradetext = QTableWidget(self)

        self.gradetext.setGeometry(220, 80, 950, 450)

        self.gradetext.setColumnCount(7)

        self.gradetext.setRowCount(24)

        self.gradetext.setHorizontalHeaderLabels([''] * 7)

        self.gradetext.setVerticalHeaderLabels(f'{tempo}:00'for tempo in range(24))

        for coluna in range(7):
            for linha in range(24):
                self.gradetext.setRowHeight(linha, 50)

        headerHorizontal = self.gradetext.horizontalHeader()
        headerHorizontal.setSectionResizeMode(QHeaderView.Stretch)

    def getNameMonth(self, Month):
        Months = {
            1: "Janeiro",
            2: "Fevereiro", 
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }
        return Months.get(Month)

    def GetDates(self):
        SelectDate = self.calendar.selectedDate()
        
        Day = SelectDate.day()
        Month = SelectDate.month()
        Year = SelectDate.year()

        NameMonth = self.getNameMonth(Month)

        self.label.setObjectName('k')
        self.applyStylesheet(self.label, 'Organizador_de_Tarefas\StyleSchedule.css')
        
        previous_dates = [SelectDate.addDays(-i) for i in range(3, 0, -1)]

        next_dates = [SelectDate.addDays(i) for i in range(1, 4)]

        for item, date in enumerate(previous_dates + [SelectDate] + next_dates):
            self.gradetext.setHorizontalHeaderItem(item, QTableWidgetItem(date.toString("ddd d/MM")))
        
        self.label.setText(f'{NameMonth} {previous_dates[-3].toString("d")} - {next_dates[-1].toString("d")}, {Year}')


    def Schedule(self):
        print('oi')
    
    def applyStylesheet(self, widget, filename="assets/StyleSchedule.css"):
        try:
            # Obtém o diretório onde o script está localizado
            base_dir = os.path.dirname(os.path.abspath(__file__))

            # Constrói o caminho absoluto para o arquivo CSS
            filepath = os.path.join(base_dir, filename)
            
            with open(filepath, "r") as f:
                widget.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Arquivo {filepath} não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao abrir o arquivo: {e}")

def Main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()