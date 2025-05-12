import random
import time
from views import funcs


def weekday_translation_game(user):
    """A simple game where the player translates the days of the week from English to Portuguese."""

    weekdays = {
        "Monday": "Segunda",
        "Tuesday": "Terça",
        "Wednesday": "Quarta",
        "Thursday": "Quinta",
        "Friday": "Sexta",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }

    english_weekdays = list(weekdays.keys())
    score = 0
    lives = 5
    answer = ""

    print("Welcome to the Weekday Translation Game!")
    print("You have 5 lives. Good luck!")

    while answer not in ["q", "Q"]:
        english_day = random.choice(english_weekdays)
        correct_translation = weekdays[english_day]

        time.sleep(0.5)
        answer = input(f"\nTranslate '{english_day}' to Portuguese: ")

        score, lives = funcs.total_score(score, lives, answer, correct_translation)

        if lives == 0:
            if user is not None:
                user.add_points(score)
            break
