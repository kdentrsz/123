def replace(word: str):
  if "o" in word.lower():
    return word.lower().replace("o", "%")
  else:
    return "Nav o"

print(replace("ght2oo3"))
