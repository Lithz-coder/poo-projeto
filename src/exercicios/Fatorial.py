class Fatorial:
    def calcular(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)


if __name__ == "__main__":
    fat = Fatorial()
    num = int(input("Digite um número inteiro não-negativo: "))
    if num < 0:
        print("Número inválido!")
    else:
        print(f"Fatorial de {num} é {fat.calcular(num)}")
