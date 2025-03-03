import random
import unicodedata

def date_translation_game():
    """
    A game where the player translates abbreviated dates from Portuguese to full English dates.
    """

    months = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    def number_to_ordinal(n):
        """Converts an integer to its ordinal form in English."""
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
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

        # Remove accents and convert to lowercase for comparison
        answer_normalized = ''.join(c for c in unicodedata.normalize('NFD', answer) if unicodedata.category(c) != 'Mn').lower()
        correct_normalized = ''.join(c for c in unicodedata.normalize('NFD', correct_translation) if unicodedata.category(c) != 'Mn').lower()

        if answer_normalized == correct_normalized.lower():
            print(f"Correct! The correct translation is '{correct_translation}'.")
            score += 1
        else:
            print(f"Incorrect. The correct translation is '{correct_translation}'.")
            lives -= 1
            print(f"Lives remaining: {lives}")

    print(f"\nGame over! Your score: {score}.")
    if lives == 0:
        print("You lost all your lives!")

if __name__ == "__main__":
    date_translation_game()