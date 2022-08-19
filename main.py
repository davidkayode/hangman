# STEP 5
#TODO 1: import modules from words and art files.
#TODO 2: improve UX
#-----------------------------------------------------------------------------#

import random
import hangman_art, hangman_words # user defined modules

chosen_word = random.choice(hangman_words.word_list)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'The solution is {chosen_word}.')

#Create blanks
display = []
for _ in chosen_word:
    display.append('_')

# run till end of game
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # note repeated guesses
    if guess in display:
        print(f'You\'ve already guessed {guess}.')

    #replace blanks with correct guesses
    count = 0
    for letter in chosen_word:
        
        if letter == guess:
            display[count] = guess
        count += 1
    
    # reduce live for every wrong guess
    if guess not in chosen_word : 
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        
        # end game if no lives left
        if lives == 0: 
            print('You lose!')
            end_of_game = True
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    # print(f'Lives left: {lives}')
    print(hangman_art.stages[lives])

    # check for completion
    if '_' not in display:
        end_of_game = True
        print('You win!')