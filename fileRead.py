import time
from csv import reader
from formSubmitter import submitResponse

# Constants
indexFileName = "currentIndex.txt"
dataFileName = "maribCSV - Sheet1.csv"

def readIndex():
    fileReader = open(indexFileName,"r")
    index = fileReader.read()
    fileReader.close() 
    return int(index)


def incrementIndex(index):
    fileWriter = open(indexFileName, "w")
    fileWriter.write(str(index+1))
    fileWriter.close()


# for x in range(100):
#     index = readIndex()
#     time.sleep(1)
#     incrementIndex(index)

def getResponseList():
    csvFile = open(dataFileName, 'r')
    csv_reader = reader(csvFile)
    header = next(csv_reader)
    responseList = []
    if header != None:
        for response in csv_reader:
            responseList.append(response)
    return responseList




startIndex = readIndex()

responseList = getResponseList()
for currIndex, response in enumerate(responseList[startIndex:]):
    print(response)
    submitResponse(response)
    incrementIndex(startIndex+currIndex)
    time.sleep(2)