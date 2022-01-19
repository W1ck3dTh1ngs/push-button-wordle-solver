from previous_letters import wrong_letters, misplaced_letters, correct_letters
from all_word_values_calculator import sort_words


def find_next_word():
  sorted_words = sort_words()
  misplaced_letters_flat = [item for sublist in misplaced_letters for item in sublist]
  
  # return the highest value word if we haven't guessed yet
  if not any([wrong_letters, misplaced_letters, correct_letters]):
    return sorted_words[0]
  
  for word in sorted_words:
    misplaced = False
    wrong = False
    missing_correct = False

    # skip if we don't find our misplaced letters
    if misplaced_letters != ['', '', '', '', ''] and not [char for char in word if char in misplaced_letters]:
      continue
      
    for idx, char in enumerate(word):
      # skip if we find a wrong letter in the word
      if char in wrong_letters:
        wrong = True
        break
      # skip if we find a letter in the wrong place
      if char in misplaced_letters[idx]:
        misplaced = True
        break
      # skip if we don't find our correct letters
      if correct_letters[idx] and correct_letters[idx] != char:
        missing_correct = True
        break

    # with all of that checked, return our highest ranking valid word (which will prematurely exit the loop)
    if not any([misplaced, wrong, missing_correct]):
      return word
