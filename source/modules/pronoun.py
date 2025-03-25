
def translate_pronouns(pronome_ingles):
    """
    Traduz pronomes pessoais do inglês para o português.
    Args:
        pronome_ingles (str): O pronome em inglês.
    Returns:
        str: O pronome traduzido em português, ou None se não encontrado.
    """

    pronomes = {
        "I": "Eu",
        "you": "Você",
        "he": "Ele",
        "she": "Ela",
        "it": "Ele/Ela",  # Para objetos ou animais
        "we": "Nós",
        "they": "Eles/Elas",
    }

    return pronomes.get(pronome_ingles)

if __name__ == '__main__':
    print(translate_pronouns('she'))