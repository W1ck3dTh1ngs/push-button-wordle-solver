from position_values import position_values


def word_value_summer(word):
  score = 0
  letters = []
  for index, letter in enumerate(word):
    if letter not in letters:
      score += position_values[index][letter]
      letters.append(letter)

  return score