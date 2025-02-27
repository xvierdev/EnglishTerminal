import random

def jogo_traducao_numeros():
    """
    Jogo para treinar a tradução de números de 0 a 1000 para inglês.
    """

    def numero_para_ingles(n):
        """
        Função auxiliar para converter um número inteiro de 0 a 1000 para inglês.
        """
        unidades = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        dezenas_especiais = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        dezenas = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if n == 0:
            return "zero"
        elif n < 10:
            return unidades[n]
        elif n < 20:
            return dezenas_especiais[n - 10]
        elif n < 100:
            dezena = dezenas[n // 10]
            unidade = unidades[n % 10]
            return dezena + (("-" + unidade) if unidade else "")
        elif n < 1000:
            centena = unidades[n // 100]
            resto = n % 100
            if resto == 0:
                return centena + " hundred"
            else:
                return centena + " hundred and " + numero_para_ingles(resto)
        elif n == 1000:
            return "one thousand"
        else:
            return "Número fora do intervalo (0-1000)."

    pontuacao = 0
    num_rodadas = 5  # Número de rodadas do jogo

    print("Bem-vindo ao Jogo de Tradução de Números (0-1000)!")

    for i in range(num_rodadas):
        numero = random.randint(0, 1000)
        traducao_correta = numero_para_ingles(numero)

        resposta = input(f"\nTraduza o número '{numero}' para inglês: ")

        if resposta.lower() == traducao_correta.lower():
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto. A tradução correta é '{traducao_correta}'.")

    print(f"\nFim do jogo! Sua pontuação: {pontuacao} de {num_rodadas}.")