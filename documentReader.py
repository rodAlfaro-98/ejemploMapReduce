import PyPDF2
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS

def DocumentReader(docName: str) -> list:
  nlp = English()

  reader = PyPDF2.PdfReader(docName)
  number_of_pages = len(reader.pages)

  texts = []
  for i in range(0,number_of_pages):
      # creating a page object
      page = reader.pages[i]
      text = page.extract_text()
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
  return texts