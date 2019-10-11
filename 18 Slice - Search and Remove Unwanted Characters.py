sentence = "@@@The quick brown fox jumped over the lazy dog###"
print(sentence)

start = sentence.find('@@@')
stop = sentence.find('###')

print('-'*30)
print('Extracted Sentence without the Junk Characters')
print(sentence[start+3:stop:1])

# The above code extract the Setence without the Junk Characters