from word_value_summer import word_value_summer
from valid_words import words


def sort_words():
  words_and_values = {}

  # calculate the value of every valid word
  for word in words:
    value = word_value_summer(word)
    words_and_values[word] = value

  # sort the words by their value in a type that classicly preserves order (so we don't get cucked by future python stuff or whatever)
  sorted_words = sorted(words_and_values.items(), key=lambda item: item[1], reverse=True)
  return [word[0] for word in sorted_words]
