import random as r

handHash = {13:"A",12:"K",11:"Q",10:"J",9:"T",8:"9",7:"8",6:"7",5:"6",4:"5",3:"4",2:"3",1:"2"}
handRankingHash = {8:"straight flush",7:"four of a kind",6:'full house',5:'flush',4:'straight',3:'three of a kind',2:'two pair',1:'one pair', 0:'high card'}
deckHash = {52:['A','h'],51:['K','h'],50:['Q','h'],49:['J','h'],48:['T','h'],47:['9','h'],46:['8','h'],45:['7','h'],44:['6','h'],43:['5','h'],42:['4','h'],41:['3','h'],40:['2','h'],39:['A','d'],38:['K','d'],37:['Q','d'],36:['J','d'],35:['T','d'],34:['9','d'],33:['8','d'],32:['7','d'],31:['6','d'],30:['5','d'],29:['4','d'],28:['3','d'],27:['2','d'],26:['A','c'],25:['K','c'],24:['Q','c'],23:['J','c'],22:['T','c'],21:['9','c'],20:['8','c'],19:['7','c'],18:['6','c'],17:['5','c'],16:['4','c'],15:['3','c'],14:['2','c'],13:['A','s'],12:['K','s'],11:['Q','s'],10:['J','s'],9:['T','s'],8:['9','s'],7:['8','s'],6:['7','s'],5:['6','s'],4:['5','s'],3:['4','s'],2:['3','s'],1:['2','s']}

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
    c = 1
    i = 0
    check = int(lst[i])

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


    return False

def isStraight(lst):
    lst = sorted(lst,key=getRanking,reverse=True)
    c = 1
    leng = len(lst)
    #print(readHand(lst))

    for x in range(0,leng):
        if x < leng - 1:
            ch1Crd = deckHash[lst[x]][0]
            ch2Crd = deckHash[lst[x+1]][0]
            ch1 = get_key(ch1Crd,handHash)
            ch2 = get_key(ch2Crd,handHash)
            #print(ch1 - ch2)

            if ch1-ch2 == 1:
                c += 1
            elif ch1-ch2 == 0:
                continue
            else:
                c = 1
            if c == 5:
                return True
        #print(f'c: {c}')
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
            #print(x)
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
    #print(handStr)
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
        #print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'straight flush':
        leng = len(lst)
        for x in range(0,leng):
            if x < leng-5:
                if sortedLst[x] - sortedLst[x+1] == 1 and sortedLst[x+1] - sortedLst[x+2] == 1:
                    rtnLst = sortedLst[x:x+5]
                    #print(readHand(rtnLst))
                    return [rtnLst,rank]
    elif rank == 'full house':
        #print('here')
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
        #print(readHand(rtnLst))
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
        #print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'straight':
        leng = len(lst)
        rtnLst = []
        c = 1
        #print(f'sortedLst: {sortedLst}')
        for x in range(0,leng):
            if x < leng - 1:
                ch1Crd = deckHash[sortedLst[x]][0]
                ch2Crd = deckHash[sortedLst[x+1]][0]
                ch1 = get_key(ch1Crd,handHash)
                ch2 = get_key(ch2Crd,handHash)
                '''
                print(deckHash[sortedLst[x]])
                print(deckHash[sortedLst[x+1]])
                print(f'ch1: {ch1}, ch2: {ch2}')
                print(ch1 - ch2)
                '''
                if ch1-ch2 == 1:
                    c += 1
                    if len(rtnLst) == 0:
                        #print(f'1: {sortedLst[x]} 2: {sortedLst[x+1]}')
                        rtnLst.append(sortedLst[x])
                        rtnLst.append(sortedLst[x+1])
                        #print(rtnLst)
                    else:
                        rtnLst.append(sortedLst[x+1])
                    #print(rtnLst)
                elif ch1-ch2 == 0:
                    continue
                else:
                    c = 1
                if c == 5:
                    #print('eh')
                    #print(readHand(rtnLst))
                    return [rtnLst,'straight']
        if c == 4:
            if ch2Crd == '2':
                if 'A' in readHand(sortedLst):
                    for x in sortedLst:
                        if deckHash[x][0] == 'A':
                            if len(rtnLst) < 5:
                                rtnLst.append(x)
        return [rtnLst,'straight']
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
        #print(readHand(rtnLst))
        return [rtnLst,rank]
    elif rank == 'two pair':
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
        #print(readHand(rtnLst))
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
        #print(readHand(rtnLst))
        return [rtnLst,rank]
    else:
        if len(sortedLst) == 5:
            return [sortedLst, rank]
        else:
            return [sortedLst[:-2],rank]

def evaluateHand(lst):
    isTripsOrBoat1 = isTripsOrBoat(lst)
    isTwoPairOrPair1 = isTwoPairOrPair(lst)
    print(f'\nfirst:{readHand(lst)}')
    if isQuads(lst):
        return bestFive(lst,'four of a kind')
    elif isFlush(lst):
        if isStraightFlush(lst):
            return bestFive(lst,'straight flush')
        else:
            return bestFive(lst,'flush')
    elif isStraight(lst):
        return bestFive(lst,'straight')
    elif isTripsOrBoat1 != 'false':
        print(isTripsOrBoat1)
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

def whoWon(lst):
    rtnHash = {}
    i = 0
    for x in lst:
        for card in x:
            print(deckHash[card][1])

    return rtnHash

def getHandPoints(lst):
    s = 0
    print(readHand(lst[0]))
    print(lst[1])
    for x in lst[0]:
        s += get_key(deckHash[x][0],handHash)
    y = get_key(lst[1],handRankingHash)
    print(y)
    return [y,s]

def createRandomHands():
    lst = []
    tempL = []

    for x in range(0,20):
        for x in range(0,5):
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

#print(evaluateHand(['12','11','37','3','28','45','41']))
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
def getRankToCheckStraight(x):
    return get_key(deckHash[x][0], handHash)
sum = 0

for x in handLst:
    #test = f'{readHand(sorted(x,key=getRanking,reverse=True))}: {evaluateHand(x)}'
    #print(readHand(sorted(x,key=getRanking,reverse=True)))
    #hand = evaluateHand(x)
    #print(f'{readHand(hand[0]),hand[1]}')
    #print(getHandPoints(hand))
    #sum += getAvg(x)
    continue

#testLst = sorted([37,10,34,35,52,26,51],key=getRanking,reverse=True)
#testHand = evaluateHand([52,43,42,2,28,1,13])
#print(testHand[0])
#print(f'{readHand(testHand[0])},{testHand[1]}')
#print(readHand(evaluateHand(testLst)[0]))
