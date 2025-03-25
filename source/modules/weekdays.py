import random
import unicodedata

def weekday_translation_game():
    """
    A simple game where the player translates the days of the week from English to Portuguese.
    """

    weekdays = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    english_weekdays = list(weekdays.keys())
    score = 0
    lives = 5

    print("Welcome to the Weekday Translation Game!")
    print("You have 5 lives. Good luck!")

    while lives > 0:
        english_day = random.choice(english_weekdays)
        correct_translation = weekdays[english_day]

        answer = input(f"\nTranslate '{english_day}' to Portuguese: ")

        # Remove acentos e converte para minúsculas para comparação
        answer_normalized = ''.join(c for c in unicodedata.normalize('NFD', answer) if unicodedata.category(c) != 'Mn').lower()
        correct_normalized = ''.join(c for c in unicodedata.normalize('NFD', correct_translation) if unicodedata.category(c) != 'Mn').lower()

        if answer_normalized == correct_normalized:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is '{correct_translation}'.")
            lives -= 1
            print(f"Lives remaining: {lives}")

    print(f"\nGame over! Your score: {score}.")
    if lives == 0:
        print("You lost all your lives!")
    return score

if __name__ == "__main__":
    weekday_translation_game()