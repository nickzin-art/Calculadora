from funcoes import sum

class Calculadora(QMainWindow):
    def addNumbe(self, number):
        self.display.setText(resultado)
        
    def cleanDisplay(self):
        self.display.setText("0") 
        
    def showResult(self):
        num1 = result = self.display.text()
        num1 = int(num1)
        num2 = 2
        result = sum(num1, num2)
        print(f'numero: {result}')
        print("Tipo:", type(result))