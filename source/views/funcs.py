import unicodedata, time

def total_score(score, lives, answer, correct_translation):
    # Remove acentos e converte para minúsculas para comparação
    answer_normalized = ''.join(c for c in unicodedata.normalize('NFD', answer) if unicodedata.category(c) != 'Mn').lower()
    correct_normalized = ''.join(c for c in unicodedata.normalize('NFD', correct_translation) if unicodedata.category(c) != 'Mn').lower()

    if answer_normalized == correct_normalized:
        score += 1
        print(f'{correct_normalized} is correct!')
        print(f'Score = {score} points')
    else:
        lives -= 1
        print(f'Incorrect. The correct translation is \'{correct_translation}\'.')
        print(f'Lives remaining: {lives}')
        
    if lives == 0:
            print('You lost all your lives!')
            print(f'\nGame over! Your score: {score}.')
            time.sleep(2)
            return score, lives
    
    return score, lives