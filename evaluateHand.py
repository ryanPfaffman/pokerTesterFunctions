import random as r

handHash = {13:"A",12:"K",11:"Q",10:"J",9:"T",8:"9",7:"8",6:"7",5:"6",4:"5",3:"4",2:"3",1:"2"}
handRankingHash = {8:"straight flush",7:"four of a kind",6:'full house',5:'flush',4:'straight',3:'three of a kind',2:'two pair',1:'one pair', 0:'high card'}
deckHash = {52:['A','h'],51:['K','h'],50:['Q','h'],49:['J','h'],48:['T','h'],47:['9','h'],46:['8','h'],45:['7','h'],44:['6','h'],43:['5','h'],42:['4','h'],41:['3','h'],40:['2','h'],39:['A','d'],38:['K','d'],37:['Q','d'],36:['J','d'],35:['T','d'],34:['9','d'],33:['8','d'],32:['7','d'],31:['6','d'],30:['5','d'],29:['4','d'],28:['3','d'],27:['2','d'],26:['A','c'],25:['K','c'],24:['Q','c'],23:['J','c'],22:['T','c'],21:['9','c'],20:['8','c'],19:['7','c'],18:['6','c'],17:['5','c'],16:['4','c'],15:['3','c'],14:['2','c'],13:['A','s'],12:['K','s'],11:['Q','s'],10:['J','s'],9:['T','s'],8:['9','s'],7:['8','s'],6:['7','s'],5:['6','s'],4:['5','s'],3:['4','s'],2:['3','s'],1:['2','s']}
shuffleDeckHash = {52:['A','h'],51:['K','h'],50:['Q','h'],49:['J','h'],48:['T','h'],47:['9','h'],46:['8','h'],45:['7','h'],44:['6','h'],43:['5','h'],42:['4','h'],41:['3','h'],40:['2','h'],39:['A','d'],38:['K','d'],37:['Q','d'],36:['J','d'],35:['T','d'],34:['9','d'],33:['8','d'],32:['7','d'],31:['6','d'],30:['5','d'],29:['4','d'],28:['3','d'],27:['2','d'],26:['A','c'],25:['K','c'],24:['Q','c'],23:['J','c'],22:['T','c'],21:['9','c'],20:['8','c'],19:['7','c'],18:['6','c'],17:['5','c'],16:['4','c'],15:['3','c'],14:['2','c'],13:['A','s'],12:['K','s'],11:['Q','s'],10:['J','s'],9:['T','s'],8:['9','s'],7:['8','s'],6:['7','s'],5:['6','s'],4:['5','s'],3:['4','s'],2:['3','s'],1:['2','s']}

def isQuads(lst):
    str = ''

    for x in lst:
        str += deckHash[int(x)][0]

    for x in str:
        if str.count(x) == 4:
            return True

    return False

def isFlush(lst):
    str = ''

    for x in lst:
        str += deckHash[int(x)][1]

    for x in str:
        if str.count(x) > 4:
            return True

    return False

def isStraightFlush(lst):
    lst = sorted(lst,reverse=True)
    ##print(lst)
    c = 1
    i = 0
    check = int(lst[i])
    if len(lst) > 5:
        for x in lst:
            if i < 6:
                if check - int(lst[i+1]) == 1:
                    c += 1
                else:
                    c = 1

                if c == 5:
                    return True

                check = int(lst[i+1])
            i += 1
    else:
        for x in lst:
            if i < 4:
                if check - int(lst[i+1]) == 1:
                    c += 1
                else:
                    c = 1

                if c == 5:
                    return True

                check = int(lst[i+1])
            i += 1

    return False

def isStraight(lst):
    lst = sorted(lst,key=getRanking,reverse=True)
    c = 1
    leng = len(lst)
    ###print(readHand(lst))

    for x in range(0,leng):
        if x < leng - 1:
            ch1Crd = deckHash[lst[x]][0]
            ch2Crd = deckHash[lst[x+1]][0]
            ch1 = get_key(ch1Crd,handHash)
            ch2 = get_key(ch2Crd,handHash)
            ###print(ch1 - ch2)

            if ch1-ch2 == 1:
                c += 1
            elif ch1-ch2 == 0:
                continue
            else:
                c = 1
            if c == 5:
                return True
        ###print(f'c: {c}')
        if c == 4:
            if ch2Crd == '2':
                if 'A' in readHand(lst):
                    return True
    return False

