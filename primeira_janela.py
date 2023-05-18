import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QPushButton

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        self.carregar_janela()

    botao1 = QPushButton('Ligar', self)
    botao1.move(100, 100) #posição dentro da janela
    botao1.resize(150, 50) #O BOTÃO DEVE SER CRIADO ANTES DE CHAMAR A JANELA...

    botao1.clicked.connect(self.botao1_click)

    self.carregar_janela()

def botao1_click(self):
    print("LIGADO")


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec())
