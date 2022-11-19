from opinionsReader import OpinionsReader
from wordProcessor import WordProcessor

opRead = OpinionsReader('.//resources//opinions.txt', './/resources//stopWords.txt')
opRead.readStopWords()
opRead.readOpinions()
opRead.showOpinions()
opRead.showStopWords()
print('-' * 15)
wProc = WordProcessor(opRead.getOpinions())
wProc.calculateStatistics()
wProc.writeStatistics()