def isTripsOrBoat(lst):
    str = ''

    for x in lst:
        str += deckHash[int(x)][0]

    def isBoat(str, c):
        for x in str:
            if x != c:
                if str.count(x) > 1:
                    return True

        return False

    for x in str:
        if str.count(x) == 3:
            ###print(x)
            if isBoat(str, x):
                return 'fh'
            else:
                return '3ok'

    return 'false'

def isTwoPairOrPair(lst):
    str = ''

    for x in lst:
        str += deckHash[int(x)][0]

    def isTwoPair(str, c):
        for x in str:
            if x != c:
                if str.count(x) == 2:
                    return True

        return False

    for x in str:
        if str.count(x) == 2:
            if isTwoPair(str, x):
                return 'two pair'
            else:
                return 'one pair'

    return 'false'
def bestFive(lst, rank):
    sortedLst = sorted(lst,key=getRanking,reverse=True)
    handStr = readHand(sortedLst)
    ###print(handStr)
    if rank == 'four of a kind':
        leng = len(lst)
        rtnLst = []
        for x in range(0,leng):
            if x < leng-3:
                if deckHash[sortedLst[x]][0] == deckHash[sortedLst[x+1]][0] == deckHash[sortedLst[x+2]][0] == deckHash[sortedLst[x+3]][0]:
                    rtnLst.append(sortedLst[x])
                    rtnLst.append(sortedLst[x+1])
                    rtnLst.append(sortedLst[x+2])
                    rtnLst.append(sortedLst[x+3])
        for x in sortedLst:
            if len(rtnLst) < 5:
                if x not in rtnLst:
                    rtnLst.append(x)
            else:
                break
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'straight flush':
        leng = len(lst)
        lst = sorted(lst,reverse=True)
        ###print('triggered')
        ###print(lst)
        ###print(readHand(sortedLst))
        for x in range(0,leng):
            if x < leng:
                ###print(x)
                if lst[x] - lst[x+1] == 1 and lst[x+1] - lst[x+2] == 1 and lst[x+2] - lst[x+3] == 1:
                    rtnLst = lst[x:x+5]
                    ###print(lst[x:x+5])
                    ###print(sortedLst)
                    ###print(readHand(rtnLst))
                    return [rtnLst,rank]
    elif rank == 'full house':
        ###print('here')
        leng = len(lst)
        rtnLst = []
        n = ''
        for x in range(0,leng):
            if x < leng-2:
                c = deckHash[sortedLst[x]][0]
                if c == deckHash[sortedLst[x+1]][0] == deckHash[sortedLst[x+2]][0]:
                    n = c
                    rtnLst.append(sortedLst[x])
                    rtnLst.append(sortedLst[x+1])
                    rtnLst.append(sortedLst[x+2])
        for x in range(0,leng):
            if x < leng-1:
                y = deckHash[sortedLst[x]][0]
                if y != n:
                    if y == deckHash[sortedLst[x+1]][0]:
                        rtnLst.append(sortedLst[x])
                        rtnLst.append(sortedLst[x+1])
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'flush':
        leng = len(lst)
        rtnLst = []
        suit = ''
        for x in sortedLst:
            c = deckHash[x][1]
            if handStr.count(c) >= 5:
                suit = c
                break

        for x in sortedLst:
            d = deckHash[x][1]
            if d == suit:
                if len(rtnLst) < 5:
                    rtnLst.append(x)
                else:
                    break
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'straight':
        leng = len(lst)
        rtnLst = []
        c = 1
        ##print(f'sortedLst: {readHand(sortedLst)}')
        for x in range(0,leng):
            if x < leng-1:
                if deckHash[sortedLst[x]][0] == deckHash[sortedLst[x+1]][0]:
                    continue
                else:
                    rtnLst.append(sortedLst[x])
            else:
                if deckHash[sortedLst[x]][0] != deckHash[rtnLst[len(rtnLst)-1]][0]:
                    rtnLst.append(sortedLst[x])
        ###print(rtnLst)
        sortedLst = rtnLst
        leng2 = len(sortedLst)
        ##print(f'sortedLst now: {readHand(sortedLst)}')
        for x in range(0,leng2-4):
            ##print(x)
            for y in range(x+4,leng2):
                yCrd = deckHash[sortedLst[y]][0]
                xCrd = deckHash[sortedLst[x]][0]
                valY = get_key(yCrd,handHash)
                valX = get_key(xCrd,handHash)
                if c+(valX-valY) == 5:
                    return [sortedLst[x:y+1],'straight']
        tempLst = sortedLst[leng2-4:leng2]
        for x in sortedLst:
            if deckHash[x][0] == 'A':
                tempLst.append(x)
                return [tempLst,'straight']

    elif rank == 'three of a kind':
        leng = len(lst)
        rtnLst = []
        for x in range(0,leng):
            if x < leng-2:
                if deckHash[sortedLst[x]][0] == deckHash[sortedLst[x+1]][0] == deckHash[sortedLst[x+2]][0]:
                    rtnLst.append(sortedLst[x])
                    rtnLst.append(sortedLst[x+1])
                    rtnLst.append(sortedLst[x+2])
        for x in sortedLst:
            if len(rtnLst) < 5:
                if x not in rtnLst:
                    rtnLst.append(x)
            else:
                break
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'two pair':
        leng = len(lst)
        rtnLst = []
        for x in range(0,leng):
            if x < leng-1:
                if deckHash[sortedLst[x]][0] == deckHash[sortedLst[x+1]][0]:
                    if len(rtnLst) != 4:
                        rtnLst.append(sortedLst[x])
                        rtnLst.append(sortedLst[x+1])
        for x in sortedLst:
            if len(rtnLst) < 5:
                if x not in rtnLst:
                    rtnLst.append(x)
            else:
                break
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'one pair':
        leng = len(lst)
        rtnLst = []
        for x in range(0,leng):
            if x < leng-1:
                if deckHash[sortedLst[x]][0] == deckHash[sortedLst[x+1]][0]:
                    rtnLst.append(sortedLst[x])
                    rtnLst.append(sortedLst[x+1])
        for x in sortedLst:
            if len(rtnLst) < 5:
                if x not in rtnLst:
                    rtnLst.append(x)
            else:
                break
        ###print(readHand(rtnLst))
        return [rtnLst,rank]
    else:
        if len(sortedLst) == 5:
            return [sortedLst, rank]
        else:
            return [sortedLst[:-2],rank]

