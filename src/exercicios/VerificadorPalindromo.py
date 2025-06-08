class VerificadorPalindromo:
    def eh_palindromo(self, texto):
        texto = texto.replace(" ", "").lower()
        return texto == texto[::-1]


if __name__ == "__main__":
    verificador = VerificadorPalindromo()
    palavra = input("Digite uma palavra ou frase: ")
    if verificador.eh_palindromo(palavra):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
