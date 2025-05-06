
def translate_pronouns():
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
    print("Welcome to the Pronouns Translator!")
    pronome = ""
    
    while pronome != "q" and pronome != "Q":
        if pronome in pronomes:
            print(f"\n{pronome} é traduzido para {pronomes[pronome]}")
            pronome = input(f"\nType the pronoun: ")
        elif pronome in list(pronomes.values()):
            res = [key for key in pronomes if pronomes[key] == pronome]
            print(f"\n{pronome} é traduzido para {res[0]}")
            pronome = input(f"\nType the pronoun: ")
        else: 
            pronome = input(f"\nType the pronoun: ")