def evaluateHand(lst):
    isTripsOrBoat1 = isTripsOrBoat(lst)
    isTwoPairOrPair1 = isTwoPairOrPair(lst)
    ##print(f'\nfirst:{lst}')
    ##print(f'\nfirst read:{readHand(lst)}')
    if isQuads(lst):
        return bestFive(lst,'four of a kind')
    elif isFlush(lst):
        ##print(f'isSF:{isStraightFlush(lst)}')
        if isStraightFlush(lst):
            ##print('42342')
            return bestFive(lst,'straight flush')
        else:
            return bestFive(lst,'flush')
    elif isStraight(lst):
        return bestFive(lst,'straight')
    elif isTripsOrBoat1 != 'false':
        ###print(isTripsOrBoat1)
        if isTripsOrBoat1 == '3ok':
            return bestFive(lst,'three of a kind')
        else:
            return bestFive(lst,'full house')
    elif isTwoPairOrPair1 != 'false':
        if isTwoPairOrPair1 == 'two pair':
            return bestFive(lst,'two pair')
        else:
            return bestFive(lst,'one pair')
    else:
        return bestFive(lst,'high card')

def sortByStrength(hash):
    hash = dict(sorted(hash.items(),key=lambda y: (y[1][2][0],y[1][2][1]),reverse=True))
    return hash

