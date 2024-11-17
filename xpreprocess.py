import re, warnings
import pandas as pd

warnings.filterwarnings("ignore")

def replaceEmoji(string):
  emoji = {
   '😭': 'menangis',   '👍': 'ok',   '🤫': 'diamlah',   '🥲': 'menangis',   '🤬': 'marah',
   '🙂': 'senyum',   '🥺': 'sedih',   '😌': 'pasrah',   '🙇': 'berserah',   '🤗': 'peluk',
   '✋🏻': 'angkat tangan',   '🔥': 'semangat',   '😅': 'tidak nyaman',   '😞': 'kecewa',  '☹️': "sedih", "😔":"sedih",
   '😋': 'enak',   '💖': 'cinta',   '🤷🏻': 'tidak tahu',   '🙏': 'terima kasih'
  }

  for word in emoji.keys():
    string = string.replace(word, " "+emoji[word])
  return string

def lowercasing(string):
  return string.lower()

def removeTwitterLink(string):
  pattern = '(https://t.co/\w+)'
  return re.sub(pattern, '',string).strip()

def removeRepeatedWords(string):
  pattern = '([A-Za-z]+)[2|²]'
  return re.sub(pattern, r'\g<1>-\g<1>',string).strip()

def removeSlankShortenWords(string):
  slanks = {
      "gini":"begini",
      "aja":"saja",
      "doang": "saja",
      "jgn": "jangan",
      "bkn": "bukan",
      "sampe": "sampai",
      " gak ": "tidak",
      " ga ": "tidak",
      " ndak": "tidak",
      "yg": "yang",
      "ngerasa": "merasa",
      "pengen": "ingin",
      "pingin": "ingin",
      " tau ": "tahu",
      "gimana": "bagaimana",
      "bgt": "sekali",
      "dri": "dari",
      "krn": "karena",
      "banget": "sekali",
      "capek": "lelah",
      "cape": "lelah",
      " nyerah": "menyerah",
      "gue": "aku",
      "gapapa": "tidak apa-apa",
      "gpp": "tidak apa-apa",
      "inget":"ingat",
      " gk ":"tidak",
      "udah":"sudah",
      "bikin":"buat",
      "mikir":"berpikir",
      "beneran":"benar-benar",
      "bener":"benar",
      "dpt":"dapat",
      " nangis":"menangis",
      " lu ": " kamu ",
      "tpi": "tapi"
  }
  for word in slanks.keys():
    pattern = r'([\s|\-])*('+(word)+r')+([\s\-\.\,]+)'
    string = re.sub(pattern, r"\g<1>"+slanks[word]+r"\g<3>", string)
  return string

def removeEnglishContraction(string):
  contractions = {
      "'s": " is",
      "'re": " are",
      "'ll": " will",
      "'m": " am",
      "'ve'": " have",
      "y'all": "you all",
      "haven't": "have not",
      "hasn't": "has not",
      "hadn't": "had not",
      "doesn't": "does not",
      "don't": "do not",
      "didn't": "did not"
  }
  for cont in contractions.keys():
    string = string.replace(cont, contractions[cont])
  return string

if __name__ == "__main__":
  string = "I'll be gini2 doang bisa2 aja gak tau mau gimana lagi"
  print(removeEnglishContraction(removeSlankShortenWords(removeRepeatedWords(replaceEmoji(lowercasing(string))))))
