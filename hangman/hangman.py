import random
from words import words
from hangman_visuals import hangman_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from teh list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    lives = 7
    
    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'c', 'cd']) --> 'a b cd'
        print("You have", lives, "left and already used these letters: ", ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 #Takes away one life if the letter is wrong
                print('\nYour letter, ', user_letter, 'is not in the word.')
            
        elif user_letter in used_letters:
            print("\nYou have already guessed that word. Please, try again.")
        else:
            print("\nInvalid character. Please, try again.")
        
    # The code gets here when the length of the word letters is equal to 0 OR when lives is equal to 0
    if lives == 0:
        print(hangman_visual_dict[lives])
        print("Game lost. The word was", word)
    else:
        print('You guessed the word', word, '!!!')


if __name__ == "__main__":
    hangman()