def whoWon(hash):
    firstKey = list(hash.keys())[0]
    ##print(f'\nhashh:{hash}\n')
    chx = hash[firstKey][2]
    for x,y in hash.items():
        lst = hash[x]
        handNums = lst[0]
        handRank = lst[2][0]

        if handRank == 8:
            ##print('strflush2')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3],y[1][2][4],y[1][2][5]),reverse=True))
                ##print(f'tieK2Pard: {tempNary}')
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                chx3 = tempNary[firstKey][2][3]
                chx4 = tempNary[firstKey][2][4]
                chx5 = tempNary[firstKey][2][5]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2 and tempNary[x][2][3] == chx3 and tempNary[x][2][4] == chx4 and tempNary[x][2][5] == chx5:
                        tempLst.append(x)
                return tempLst
        elif handRank == 7:
            ##print('quads2')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2]),reverse=True))
                ##print(f'tieK2Quads: {tempNary}')
                firstKey = list(tempNary.keys())[0]
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2:
                        tempLst.append(x)
                return tempLst
        elif handRank == 6:
            ##print('boats2')
            ##print(f'top: {handRank}')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
                ##print(f'tempNary: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2]),reverse=True))
                firstKey = list(tempNary.keys())[0]
                ###print(f'\nhashh:{hash}\n')
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2:
                        tempLst.append(x)
                return tempLst
        elif handRank == 5:
            ##print('flush2')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3],y[1][2][4],y[1][2][5]),reverse=True))
                ##print(f'tieK2Pard: {tempNary}')
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                chx3 = tempNary[firstKey][2][3]
                chx4 = tempNary[firstKey][2][4]
                chx5 = tempNary[firstKey][2][5]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2 and tempNary[x][2][3] == chx3 and tempNary[x][2][4] == chx4 and tempNary[x][2][5] == chx5:
                        tempLst.append(x)
                return tempLst
        elif handRank == 4:
            ##print('str2')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1]),reverse=True))
                ##print(f'tieK2Pard: {tempNary}')
                chx1 = tempNary[firstKey][2][1]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1:
                        tempLst.append(x)
                return tempLst
        elif handRank == 3:
            ##print('this time3')
            ##print(f'top: {handRank}')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
                ##print(f'tempNary: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst36 = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3]),reverse=True))

                firstKey = list(tempNary.keys())[0]
                ###print(f'\nhashh:{hash}\n')
                chx1 = tempNary[firstKey][2][2]
                chx2 = tempNary[firstKey][2][3]
                lst32 = []
                for x, y in tempNary.items():
                    if tempNary[x][2][2] == chx1 and tempNary[x][2][3] == chx2:
                        lst32.append(x)
                    ##print('\n')
                    ###print(tempNary[x][2][2][0])
                ##print(f'tieK: {tempNary}')
                return lst32
                ##print('\n\n')
            ##print(f'hashtime: {hash}')
            ##print(hash[x])
            ##print(lst[2])
        elif handRank == 2:
            ##print('2nd2pair')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3]),reverse=True))
                ##print(f'tieK2Pard: {tempNary}')
                firstKey = list(tempNary.keys())[0]
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                chx3 = tempNary[firstKey][2][3]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2 and tempNary[x][2][3] == chx3:
                        tempLst.append(x)
                return tempLst
        elif handRank == 1:
            ##print('paird')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            if len(tempNary) == 1:
                ##print(list(tempNary.keys()))
                return list(tempNary.keys())
            else:
                tempLst = []
                tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3],y[1][2][4]),reverse=True))
                ##print(f'tieKPard: {tempNary}')
                firstKey = list(tempNary.keys())[0]
                chx1 = tempNary[firstKey][2][1]
                chx2 = tempNary[firstKey][2][2]
                chx3 = tempNary[firstKey][2][3]
                chx4 = tempNary[firstKey][2][4]
                for x, y in tempNary.items():
                    if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2 and tempNary[x][2][3] == chx3 and tempNary[x][2][4] == chx4:
                        tempLst.append(x)
                return tempLst
        else:
            ##print('hgh2')
            tempNary = {}
            for x,y in hash.items():
                if hash[x][2][0] == handRank:
                    tempNary.update({x:hash[x]})
            ##print(f'tempNaryPaird: {tempNary}')
            tempLst = []
            tempNary = dict(sorted(tempNary.items(),key=lambda y: (y[1][2][0],y[1][2][1],y[1][2][2],y[1][2][3],y[1][2][4],y[1][2][5]),reverse=True))
            ##print(f'tieKPard: {tempNary}')
            firstKey = list(tempNary.keys())[0]
            chx1 = tempNary[firstKey][2][1]
            chx2 = tempNary[firstKey][2][2]
            chx3 = tempNary[firstKey][2][3]
            chx4 = tempNary[firstKey][2][4]
            chx5 = tempNary[firstKey][2][5]
            for x, y in tempNary.items():
                if tempNary[x][2][1] == chx1 and tempNary[x][2][2] == chx2 and tempNary[x][2][3] == chx3 and tempNary[x][2][4] == chx4 and tempNary[x][2][5] == chx5:
                    tempLst.append(x)
            return tempLst

