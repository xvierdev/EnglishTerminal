import sqlite3
import util
import time
from views import funcs

DB_FILE = util.get_path("main.db")


def get_random_word(category=None):
    """Returns a random word from the database, filtered by category if provided."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            if category:
                cursor.execute(
                    "SELECT english, portuguese FROM Words WHERE category = ? ORDER BY RANDOM() LIMIT 1",
                    (category,),
                )
            else:
                cursor.execute(
                    "SELECT english, portuguese FROM Words ORDER BY RANDOM() LIMIT 1"
                )
            word_data = cursor.fetchone()
            if word_data:
                return word_data
            else:
                return None
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return None


def get_available_categories():
    """Retrieves the list of available categories from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM Words")
            categories = [row[0] for row in cursor.fetchall()]
            return categories
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return []


def get_category_word_count(category):
    """Counts the number of words in a specific category."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Words WHERE category = ?", (category,))
            count = cursor.fetchone()[0]
            return count
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return 0


def game(user=None):
    """Main game loop."""
    score = 0
    lives = 5
    answer = ""

    print("Welcome to the Translation Game!")
    print("Exit Q/q\n")

    # Show available categories
    categories = get_available_categories()
    if categories:
        print("Available Categories:")
        i = 1
        for category in categories:
            print(f"{i} - {category}")
            i += 1
        print()

    # Get category choice from the user, converted to lowercase
    category_choice = (
        input("Enter a category to play (or press Enter for any): ").strip().lower()
    )

    # Check if the category exists
    if category_choice and category_choice not in categories:
        if category_choice.isnumeric() and int(category_choice) <= len(categories):
            category_choice = categories[int(category_choice) - 1]
            print(f"\nCategoria selecionada: {category_choice}")

            while answer not in ["q", "Q"]:
                word_data = get_random_word(category_choice)
                if word_data:
                    english_word, portuguese_phrase = word_data
                    correct_translation = portuguese_phrase  # Normalize

                    time.sleep(0.5)
                    answer = input(f'\nTranslate "{english_word}": ')

                    score, lives = funcs.total_score(
                        score, lives, answer, correct_translation
                    )

                else:
                    print("Could not retrieve a word from the database.")
                    lives = 0

                if lives == 0:
                    if user is not None:
                        user.add_points(score)
                    break

        else:
            print("Category not found.\n")
            category_choice = (
                input("Enter a category to play (or press Enter for any): ")
                .strip()
                .lower()
            )

    # Get the word count
    if category_choice:
        get_category_word_count(category_choice)
    else:
        get_category_word_count("")
