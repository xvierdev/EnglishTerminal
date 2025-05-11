import random
import time
from views import funcs

def number_translation_game():
    """
    Game to practice translating numbers to English with increasing difficulty.
    """

    def number_to_english(n):
        """
        Helper function to convert an integer to English.
        """
        thousands = ["", "thousand", "million"]

        if n == 0:
            return "zero"

        parts = []
        for i in range(3):
            if n % 1000 != 0:
                parts.insert(0, number_to_english_under_1000(n % 1000) + " " + thousands[i])
            n //= 1000

        return " ".join(parts).strip()

    def number_to_english_under_1000(n):
        """
        Helper function to convert an integer from 0 to 999 to English.
        """
        units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            ten = tens[n // 10]
            unit = units[n % 10] if n % 10 != 0 else ""
            return ten + (("-" + unit) if unit else "")
        else:
            hundred = units[n // 100]
            remainder = n % 100
            if remainder == 0:
                return hundred + " hundred"
            else:
                return hundred + " hundred and " + number_to_english_under_1000(remainder)

    score = 0
    lives = 5
    answer = ""
    difficulty_level = 1

    print("Welcome to the Number Translation Game!")
    print("You have 5 lives. Good luck!")
    print("Exit Q/q")

    while answer not in ["q", "Q"]:
        if score >= difficulty_level * 5:
            difficulty_level += 1

        max_range = 10 ** difficulty_level
        number = random.randint(0, max_range)

        correct_translation = number_to_english(number).strip()

        time.sleep(0.5)
        answer = input(f"\nTranslate the number '{number}' to English: ")

        score, lives = funcs.total_score(score, lives, answer, correct_translation)
        
        if (lives == 0):
            break