import random, time
from views import funcs

def month_translation_game():
    """
    Um jogo simples onde o jogador traduz os meses do ano do inglês para o português e vice-versa.
    """

    months_pt_to_en = {
        "Janeiro": "January",
        "Fevereiro": "February",
        "Março": "March",
        "Abril": "April",
        "Maio": "May",
        "Junho": "June",
        "Julho": "July",
        "Agosto": "August",
        "Setembro": "September",
        "Outubro": "October",
        "Novembro": "November",
        "Dezembro": "December"
    }

    months_en_to_pt = {
        "January": "Janeiro",
        "February": "Fevereiro",
        "March": "Março",
        "April": "Abril",
        "May": "Maio",
        "June": "Junho",
        "July": "Julho",
        "August": "Agosto",
        "September": "Setembro",
        "October": "Outubro",
        "November": "Novembro",
        "December": "Dezembro"
    }

    all_months_pt = list(months_pt_to_en.keys())
    all_months_en = list(months_en_to_pt.keys())
    score = 0
    lives = 5
    round = 0 

    print("Bem-vindo ao Jogo de Tradução de Meses!")
    print("Você tem 5 vidas. Boa sorte!")

    while lives > 0:
        if random.choice([True, False]):  # Escolhe aleatoriamente a direção da tradução
            month_pt = random.choice(all_months_pt)
            correct_translation = months_pt_to_en[month_pt]
            answer = input(f"\nTraduza '{month_pt}' para inglês: ")
        else:
            month_en = random.choice(all_months_en)
            correct_translation = months_en_to_pt[month_en]
            answer = input(f"\nTraduza '{month_en}' para português: ")

        score, lives = funcs.total_score(score, lives, answer, correct_translation)
        
        if lives == 0: break