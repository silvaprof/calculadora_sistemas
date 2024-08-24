from PySide6.QtWidgets import QApplication, QMainWindow
from interface_grafica import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        # Título
        self.setWindowTitle("Calculadora de Sistemas")

        # Botão calcular
        self.pushButton.clicked.connect(self.calcular_resultado)




    # Funções
        
    # Função para calcular a incógnita x
    def calc_x(self, a, b, c, d, e, f):
        try:
            x = (c - (b * ((a * f) - (d * c)) / ((-d * b) + (e * a)))) / a
        except ZeroDivisionError:
            self.exibir_erro("Erro: Valores inválidos.")
        return x

    # Função para calcular a incógnita y
    def calc_y(self, a, b, c, d, e, f):
        try:
            y = ((a * f) - (d * c)) / ((-d * b) + (e * a))
        except ZeroDivisionError:
            self.exibir_erro("Erro: Valores inválidos.")
        return y

    def calcular_resultado(self):
        try:        
            # Coleta as variáveis
            a = float(self.lineEdit_x_1.text())
            b = float(self.lineEdit_y_1.text())
            c = float(self.lineEdit_eq_1.text())
            d = float(self.lineEdit_x_2.text())
            e = float(self.lineEdit_y_2.text())
            f = float(self.lineEdit_eq_2.text())

            # Calcula as incógnitas
            x = self.calc_x(a, b, c, d, e, f)
            y = self.calc_y(a, b, c, d, e, f)

            # Exibe o resultado
            self.exibir_resultado(x, y, a, b, c, d, e, f)
        except ValueError:
            self.exibir_erro("Erro: Valores inválidos.")
        except Exception:
            self.exibir_erro(f"Erro: sistema impossivel ou indeterminado.")

    def exibir_resultado(self, x, y, a, b, c, d, e, f):
        resultado_texto = f"O valor de x é {x:.2f} e o valor de y é {y:.2f}"

        self.label_resposta_2.setText("Resultado: " + resultado_texto)
        
    def exibir_erro(self, mensagem):
        self.label_resposta_2.setText(mensagem)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
