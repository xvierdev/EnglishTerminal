import sqlite3
from pathlib import Path
import unicodedata

DB_FILE = Path(__file__).parent.parent / 'db' / "main.db"

def get_random_word(category=None):
    """Returns a random word from the database, filtered by category if provided."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            if category:
                cursor.execute('SELECT english, portuguese FROM Words WHERE category = ? ORDER BY RANDOM() LIMIT 1', (category,))
            else:
                cursor.execute('SELECT english, portuguese FROM Words ORDER BY RANDOM() LIMIT 1')
            word_data = cursor.fetchone()
            if word_data:
                return word_data
            else:
                return None
    except sqlite3.Error as e:
        print(f'Database Error: {e}')
        return None

def normalize_text(text):
    """Normalizes text by removing accents, converts to lowercase, and replaces hyphens with spaces."""
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().replace('-', ' ')

def get_available_categories():
    """Retrieves the list of available categories from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DISTINCT category FROM Words')
            categories = [row[0] for row in cursor.fetchall()]
            return categories
    except sqlite3.Error as e:
        print(f'Database Error: {e}')
        return []

def get_category_word_count(category):
    """Counts the number of words in a specific category."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Words WHERE category = ?', (category,))
            count = cursor.fetchone()[0]
            return count
    except sqlite3.Error as e:
        print(f'Database Error: {e}')
        return 0

def game():
    """Main game loop."""
    points = 0
    lifes = 5
    rounds = 0  # Track the number of rounds played.

    print("Welcome to the Translation Game!\n")

    # Show available categories
    categories = get_available_categories()
    if categories:
        print("Available Categories:")
        for category in categories:
            print(f"- {category}")
        print()

    # Get category choice from the user, converted to lowercase
    category_choice = input("Enter a category to play (or press Enter for any): ").strip().lower()

    # Check if the category exists
    if category_choice and category_choice not in categories:
        print("Category not found. Playing with any category.\n")
        category_choice = None  # If category doesn't exist, set to None

    # Get the word count
    if category_choice:
        category_word_count = get_category_word_count(category_choice)
    else:
        category_word_count = get_category_word_count("") # Get the total word count across ALL categories (if no specific category was selected)

    while lifes > 0:
        word_data = get_random_word(category_choice)
        if word_data:
            english_word, portuguese_phrase = word_data
            expected_answers = [normalize_text(portuguese_phrase)]  # Normalize

            answer = input(f'Translate "{english_word}": ')
            normalized_answer = normalize_text(answer)

            if normalized_answer in expected_answers:
                points += 1
                rounds += 1  # Increment the number of rounds played
                print(f'Correct! You have {points} points!\n')
            else:
                lifes -= 1
                rounds += 1 # Increment the number of rounds played even after incorrect answers
                print(f'Incorrect. The translation of "{english_word}" is "{portuguese_phrase.replace('-',  ' ')}".\n')
                print(f'{lifes} lives remaining.\n')
        else:
            print("Could not retrieve a word from the database.")
            lifes = 0

        # Check if enough rounds have been played
        if category_word_count and rounds >= min(category_word_count, 20) or lifes <= 0:
            #Congratulate if 20 words from a category got asked
            if points >= 2:
                print("Congratulations! You have been asked at least two words from this Category")
                print(f'You earned {points} points!')
            elif points == 1:
                print(f'You earned {points} point!')
            else:
                print('You didn\'t earn any points.')

            print("GAME OVER!")
            print('Better luck next time!')
            break
    return points

if __name__ == '__main__':
    game()