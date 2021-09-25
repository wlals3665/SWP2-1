# 백연선-20191604
import pickle

dbfilename = 'BaekYeonSun.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
        for p in scdb:
            p['Age'] = int(p['Age'])
            p['Score'] = int(p['Score'])
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb



# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
            except IndexError:
                print("input name, age, score")
            except ValueError:
                print("check name, age, score")
            else:
                scdb += [record]
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'].lower() == parse[1].lower():
                        scdb.remove(p)    
            except IndexError:
                print("input name")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print("Age=" + str(p['Age']), "Name=" + p['Name'], "Score=" + str(p['Score']))
            except IndexError:
                print("input name")
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = int(p['Score'])
                        p['Score'] += int(parse[2])
            except IndexError:
                print("input name, num")
            except ValueError:
                print("check name, num")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            p[attr] = str(p[attr])
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
