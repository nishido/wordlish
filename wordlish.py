from colored import fg, attr #fg{1} = red, fg{2} = green, fg{3} = yellow, attr('reset') = back to regular
from english_words import english_words_lower_set
from random import choice
# A terminal version of the popular wordle game
# ...just not as good

def get_random_word():
  word_length = 0
  while not(word_length == 5):
    random_word = choice(tuple(english_words_lower_set))
    word_length = len(random_word)
  return random_word.upper()

def check_valid_length(guess):
  valid_guess = False
  if (len(guess) == 5):
    valid_guess = True
  return valid_guess

def check_valid_word(guess):
  valid_guess = True
  if not(guess in english_words_lower_set):
    valid_guess = False
  return valid_guess

def adjust_status(rand_word, guess, status):
  letter_counts = {}
  for letter in rand_word:
    letter_counts[letter] = 0
  for letter in rand_word:
    letter_counts[letter] += 1
  for i in range(5):
    if guess[i] == rand_word[i]:
      status[i] = fg(2)
      letter_counts[guess[i]] -= 1
    elif (guess[i] in rand_word) and (letter_counts[guess[i]] > 0):
      status[i] = fg(3)

def play_wordlish():
  rand_word = get_random_word()
  #print(rand_word)

  turns = 6
  while turns > 0:
    guess = input("Please enter your guess (5 letter word in the english language): ")
    valid_guess = False
    valid_guess = check_valid_length(guess)
    if not(valid_guess == True):
      print(f"I'm sorry, but {guess} is not 5 letters.")
      continue
    valid_guess = check_valid_word(guess)
    if not(valid_guess == True):
      print(f"I'm sorry, but {guess} is not a valid word. You lose one turn.")
      turns -= 1
      continue
    guess = guess.upper()

    status = [fg(1), fg(1), fg(1), fg(1), fg(1)]
    adjust_status(rand_word, guess, status)

    print(f"{status[0]+guess[0]+status[1]+guess[1]+status[2]+guess[2]+status[3]+guess[3]+status[4]+guess[4]+attr('reset')}")
    if (status[0] == fg(2)) and (status[1] == fg(2)) and (status[2] == fg(2)) and (status[3] == fg(2)) and (status[4] == fg(2)):
      print(f"Congratulations! You correctly guessed {guess} in {turns} turns.")
      break
    turns -= 1

  if turns <= 0:
    print(f"Sorry, you have run out of turns. The correct answer was {rand_word}!")
  
  repeat_play = input("Would you like to play again? Y/N: ")
  if (repeat_play.upper() == "Y"):
    play_wordlish()

play_wordlish()


