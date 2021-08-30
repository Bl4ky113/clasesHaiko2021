
VOCALES = ['a', 'e', 'i', 'o', 'u']

class word ():
  def __init__(self) -> None:
    self.word = input("Ingresa una palabra:  ")
    self.info = self.getInfo(self.word)
  
  def getInfo (self, word): 
    info_dict = {} 
    has_vocals = False 
    num_vocals = 0 
    vocals = []
    for char in word:
      if char.lower() in VOCALES:
        has_vocals = True
        num_vocals += 1
        if char.lower() not in vocals:
          vocals += char

    info_dict.update({ "has_vocals": has_vocals, "num_vocals": num_vocals, "vocals": vocals })
    return info_dict

arr_words = []
input_word = word()

while input_word.word != "fin":
  arr_words.append(input_word)
  input_word = word()

for index_word in arr_words:
  if (index_word.info["has_vocals"] == True):
    print(f"La Palabra {index_word.word} Sí tiene Vocales")
    print(f"Tiene {index_word.info['num_vocals']} vocales y son {index_word.info['vocals']}")
  else:
    print(f"La Palabra {index_word.word} No tiene Vocales")