word = input()
word_list = []
for i in range(len(word)):
  if word[i].isupper() == True:
    word_list.append(word[i].lower())
  else:
    word_list.append(word[i].upper())
print(''.join(word_list))