def getHandPoints(lst):
    s = 0
    ##print('readHandTimes')
    ##print(lst)
    handNums = lst[0]
    handRank = lst[1]
    ##print('readHandTimes ' + handRank)

    if handRank == 'straight flush':
        ##print('strflush1')
        crd1 = deckHash[handNums[0]][0]
        crd2 = deckHash[handNums[1]][0]
        crd3 = deckHash[handNums[2]][0]
        crd4 = deckHash[handNums[3]][0]
        crd5 = deckHash[handNums[4]][0]
        keycrd1 = get_key(crd1,handHash)
        keycrd2 = get_key(crd2,handHash)
        keycrd3 = get_key(crd3,handHash)
        keycrd4 = get_key(crd4,handHash)
        keycrd5 = get_key(crd5,handHash)
        ##print(readHand(handNums))
        ##print([8,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5])
        return [8,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5]
    elif handRank == 'four of a kind':
        ##print('quads1')
        quadsCrd = deckHash[handNums[0]][0]
        kckr = deckHash[handNums[4]][0]
        keycrd1 = get_key(quadsCrd,handHash)
        keycrd2 = get_key(kckr,handHash)
        ##print(readHand(handNums))
        ##print([7,keycrd1,keycrd2])
        return [7,keycrd1,keycrd2]
    elif handRank == 'full house':
        ##print(readHand(handNums))
        ##print('boats1')
        ##print(readHand(handNums))
        topboat = deckHash[handNums[0]][0]
        bottomboat = deckHash[handNums[3]][0]
        keytopboat = get_key(topboat,handHash)
        keybottomboat = get_key(bottomboat,handHash)
        ##print([6,keytopboat,keybottomboat])
        return [6,keytopboat,keybottomboat]
    elif handRank == 'flush':
        ##print('flush1')
        crd1 = deckHash[handNums[0]][0]
        crd2 = deckHash[handNums[1]][0]
        crd3 = deckHash[handNums[2]][0]
        crd4 = deckHash[handNums[3]][0]
        crd5 = deckHash[handNums[4]][0]
        keycrd1 = get_key(crd1,handHash)
        keycrd2 = get_key(crd2,handHash)
        keycrd3 = get_key(crd3,handHash)
        keycrd4 = get_key(crd4,handHash)
        keycrd5 = get_key(crd5,handHash)
        ##print(readHand(handNums))
        ##print([5,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5])
        return [5,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5]
    elif handRank == 'straight':
        fst = deckHash[handNums[0]][0]
        snd = deckHash[handNums[4]][0]
        str = f'straight {snd} to {fst}'
        ###print(str)
        if snd == 'A':
            return [4,0]
        else:
            ###print(get_key(snd,handHash))
            return [4,get_key(snd,handHash)]

        ###print(readHand(handNums))
    elif handRank == 'three of a kind':
        fst = deckHash[handNums[0]][0]
        snd = deckHash[handNums[3]][0]
        trd = deckHash[handNums[4]][0]
        str = f'3oak, {fst},{snd},{trd}'
        ##print(str)
        ##print(readHand(handNums))
        keyfst = get_key(fst,handHash)
        return [3,keyfst,get_key(snd,handHash),get_key(trd,handHash)]

    elif handRank == 'two pair':
        ##print('1st2pair')
        ##print(readHand(handNums))
        pair1 = deckHash[handNums[0]][0]
        pair2 = deckHash[handNums[2]][0]
        kickr = deckHash[handNums[4]][0]
        keypair1 = get_key(pair1,handHash)
        keypair2 = get_key(pair2,handHash)
        keykickr = get_key(kickr,handHash)
        ##print([2,keypair1,keypair2,keykickr])
        return[2,keypair1,keypair2,keykickr]

    elif handRank == 'one pair':
        ##print('paird1st')
        pair = deckHash[handNums[0]][0]
        kickr1 = deckHash[handNums[2]][0]
        kickr2 = deckHash[handNums[3]][0]
        kickr3 = deckHash[handNums[4]][0]
        keypair = get_key(pair,handHash)
        keykickr1 = get_key(kickr1,handHash)
        keykickr2 = get_key(kickr2,handHash)
        keykickr3 = get_key(kickr3,handHash)
        ##print(readHand(handNums))
        ##print([1,keypair,keykickr1,keykickr2,keykickr3])
        return [1,keypair,keykickr1,keykickr2,keykickr3]

    else:
        ##print('hgh1')
        crd1 = deckHash[handNums[0]][0]
        crd2 = deckHash[handNums[1]][0]
        crd3 = deckHash[handNums[2]][0]
        crd4 = deckHash[handNums[3]][0]
        crd5 = deckHash[handNums[4]][0]
        keycrd1 = get_key(crd1,handHash)
        keycrd2 = get_key(crd2,handHash)
        keycrd3 = get_key(crd3,handHash)
        keycrd4 = get_key(crd4,handHash)
        keycrd5 = get_key(crd5,handHash)
        ##print(readHand(handNums))
        ##print([0,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5])
        return [0,keycrd1,keycrd2,keycrd3,keycrd4,keycrd5]
    ##print(readHand(lst[0]))
    ##print(lst[1])
    for x in lst[0]:
        s += get_key(deckHash[x][0],handHash)
    y = get_key(lst[1],handRankingHash)
    ##print(y)
    return [y,s]

