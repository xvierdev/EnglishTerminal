import random
from views import funcs


def date_translation_game():
    """
    A game where the player translates abbreviated dates from Portuguese to full English dates.
    """

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    def number_to_ordinal(n):
        """Converts an integer to its ordinal form in English."""
        if 10 <= n % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return str(n) + suffix

    score = 0
    lives = 5

    print("Welcome to the Date Translation Game!")
    print("You have 5 lives. Good luck!")

    while lives > 0:
        day = random.randint(1, 28)  # Simplifying to avoid issues with 30/31 day months
        month_num = random.randint(1, 12)
        month_en = months[month_num]

        date_pt = f"{day}/{month_num}"
        correct_translation = f"{month_en} {number_to_ordinal(day)}"

        answer = input(f"\nTranslate the date '{date_pt}' to full English: ")

        score, lives = funcs.total_score(score, lives, answer, correct_translation)

        if lives == 0:
            break
