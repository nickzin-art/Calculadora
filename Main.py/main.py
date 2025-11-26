from PyQt5.QtWidgets import QApplication
from view.TelaExemplo import TelaPrograma

if __name__ == "__main__":
    app = QApplication([])

    tela = TelaPrograma()
    app.exec_()


