text = input("ievadit tekstu: ")
def replaceO (text):
  if text.count("o")>0 or text.count("O")>0:
    text = text.replace("o","%")
    text = text.replace("O","%")
    print(text)
  else:
    text = "Nav burtu O vai o."
    return text
    print(text)
replaceO (text)