def createRandomHands():
    lst = []
    tempL = []

    for x in range(0,10):
        for x in range(0,7):
            tempVal = r.randrange(1,53)
            while tempVal in tempL:
                tempVal = r.randrange(1,53)
            tempL.append(tempVal)
        lst.append(sorted(tempL,reverse=True))
        tempL = []

    return lst

def get_key(val, hash):
    for key, value in hash.items():
        if val == value:
            return key

def readHand(lst):
    str = ''

    for x in lst:
        i = deckHash[x]
        str += f'{i[0]}{i[1]} '

    return str.strip()

###print(evaluateHand(['12','11','37','3','28','45','41']))
handLst = createRandomHands()

def getAvg(lst):
    s = 0
    i = 1
    for x in lst:
        s += x
        i += 1

    return s/i

def getRanking(x):
    return get_key(deckHash[x][0], handHash)
def sortLstByDeckHash(x):
    return get_key(deckHash[x][0], deckHash)
def getRankToCheckStraight(x):
    return get_key(deckHash[x][0], handHash)
sum = 0

for x in handLst:
    #test = f'{readHand(sorted(x,key=getRanking,reverse=True))}: {evaluateHand(x)}'
    ###print(readHand(sorted(x,key=getRanking,reverse=True)))
    #hand = evaluateHand(x)
    ###print(hand)
    ###print(f'{readHand(hand[0]),hand[1]}')
    ###print(getHandPoints(hand))
    #sum += getAvg(x)
    continue

