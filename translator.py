import goslate

def Translator(primary_text):
    gs = goslate.Goslate()
    return gs.translate(primary_text, 'fr')

primary_text = input("")
print(Translator(primary_text))
