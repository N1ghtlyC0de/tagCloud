class WordProcessor():
  def __init__(self, opinions):
    self.opinions = opinions
    self.wordDic = {}
    self.totalWords = 0

  def calculateStatistics(self):
    self.addWord()
    for op in self.opinions:
      for word in op:
          valF = self.calculateFrecuency(word)
          valR = self.calculateRelevance(word)
          self.wordDic[word] = (valF, valR)
  
  def addWord(self):
    for op in self.opinions:
      self.totalWords += len(op)

  def calculateFrecuency(self, word):
    wordRepet = 0
    for op in self.opinions:
      wordRepet = wordRepet + op.count(word)
    frequency = round(wordRepet * 100 / self.totalWords, 2)
    return frequency 
  
  def calculateRelevance(self, word):
    wordCount = 0
    for op in self.opinions:
      if op.count(word) > 0:
        wordCount = wordCount + 1
    return wordCount
    
  def writeStatistics(self):
    with open('output.txt', 'w', encoding = 'utf-8') as outputF:
      outputList = []
      for key, val in self.wordDic.items():
        outputFormat = key + ',' + ' ' + str(val) + '\n'
        outputList.append(outputFormat)
      outputList.sort()
      for out in outputList:
        outputF.write(out)