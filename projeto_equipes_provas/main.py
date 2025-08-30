import sys
import warnings
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.tela import Ui_MainWindow
from controller.controller import Controller

warnings.filterwarnings("ignore", category=DeprecationWarning)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = Controller()

        # Conectar botão "Cadastrar Equipe"
        self.btnCadastrarEquipe.clicked.connect(self.cadastrar_equipe)

    def cadastrar_equipe(self):
        nome = self.inputNomeEquipe.text()
        membros = self.inputMembros.toPlainText().split("\n")
        self.controller.cadastrar_equipe(nome, membros)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Main()
    janela.show()
    sys.exit(app.exec_())
