import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira janela"
        self.label = QLabel("Aperte o botão", self)

        botao1 = QPushButton('Ligar', self)
        botao1.move(350, 300)
        botao1.resize(100, 40)
        botao1.setStyleSheet("background-color: lightblue;"
                             "border: 1px solid lightblue;"
                             "font-weight: bold;"
                             "font-family: Arial;"
                             "border-radius: 3px;"
                             "letter-spacing: 2px;"
                             "font-size: 14px;")

        botao1.clicked.connect(self.botao_1_click)

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_1_click(self):
        print("Ligado")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    j = Janela()
    sys.exit(app.exec())
