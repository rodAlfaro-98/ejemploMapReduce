import PyPDF2
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS

def Map(documents):
    list = []
    for i in range(len(documents)):
        for j in documents[i]:
            pair = (j,i)
            list.append(pair)
    return list

def Reduce(list):
    map = {}
    for i in list:
        words = i[0].split(' ')
        #print(words)
        for j in words:
            if j in map.keys():
                map[j].append(i[1])
            else:
                map[j] = [i[1]]
    return map

nlp = English()

reader = PyPDF2.PdfReader("beemovie.pdf")
number_of_pages = len(reader.pages)

texts = []
for i in range(0,number_of_pages):
    # creating a page object
    page = reader.pages[i]
    text = page.extract_text()
    list_aux = []
    word_category = []
    for j in text.split('\n'):
        j = j.split(' ')
        for k in j:
            doc = nlp(k)
            for token in doc:
                word_category.append(token.text)

    palabras_final = []
    for word in word_category:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False and word not in ['.',',','!','?','"']:
            palabras_final.append(word.lower())
    
    # extracting text from page
    texts.append(palabras_final)

# closing the pdf file object
list = Map(texts)
map = Reduce(list)
while True:
    key = input("Ingrese palabra a buscar en el script en inglés de Bee Movie\n$ ")
    print("Páginas en las que aparece la palabra:")
    try:
        print(map[key])
    except:
        print("La palabra {} no se encuentra en el script".format(key))
    continuar = input("Desea ingresar otra palabra? [y/n]\n$ ")
    if continuar.lower() != 'y':
        continuar = input("Desea ver el índice ordenado? [y/n]\n$ ")
        if continuar.lower() == 'y':
            sorted=sorted(map.keys(), key=lambda x:x.lower())
            for key in sorted:
                print("{0}: {1}".format(key,map[key]))
        else:
            break