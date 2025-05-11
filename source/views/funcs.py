import unicodedata
import time


def total_score(score, lives, answer, correct_translation):
    # Remove acentos e converte para minúsculas para comparação
    answer_normalized = _nomalize_text(answer)
    correct_normalized = _nomalize_text(correct_translation)

    if answer_normalized == correct_normalized:
        score += 1
        print(f"{correct_normalized} is correct!")
        print(f"Score = {score} points")
    else:
        lives -= 1
        print(f"Incorrect. The correct translation is '{correct_translation}'.")
        print(f"Lives remaining: {lives}")

    if lives == 0:
        print("You lost all your lives!")
        print(f"\nGame over! Your score: {score}.")
        time.sleep(2)
        return score, lives

    return score, lives


def _nomalize_text(text):
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    ).lower()
