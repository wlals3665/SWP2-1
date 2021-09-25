# 박시윤-20212997
import pickle

dbfilename = 'assignment3_20212997.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
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
            if len(parse)>=4:
                try:
                    record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                except ValueError as e:
                    print("입력하신 나이나 점수가 숫자가 아닙니다.")
                    continue
                scdb += [record]
            else:
                print("add의 입력 형식이 옳지 않습니다. (add 이름 나이 점수)")
        elif parse[0] == 'del':
            if len(parse)>=2:
                list = []
                for p in scdb:
                    if p['Name'] != parse[1]:
                        list.append(p)
                scdb=list
            else:
                print("del의 입력 형식이 옳지 않습니다. (del 이름)")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            if (sortKey != 'Name') and (sortKey != 'Age') and (sortKey != 'Score'):
                print("입력하신 키값이 옳지 않습니다. (show 키값(Name/Score/Age))")
                continue
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'inc':
            if len(parse)>=3:
                try:
                    int(parse[2])
                except ValueError as e:
                    print("입력하신 점수의 값이 숫자가 아닙니다.")
                    continue
                for n in scdb:
                    if n['Name'] == parse[1]:
                        n['Score']= int(n['Score'])+int(parse[2])
            else:
                print("inc의 입력 형식이 옳지 않습니다. (inc 이름 추가할점수)")
        elif parse[0] == 'find':
            if len(parse)>=2:
                for n in scdb:
                    if n['Name'] == parse[1]:
                        for attr in sorted(n):
                            print(attr + "=" + n[attr], end=' ')
                        print()
            else:
                print("find의 입력 형식이 옳지 않습니다. (find 이름)")
        elif parse[0] == 'help':
            print("add 이름 나이 점수 : 입력한 이름 나이 정수를 레코드에 추가합니다.")
            print("del 이름 : 해당 이름과 같은 모든 사람들의 레코드들을 삭제합니다.")
            print("show 키(Name/Score/Age) : 레코드의 모든 내용을 키값 기준으로 정렬하여 나타냅니다. (키값 미입력시 기본값 Name)")
            print("inc 이름 추가할점수 : 이름을 가진 모든 사람의 점수를 추가할점수만큼 추가합니다.")
            print("find 이름 : 해당 이름을 가진 모든 사람들의 레코드들을 찾습니다.")
            print("quit : 변경사항을 저장하고 프로그램을 종료합니다.")
            print("!    모든 명령어에 필요한 정보보다 많은 것들을 입력할 경우 해당 정보들은 무시됩니다    !")
        else:
            print("Invalid command: " + parse[0])
            print("명령어에 도움이 필요할 경우 help를 입력하시오.")


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
