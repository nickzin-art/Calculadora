from PyQt5.QtWidgets import QMainWindow 
from PyQt5.uic import loadUi
from PyQt5.Qtcore import pyqtSlot

class TelaPrograma(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/.ui", self)
        self.show()
        self.pushButton
        
        
    def MostrarInfo(self):
        contador = 0
        contador += 1
        print(f'vc clicou no botão: {contador}')
    

    @pyqtSlot
    def on_pushButon_clicked(self):
        print("Voce clicou no botão")