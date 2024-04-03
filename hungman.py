""""
hanging man game

the progress of the game:
The player needs to enter (1) a path to a word file and (2) a position (index) for a word in the file.
In accordance with the input from the player, the secret word for the game will be selected.
The player will be shown the appropriate state of the hanging man based on his number of failed attempts.
At the beginning of the game, the opening state (the first of the seven states, i.e.
the horizontal line of the rack) will be displayed.
Below the hanging man,
the secret word will be presented to the player in the structure of underscores (with spaces).
The player has to input one character each round.
If the character is not correct (two characters or more and/or is not an English letter,
or it was guessed before), an "X" will be printed to the screen,
and the list of letters that have already been guessed in the past will be printed (as a string of lowercase letters,
sorted from lower to upper and separated by arrows) the player will enter another character until Confirm that the
character to be typed will be correct.
After each correct guess, the secret word will be presented to the player in the structure of underscores (even if he
guessed partially or has not yet been able to guess at all).
In case of a failed guess - the output will be printed :( and below it will be printed a picture of the hanging man
in a more "advanced" state.

End of the game:
If the player guessed the whole word correctly - WIN will be printed to the screen.
If the player guessed six failed attempts - LOSE will be printed to the screen.

Thank you!

Tzvi gafni
tzvigafni@gmail.com
0548425660
"""


def print_the_splash_screen():
    """ Print welcome and logo and num of max tries
    """
    HANGMAN_ASCII_ART = r"""
    Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    """
    print(HANGMAN_ASCII_ART)
    # num of life
    MAX_TRIES = 6
    print('Max tries - ', MAX_TRIES)


def choose_word(file_path: str, index: int) -> str:
    """ The function returns the word at index position,
    which will be used as the secret word for guessing.
    :param file_path: string representing a path to a text file containing space-separated words.
    :param index: An integer representing the position of a particular word in the file.
    :type file_path: str
    :type index: int
    :return: secret word
    :rtype: str
    """
    spells_input_file = open(file_path, "r")
    lines = spells_input_file.read().split()
    while index > len(lines):
        ''' If the position (index) is greater than the number of words in the file, 
        the function continues to count positions in a circular fashion
        '''
        index -= len(lines)
    secret_word = lines[index - 1]
    spells_input_file.close()
    return secret_word.lower()


def check_valid_input(letter_guessed: str, old_letters_guessed: list) -> bool:
    """ Check if valid input -
    1. length of letter_guessed is only 1
    2. letter_guessed only between a and z
    3. letter_guessed not in old_letters_guessed
    :param letter_guessed: letter guessed value
    :param old_letters_guessed: list old letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
    if len(letter_guessed) == 1 and 'a' <= letter_guessed <= 'z' and letter_guessed not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list, secret_word: str) -> bool:
    """" This function checks 3 options:
    1. If the input is correct and the letter is indeed found in the secret word that needs to be guessed,
     the letter will be added to the list of letters already guessed, and the function will return true.
    2. If the input is correct and the letter is not in the secret word that needs to be guessed,
     the letter will be added to the list of already guessed letters,
     a crying smiley will be printed, and a false will be returned.
    3. If the input is incorrect, X will be printed,
     and in addition, if the letter is already in the list of previous letters guessed,
     the list of letters already guessed will be printed sorted and separated by ->,
     and true will be returned.
    In the main function we will increment the value of num_of_tries when false is returned.
    :param letter_guessed: letter guessed value
    :param old_letters_guessed: list old letters guessed
    :param secret_word: secret word
    :type letter_guessed: str
    :type old_letters_guessed: list
    :type secret_word: str
    :return: True or False
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        # check if letter_guessed in secret_word
        if check_if_letter_in_secret_word(letter_guessed, secret_word):
            old_letters_guessed.append(letter_guessed)
            return True
        else:
            old_letters_guessed.append(letter_guessed)
            print(' :( ')
            # In the main function we will increment the value of num_of_tries when false is returned.
            return False
    else:
        print('X')
        if letter_guessed in old_letters_guessed:
            if len(old_letters_guessed) == 1:
                print('The letter you already guessed is - ', old_letters_guessed[0])
            else:
                print('The letters you already guessed are ', *sorted(old_letters_guessed), sep=' -> ')
        return True


def check_if_letter_in_secret_word(letter_guessed: str, secret_word: str) -> bool:
    """" Check if letter guessed in secret word
    :param letter_guessed: letter guessed value
    :param secret_word: secret word value
    :param secret_word: secret word
    :type letter_guessed: str
    :type secret_word: str
    :return: True or False
    :rtype: bool
    """
    if letter_guessed in secret_word:
        return True
    else:
        return False


def show_hidden_word(secret_word: str, old_letters_guessed: list):
    """" A function that prints the hidden word at all stages of the game,
     when every time a letter is added it is revealed,
     and the rest of the letters are displayed as an underscore.
    :param secret_word: secret word
    :param old_letters_guessed: list old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    """
    hidden_word = '\n'
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            hidden_word += secret_word[i]
            hidden_word += ' '
        else:
            hidden_word += '_ '
    print(hidden_word)


def check_win(secret_word: str, old_letters_guessed: list) -> bool:
    """" A function that checks in every move whether it has found all the letters of the secret word.
    :param secret_word: secret word
    :param old_letters_guessed: list old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    """
    count = 0
    for i in old_letters_guessed:
        if i in secret_word:
            count += 1

    if count == len(secret_word):
        return True
    else:
        return False

#  tuple that holds the hangman snapshot
HANGMAN_PHOTOS = {
    '0': r'x-------x',
    '1': r'''    
    x-------x
    |
    |
    |
    |
    |''',
    '2': r'''
    x-------x
    |       |
    |       0
    |
    |
    |
    ''',
    '3': r'''
    x-------x
    |       |
    |       0
    |       |
    |
    |
    ''',
    '4': r'''
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    ''',
    '5': r'''
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    ''',
    '6': r'''
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    '''
}


def print_hangman(num_of_tries: int):
    """" A function that prints the state of the hanging man in every move of the game.
    The fuller the man - the closer to losing the game.
    :param num_of_tries: the number of tries the user has performed so far.
    :type num_of_tries: int
    """
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def main():
    """" Main function
    """
    print_the_splash_screen()
    file_path = input('Enter file path: ')
    i = int(input('Enter index: '))
    print('\nLet\'s start!\n')
    secret_word = choose_word(file_path, i)
    num_of_tries = 0  # Number of failed user attempts
    old_letters_guessed = []  # letters that the player has already guessed
    print_hangman(num_of_tries)
    print('\n Secret word is - ', "_ " * len(secret_word))
    # loop ran as long as the attempts were not over and there was no victory
    while num_of_tries < 6 and not (check_win(secret_word, old_letters_guessed)):
        letter_guessed = input("\nPlease enter a letter: ").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
            show_hidden_word(secret_word, old_letters_guessed)
        else:
            num_of_tries += 1
            print_hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters_guessed)
    if check_win(secret_word, old_letters_guessed):
        print("  --- WIN ---")
    else:
        print("  --- LOSE ---")

if __name__ == "__main__":
    main()
