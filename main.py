from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Janela da Nicole"
        self.condicao = "Desligado"

        botao1 = QPushButton("Ligar", self)
        botao1.move(240, 330)
        botao1.resize(150, 50)

        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton("Desligar", self)
        botao2.move(390, 330)
        botao2.resize(150, 50)

        botao2.clicked.connect(self.botao2_click)

        self.label1 = QLabel(self)
        self.label1.setText(self.condicao)
        self.label1.move(345, 270)
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px;color: "red";}')
        self.label1.resize(150, 50)

        self.label = QLabel(self) 
        self.pixmap = QPixmap('lua.png') 
        self.label.setPixmap(self.pixmap) 
        self.label.resize(256, 256)
        self.label.move(270, 20)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(240, 400)
        self.caixa_texto.resize(150, 25)

        botao_leitura = QPushButton("LEIA", self)
        botao_leitura.move(390, 400)
        botao_leitura.resize(150, 25)

        botao_leitura.clicked.connect(self.leitura)

        self.carregar_janela()
        

    def carregar_janela(self):
        
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        
        self.show()

    def botao1_click(self):
        self.condicao = "Ligado"
        self.label1.setText(self.condicao)
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px;color: "green"}')
        self.pixmap = QPixmap('sol.png') 
        self.label.setPixmap(self.pixmap) 

    def botao2_click(self):
        self.condicao = "Desligado"
        self.label1.setText(self.condicao)
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px;color: "red"}')
        self.pixmap = QPixmap('lua.png') 
        self.label.setPixmap(self.pixmap) 

    def leitura(self):
        texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        self.label1.setText(texto)
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px;color: "blue"}')
        
        
if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec())
