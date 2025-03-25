import random
import unicodedata

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

        # Remove acentos e converte para minúsculas para comparação
        answer_normalized = ''.join(c for c in unicodedata.normalize('NFD', answer) if unicodedata.category(c) != 'Mn').lower()
        correct_normalized = ''.join(c for c in unicodedata.normalize('NFD', correct_translation) if unicodedata.category(c) != 'Mn').lower()

        if answer_normalized == correct_normalized:
            print(f"Correto! A tradução correta é '{correct_translation}'.")
            score += 1
        else:
            print(f"Incorreto. A tradução correta é '{correct_translation}'.")
            lives -= 1
            print(f"Vidas restantes: {lives}")

    print(f"\nFim do jogo! Sua pontuação: {score}.")
    if lives == 0:
        print("Você perdeu todas as suas vidas!")
    return score

if __name__ == "__main__":
    month_translation_game()