#steps to evaluate hand
#sort hand list by deckHash
'''
strFlsLst = [13, 42, 46, 45, 44, 43, 6]
strFlsLst = sorted(strFlsLst,key=getRanking,reverse=True)
strFlsLst2 = [50, 47, 46, 45, 44, 43, 6]
strFlsLst2 = sorted(strFlsLst2,key=getRanking,reverse=True)
handEval = evaluateHand(strFlsLst)
handEval2 = evaluateHand(strFlsLst2)
##print(f'handEval: {handEval}')
##print(f'handEvalRead: {readHand(handEval[0])}')
##print(f'handEval: {handEval2}')
##print(f'handEvalRead: {readHand(handEval2[0])}')
#testLst = sorted([37,10,34,35,52,26,51],key=getRanking,reverse=True)
#testHand = evaluateHand([52,43,42,2,28,1,13])
###print(testHand[0])
###print(f'{readHand(testHand[0])},{testHand[1]}')
###print(readHand(evaluateHand(testLst)[0]))
###print(readHand(evaluateHand([45, 41, 40, 39, 16, 15, 4])[0]))
'''
'''
for x in range(0,10):
    ##print(f'\t\t\tNEW HAND\n\n\n\n\n')
    shuffleDeckHash = {52:['A','h'],51:['K','h'],50:['Q','h'],49:['J','h'],48:['T','h'],47:['9','h'],46:['8','h'],45:['7','h'],44:['6','h'],43:['5','h'],42:['4','h'],41:['3','h'],40:['2','h'],39:['A','d'],38:['K','d'],37:['Q','d'],36:['J','d'],35:['T','d'],34:['9','d'],33:['8','d'],32:['7','d'],31:['6','d'],30:['5','d'],29:['4','d'],28:['3','d'],27:['2','d'],26:['A','c'],25:['K','c'],24:['Q','c'],23:['J','c'],22:['T','c'],21:['9','c'],20:['8','c'],19:['7','c'],18:['6','c'],17:['5','c'],16:['4','c'],15:['3','c'],14:['2','c'],13:['A','s'],12:['K','s'],11:['Q','s'],10:['J','s'],9:['T','s'],8:['9','s'],7:['8','s'],6:['7','s'],5:['6','s'],4:['5','s'],3:['4','s'],2:['3','s'],1:['2','s']}
    shuffledKeys =  list(shuffleDeckHash.keys())
    r.shuffle(shuffledKeys)
    ##print(f'shuffledDeckKeys: {shuffledKeys}')
    ind = 0
    ind2 = 0
    cardsNeededPre = 12
    handMapTest = {'Big Blind':[],'UTG':[],'UTG+1':[],'UTG+2':[],'Dealer':[],'Small Blind':[]}
    ###print(list(handMapTest.keys())[0])
    handMapTestLst = list(handMapTest.keys())
    handMapTestLstLen = len(handMapTestLst)
    communityCardsTest = []
    ##print(f'handMapTestLstLen: {handMapTestLstLen}')
    sec = False
    tempLst7 = []

    for x in shuffledKeys:
        if ind < cardsNeededPre:
            ##print(x)
            ##print(f'ind2: {ind2}')
            ###print(handMapTest[handMapTestLst[ind2]])
            ##print(deckHash[x])
            curSeat = handMapTestLst[ind2]
            curCard = deckHash[x]
            ##print(f'cur: {curSeat}')
            ##print(f'curCard: {curCard}')
            if sec:
                tempLst7 = handMapTest[curSeat]
                ###print(f'te: {tempLst10}')
                tempLst7.append(x)
                handMapTest[curSeat] = tempLst7
                tempLst7 = []
                ###print(f'curCard: {tempLst10+curCard}')
                #tempLst10.append(curCard[1])
                ###print(f'te: {tempLst10}')
                #handMapTest[curSeat] = tempLst10

            else:
                tempLst7.append(x)
                handMapTest[curSeat] = tempLst7
                tempLst7 = []
            ###print(handMapTest)
            if ind2 == handMapTestLstLen-1:
                sec = True
                ind2 = 0
            else:
                ind2 += 1
            ###print(f'{shuffleDeckHash[x]}')
            del shuffleDeckHash[x]
        else:
            break

        ind += 1

    ##print(f'shuffledDeckKeys: {len(shuffledKeys)}')
    lstAfterPreDeal = shuffledKeys[ind:]
    ##print(f'len lstAfterPreDeal: {len(lstAfterPreDeal)}')
    ##print(f'ind: {shuffledKeys[ind:]}')
    ##print(f'handMapTest after: {handMapTest}')
    ##print(f'shuffleDeckHash after: {shuffleDeckHash}')
    communityCardsTest.extend(lstAfterPreDeal[1:4])
    communityCardsTest.append(lstAfterPreDeal[4])
    communityCardsTest.append(lstAfterPreDeal[6])
    ##print(f'flop: {communityCardsTest[:3]}')
    ##print(f'turn: {communityCardsTest[3]}')
    ##print(f'river: {communityCardsTest[4]}')
    ##print(f'board: {readHand(communityCardsTest)}')
    for x,y in handMapTest.items():
        handMapTest[x].extend(communityCardsTest)
        ##print(readHand(handMapTest[x]))
    for x,y in handMapTest.items():
        handEval = evaluateHand(handMapTest[x])
        ##print(f'{x}:{readHand(handMapTest[x])}')
        handMapTest[x] = handEval
        handPoints = getHandPoints(handMapTest[x])
        handMapTest[x].append(handPoints)
        ##print(handMapTest[x])
        ##print(readHand(handMapTest[x][0]))

    ##print(f'new handMapTest: {handMapTest}')
    handMapStr = sortByStrength(handMapTest)
    ##print()
    ##print(f'handMapStr: {handMapStr}')
    winnersLst = whoWon(handMapStr)
    if len(winnersLst) > 1:
        for x in winnersLst:
            ##print(f'\t\t\tNEW TIE HAND\n\n\n\n\n')
            ##print(x)
            ##print(handMapTest[x])
            ##print(f'board: {readHand(communityCardsTest)}')
            ##print(readHand(handMapTest[x][0]))
            ##print()

    else:
        for x in winnersLst:
            ##print(f'\t\t\tNEW WINNER3s\n\n\n\n\n')
            ##print(x)
            ##print(handMapTest[x])
            ##print(f'board: {readHand(communityCardsTest)}')
            ##print(readHand(handMapTest[x][0]))
            ##print()
'''
playerMap = {'Big Blind':[],'Dealer':[]}
shuffledKeys = [52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def getProb(map):
    r.shuffle(shuffledKeys)
    ###print(f'shuffledDeckKeys: {shuffledKeys}')
    ind = 0
    ind2 = 0
    mapLst = list(map.keys())
    mapLstLen = len(mapLst)
    cardsNeededPre = mapLstLen*2
    communityCards = []
    ###print(cardsNeededPre)
    ###print(list(handMapTest.keys())[0])
    sec = False
    tempLst7 = []

    for x in shuffledKeys:
        if ind < cardsNeededPre:
            ###print(x)
            ###print(f'ind2: {ind2}')
            ###print(handMapTest[handMapTestLst[ind2]])
            ###print(deckHash[x])
            curSeat = mapLst[ind2]
            curCard = deckHash[x]
            ###print(f'cur: {curSeat}')
            ###print(f'curCard: {curCard}')
            if sec:
                tempLst7 = map[curSeat]
                ###print(f'te: {tempLst10}')
                tempLst7.append(x)
                map[curSeat] = tempLst7
                tempLst7 = []
                ###print(f'curCard: {tempLst10+curCard}')
                #tempLst10.append(curCard[1])
                ###print(f'te: {tempLst10}')
                #handMapTest[curSeat] = tempLst10

            else:
                tempLst7.append(x)
                map[curSeat] = tempLst7
                tempLst7 = []
            ###print(handMapTest)
            if ind2 == mapLstLen-1:
                sec = True
                ind2 = 0
            else:
                ind2 += 1
            ###print(f'{shuffleDeckHash[x]}')
            del shuffleDeckHash[x]
        else:
            break

        ind += 1
    ###print(f'\nmap after deal: {map}\n')
    startHash = {}
    for x,y in map.items():
        tempLst = []
        for z in map[x]:
            tempLst.append(z)
        startHash[x] = tempLst
        ###print(f'mapher: {map[x]}')
    ###print(map)
    lstAfterPreDeal = shuffledKeys[ind:]
    communityCards.extend(lstAfterPreDeal[1:4])
    communityCards.append(lstAfterPreDeal[4])
    communityCards.append(lstAfterPreDeal[6])


    fstBoard = True

    probmap = {}
    checkstr = ''
    holeCardsMap = {}
    iters = 100000
    for x in range(0,iters):
        ###print(f'\n\nmap::: {map}\n\n')
        if fstBoard:
            for x,y in map.items():
                ###print('11')
                map[x].extend(communityCards)
                handEval = evaluateHand(map[x])
                map[x] = handEval
                handPoints = getHandPoints(map[x])
                map[x].append(handPoints)
            map = sortByStrength(map)
            ###print(map)
            winnersLst = whoWon(map)
            if len(winnersLst) > 1:
                #print('here')
                #print(f'probmap: {probmap}')
                for x in winnersLst:
                    if x in checkstr:
                        probmap[x][1] += 1
                    else:
                        probmap[x] = [0,1]
                        checkstr += x
                #print(f'probmap: {probmap}')
            else:
                for x in winnersLst:
                    if x in checkstr:
                        probmap[x][0] += 1
                    else:
                        probmap[x] = [1,0]
                        checkstr += x
            ###print(f'\n\n{map}')
            ###print(f'checkstr: {checkstr}')
            fstBoard = False
            communityCards = []
        else:
            r.shuffle(lstAfterPreDeal)
            communityCards.extend(lstAfterPreDeal[1:4])
            communityCards.append(lstAfterPreDeal[4])
            communityCards.append(lstAfterPreDeal[6])
            ###print(f'wer: {map}')
            for x,y in map.items():
                tempLst = []
                for z in startHash[x]:
                    tempLst.append(z)
                map[x] = tempLst
                map[x].extend(communityCards)
                handEval = evaluateHand(map[x])
                map[x] = handEval
                handPoints = getHandPoints(map[x])
                map[x].append(handPoints)
            map = sortByStrength(map)
            ###print(f'mapafterevaluation: {map}')

            winnersLst = whoWon(map)
            if len(winnersLst) > 1:
                #print('here')
                #print(f'probmap: {probmap}')
                for x in winnersLst:
                    if x in checkstr:
                        probmap[x][1] += 1
                    else:
                        probmap[x] = [0,1]
                        checkstr += x
                #print(f'probmap: {probmap}')
            else:
                for x in winnersLst:
                    if x in checkstr:
                        probmap[x][0] += 1
                    else:
                        probmap[x] = [1,0]
                        checkstr += x
                ###print(holeCardsMap[x])

                #handEval = evaluateHand(map[x])
                ###print(readHand(map[x]))
                ###print(handEval)
            ###print(readHand(communityCards))
            communityCards = []
        ##print(f'probmap: {probmap}')
    u = 0
    t = 0
    for x,y in probmap.items():
        probmap[x][0] = round((probmap[x][0]/iters)*100,1)
        probmap[x][1] = round((probmap[x][1]/iters)*100,1)

        t += 1
    print(f'u: {u}')
    ze = (1-u)/t
    print(z)

    for x,y in startHash.items():
        print(f"{x}'s Hole Cards:{readHand(startHash[x])}")
    print(probmap)

print(getProb(playerMap))
