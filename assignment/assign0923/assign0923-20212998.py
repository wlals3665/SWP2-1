# 박윤재-20212998
import pickle

dfn= 'SkuldNorniern-20212998.dat'

def ReadSDB():
    try:
        fH = open(dfn, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dfn)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("DB is Empty: ", dfn)
    else:
        print("Open DB: ", dfn)
    fH.close()
    return scdb

def WriteSDB(scdb):
    fH = open(dfn, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def ShowSDB(scdb, keyn):
    for p in sorted(scdb, key=lambda person: person[keyn]):
        for attr in sorted(p):
            print(f"{attr}={p[attr]}", end=' ')
        print()

def DoSDB(scdb):
    while(True):
        try:
            inputstr = (input("Score DB > "))
            if inputstr == "":
                continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                if len(parse) < 4:
                    raise Exception('Input the name, age, score.')
                if not (parse[2].isdigit() and parse[3].isdigit()):
                    raise Exception('Input of the age and score must be in integer form.')
                record = {'Name': parse[1], 'Age': int(parse[2]),'Score': int(parse[3])}
                scdb += [record]
            elif parse[0] == 'del':
                if len(parse) < 2:
                    raise Exception('Input name for del.')
                for p in reversed(scdb):
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                ShowSDB(scdb, sortKey)
            elif parse[0] == 'find':
                if len(parse) < 2:
                    raise Exception('Input name to find.')
                target_scdb = []
                for p in scdb:
                    if p['Name'] == parse[1]:
                        target_scdb.append(p)
                ShowSDB(target_scdb, 'Age')
            elif parse[0] == 'inc':
                if len(parse) < 3:
                    raise Exception('Input name and the amount to inc.')
                if not parse[2].isdigit():
                    raise Exception('Imput amount in integer form to inc.')
                for p in scdb:
                    if p.get('Name') == parse[1]:
                        p['Score'] += int(parse[2])
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
        except Exception as e:
            print('[Error]', e)

sdb = ReadSDB()
DoSDB(sdb)
WriteSDB(sdb)
