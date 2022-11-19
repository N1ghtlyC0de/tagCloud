class OpinionsReader():
  def __init__(self, opinionsFile, stopWordsFile):
    self.opinionsFile = opinionsFile
    self.stopWordsFile = stopWordsFile
    self.opinions = []
    self.stopWords = set()

  def readOpinions(self):
    with open(self.opinionsFile, 'r', encoding = 'utf-8') as opFile:
      for line in opFile:
        line = line.rstrip('\n').lstrip('¿').rstrip('?').replace(',', '').casefold().strip()
        line = line.split()
        op = ''
        if line:
          for l in line:
            if l not in self.stopWords:
              op += ' ' + l
              op = op.strip()
          self.opinions.append(op.split())
      
  def readStopWords(self):
    with open(self.stopWordsFile, 'r', encoding = 'utf-8') as swFile:
      for line in swFile:
        line = line.strip('\n').split(', ') 
        self.stopWords.update(line)         
        self.stopWords.discard('')         

  def showOpinions(self):
    totalOpinions = len(self.opinions)
    print(totalOpinions, 'OPINIONES')
    for op in self.opinions:
      print(op)
      
  def showStopWords(self):
    totalStopWords = len(self.stopWords)
    print(totalStopWords, 'STOPWORDS')
    for sw in self.stopWords:
      print(sw)

  def getOpinions(self):
    return self.opinions