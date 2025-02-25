import random

def jogo_traducao_dias():
    """
    Um jogo simples onde o jogador traduz os dias da semana em inglês para português.
    """

    dias_da_semana = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    dias_ingleses = list(dias_da_semana.keys())
    pontuacao = 0

    print("Bem-vindo ao Jogo de Tradução dos Dias da Semana!")

    for i in range(5):  # Jogaremos 5 rodadas
        dia_ingles = random.choice(dias_ingleses)
        traducao_correta = dias_da_semana[dia_ingles]

        resposta = input(f"\nTraduza '{dia_ingles}' para português: ")

        if resposta.lower() == traducao_correta.lower():
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto. A tradução correta é '{traducao_correta}'.")

    print(f"\nFim do jogo! Sua pontuação: {pontuacao} de 5.")