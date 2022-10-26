import unittest
from documentReader import DocumentReader
from userFunctions import Map, Reduce

class TestDocumentReader(unittest.TestCase):
  texts = DocumentReader("beemovie.pdf")
  list = Map(texts)

  global map
  map = Reduce(list)

  def test_wordInDoc(self):
    key = "jazz"
    pages = [2]
    self.assertEqual(map[key],pages)

  def test_wordNotInDoc(self):
    with self.assertRaises(Exception):
      key = "Shrek"
      print(map[key])


if __name__ == '__main__':
    unittest.main()