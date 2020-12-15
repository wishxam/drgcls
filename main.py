import os 
import pickle

f1 = open('diagdict.csvdump','rb')
f2 = open('operdict.csvdump','rb')
drgDiagDict = pickle.loads(f1.read())
drgOperDict = pickle.loads(f2.read())

def DrgClassifier(record):
    
    diagCodeList = []
    diagDesc = []

    operCodeList = []
    operDesc = []
    
    for diagcode in diagCodeList:
        diagDesc = diagDesc.append(FindCode(diagcode, mode='D'))
    
    for opercode in operCodeList:
        operDesc = operDesc.append(FindCode(opercode, mode='O'))





def FindCode(code,mode):

    if mode == 'D':
        if code in drgDiagDict.keys():
            return drgDiagDict[code]
    elif mode == 'O':
        if code in drgOperDict.keys():
            return drgOperDict[code]
    else:
        return 'mode: '+mode+' not exist'
    return 'NotInclude'

if __name__ == '__main__':
    print(FindCode('Q24.808','D')[0])







