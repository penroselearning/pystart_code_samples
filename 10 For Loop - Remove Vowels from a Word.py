longest_word='pneumonoultramicroscopicsilicovolcanoconiosis'
new_word_without_vowels=''
vowels=['a','e','i','o','u']

for letter in longest_word:
  if letter not in vowels :
    new_word_without_vowels += letter

print(f'The worlds longest word without vowels - {new_word_without_vowels.upper()}')