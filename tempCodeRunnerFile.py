def search (text, word):
  if word in text:
    return "Word found"
  else:
    return "Word not found"
    
text = input("bir metin gir: ")
word = input("bir kelime gir: a")

print(search(text, word))
