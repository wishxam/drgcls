import csv
import pickle


path = ['diagdict.csv','operdict.csv']

for i in path:
    with open(i,'r',encoding='gb18030') as f:
        csvfile = csv.reader(f)
        data = dict()
        for row in csvfile:
            data[row[0]] = [row[1],row[2]]
        i_w = i+'dump'
        with open(i_w,'wb') as f_w:
            f_w.write(pickle.dumps(data))


#print(data['Q24.808'])