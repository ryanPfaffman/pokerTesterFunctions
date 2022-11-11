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

def isTripsOrBoat(lst):
    str = ''

    for x in lst:
        str += deckHash[int(x)][0]

    def isBoat(str, c):
        for x in str:
            if x != c:
                if str.count(x) > 2:
                    return True

        return False

    for x in str:
        if str.count(x) == 3:
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

def evaluateHand(lst):
    isTripsOrBoat1 = isTripsOrBoat(lst)
    isTwoPairOrPair1 = isTwoPairOrPair(lst)

    if isQuads(lst):
        return [lst,'four of a kind']
    elif isFlush(lst):
        if isStraightFlush(lst):
            return [lst,'straight flush']
        else:
            return [lst,'flush']
    elif isTripsOrBoat1 != 'false':
        if isTripsOrBoat1 == '3ok':
            return [lst,'three of a kind']
        else:
            return [lst,'full house']
    elif isTwoPairOrPair1 != 'false':
        if isTwoPairOrPair1 == 'two pair':
            return [lst,'two pair']
        else:
            return [lst,'one pair']
    else:
        return [lst,'high card']

def whoWon(lst):
    rtnHash = {}
    i = 0
    for x in lst:
        for card in x:
            print(deckHash[card][1])

    return rtnHash

def createRandomHands():
    lst = []
    tempL = []

    for x in range(0,1000000):
        for x in range(0,7):
            tempVal = r.randrange(1,53)
            while tempVal in tempL:
                tempVal = r.randrange(1,53)
            tempL.append(tempVal)
        lst.append(sorted(tempL,reverse=True))
        tempL = []

    return lst

def get_key(val):
    for key, value in handHash.items():
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
    return get_key(deckHash[x][0])
sum = 0

for x in handLst:

    test = f'{readHand(sorted(x,key=getRanking,reverse=True))}: {evaluateHand(x)}'
    hand = evaluateHand(x)
    sum += getAvg(x)
