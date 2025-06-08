class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b


if __name__ == "__main__":
    calc = Calculadora()
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")

    if op == '+':
        print("Resultado:", calc.somar(a, b))
    elif op == '-':
        print("Resultado:", calc.subtrair(a, b))
    elif op == '*':
        print("Resultado:", calc.multiplicar(a, b))
    elif op == '/':
        print("Resultado:", calc.dividir(a, b))
    else:
        print("Operação inválida.")
