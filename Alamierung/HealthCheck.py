from Dataset import Dataset
import EvaluateAverage
from Severity import calculateSeverity
    
checkList = []
CHECKLIST_MAX = 10

def main():
    #get Information from db, to fill checkList
    data1 = Dataset(90, 90, 100, 1000, 45, 50, 1)
    listAppend(data1)
    data2 = Dataset(90, 90, 100, 1000, 45, 50, 1)
    listAppend(data2)
    avgDict = EvaluateAverage.evaluateAverage(checkList)
    calculateSeverity(avgDict)

# append to checklist and kicks first element out if length of checklist is larger than CHECKLIST_MAX
def listAppend(data):
    global checkList
    if len(checkList) <= CHECKLIST_MAX: 
        checkList.append(data)
    else:
        checkList = checkList[1:].append(data)

if __name__ == "__main__":
    main()