directory = '/Users/ryanpfaffman/Ignition Casino Poker/Hand History/580034560407/'
handHistory = open(directory + "HH20221107-212235 - 13322023 - RING - $0.10-$0.25 - HOLDEM - NL - TBL No.28014588.txt", "r")
from evaluateHand import *

def makeHandLst(lst,otherLst):
    rtnLst = otherLst
    hand = lst[0].strip()
    rtnLst.append(hand[:3])
    rtnLst.append(hand[-2:])
    return rtnLst

def getLstItems(lst):
    rtnLst = []
    for x in lst:
        rtnLst.append(x)
    return rtnLst

def changeHand(lst):

    def makeLst(str):
        lst = []
        str = str.strip()
        for x in str:
            lst.append(x)

        return lst

    rtnLst = []
    for x in lst:
        #rtnLst.append(deckHash[get_key(x)])
        rtnLst.append(get_key(makeLst(x), deckHash))

    return rtnLst
def getData(file, dataLst):
    #starting variables
    wonLast = False
    handNumber = ''
    tableNumber = ''

    newHandSetUp = True
    holeCards = False

    knowSeat = False
    knowHand = False
    knowSeatNum = False
    knowAllSeats = False

    mySeat = ''
    mySeatNum = ''
    myHand = ''

    communityCards = []
    myHandEval = []

    handMap = {'Big Blind':[],'UTG':[],'UTG+1':[],'UTG+2':[],'Dealer':[],'Small Blind':[]}

    firstAction = False
    #end starting variables

    #helpers
    def pullMySeat(str):
        rtn = ''
        for x in str:
            if x == '[':
                c = len(str.strip())-1
                return [rtn.strip(), str[c-5:c]]
            rtn += x
    def pullHand(str):
        str = str.strip()
        leng = len(str)
        return str[leng-6:leng-1].strip()

    def pullSeatNum(str):
        rtn = ''
        for x in str:
            if x == ':':
                return rtn[-1]
            rtn += x

    def getHandAndTableNum(str):
        start = False
        knowHandNum = False
        handNum = ''

        knowTableNum = False
        tableNum = ''

        for x in str:
            if x == '#':
                if knowHandNum == False:
                    start = True
                else:
                    start = True

            if start:
                if x == ' ':
                    start = False
                    if knowHandNum == False:
                        knowHandNum = True
                    else:
                        return [handNum, tableNum]
                if start and knowHandNum == False:
                    handNum += x
                if start and knowHandNum:
                    tableNum += x

    print(getHandAndTableNum('Ignition Hand #4370234631 TBL#28014588 HOLDEM No Limit - 2022-11-07 22:39:43'))
    #end helpers

    #start of iterations
    for x in handHistory:

    #seat set ups
        if "Ignition" in x:
            newHandSetUp = True
            lst1 = getHandAndTableNum(x)
            handNumber = lst1[0]
            tableNumber = lst1[1]

        if newHandSetUp:
            if knowSeatNum == False:
                if "[" in x:
                    mySeatNum = pullSeatNum(x)
                    knowSeatNum = True
                    newHandSetUp = False
        if "HOLE" in x:
            holeCards = True

        if holeCards:
            if knowSeat == False and knowHand == False:
                if "ME" in x:
                    lst2 = pullMySeat(x)
                    mySeat = lst2[0]
                    myHand = lst2[1]

                    print('hand#: ' + handNumber)
                    print('table#: ' + tableNumber)
                    print('my seat num: ' + mySeatNum)
                    print('my seat: ' + mySeat)
                    print('my hand: ' + myHand)

                    knowSeat = True
                    knowHand = True
                    mySeatNum = 0
            st = x.strip()
            if 'Card' not in st and 'HOLE' not in st:
                #print(handMap)
                holeCards = False
                knowAllSeats = True
                firstAction = True
                for i in handMap.copy():
                    if handMap[i] == []:
                        del handMap[i]
            if knowAllSeats == False:
                if 'UTG+1' in st:
                    print(st)
                #print(st)
                #print(pullHand(st))
                if 'Big' in st:
                    handMap['Big Blind'] = pullHand(st)
                elif 'Smal' in st:
                    handMap['Small Blind'] = pullHand(st)
                elif 'UTG ' in st:
                    handMap['UTG'] = pullHand(st)
                elif 'UTG+1' in st:
                    handMap['UTG+1'] = pullHand(st)
                elif 'UTG+2' in st:
                    handMap['UTG+2'] = pullHand(st)
                elif 'Dealer' in st:
                    handMap['Dealer'] = pullHand(st)
                #print(handMap)
        if "* F" in x:
            l = len(x)
            floppy = x.strip()
            #print(floppy)
            communityCards.append(floppy[l-10:l-8])
            communityCards.append(floppy[l-7:l-5])
            communityCards.append(floppy[l-4:l-2])
            #print(communityCards)

        if "* T" in x:
            l = len(x)
            turny = x.strip()
            communityCards.append(turny[l-4:l-2])
            #print(communityCards)

        if "* R" in x:
            l = len(x)
            rivery = x.strip()
            #print(rivery)
            print(handNumber)
            communityCards.append(rivery[l-4:l-2])
        if "SUM" in x:
            #print(f'handMap: {handMap}')
            print(f'beginning hands: {handMap}')
            if len(communityCards) > 2:
                tempLst3 = []
                for x,y in handMap.items():
                    tempLst = getLstItems(communityCards)
                    tempLst.append(handMap[x][:3])
                    tempLst.append(handMap[x][-2:])
                    handMap[x] = tempLst
                    tempLst = []

                    tempLst3 = []
                    for z in handMap[x]:
                        tempLst2 = []
                        for each in z:
                            if each != ' ' and each != None:
                                tempLst2.append(each)
                        if tempLst2 != []:
                            tempLst3.append(get_key(tempLst2,deckHash))
                        #print(tempLst3)
                        tempLst2 = []
                    handMap[x] = tempLst3
                    #print(f'{x}:{handMap[x]}')
                    handMap[x] = evaluateHand(handMap[x])
                    handMap[x].append(getHandPoints(handMap[x]))
                    #print(handMap[x])

                print(f'finalHash: {handMap}')

                bestHand = []

                handMap = dict(sorted(handMap.items(),key=lambda y: (y[1][2][0],y[1][2][1]),reverse=True))

                winners = []

                firstKey = list(handMap.keys())[0]
                chx = handMap[firstKey][2]
                for x,y in handMap.items():
                    if handMap[x][2][0] == chx[0] and handMap[x][2][1] == chx[1]:
                        winners.append(x)
                    else:
                        break
                print(winners)
            print(handMap)
            knowSeatNum = False
            holeCards = False
            knowSeat = False
            knowHand = False
            firstAction = False
            knowAllSeats = False
            handNumber = ''
            tableNumber = ''
            communityCards = []
            handMap = {'Big Blind':[],'UTG':[],'UTG+1':[],'UTG+2':[],'Dealer':[],'Small Blind':[]}
    #end seat set ups

print(getData(directory, handHistory))
