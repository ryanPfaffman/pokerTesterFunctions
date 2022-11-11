directory = '/Users/ryanpfaffman/Ignition Casino Poker/Hand History/580034560407/'
handHistory = open(directory + "HH20221107-212235 - 13322023 - RING - $0.10-$0.25 - HOLDEM - NL - TBL No.28014588.txt", "r")
from evaluateHand import *

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

    mySeat = ''
    mySeatNum = ''
    myHand = ''

    communityCards = []
    myHandEval = []
    #end starting variables

    #helpers
    def pullSeat(str):
        rtn = ''
        for x in str:
            if x == '[':
                c = len(str.strip())-1
                return [rtn.strip(), str[c-5:c]]
            rtn += x

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
                    lst2 = pullSeat(x)
                    mySeat = lst2[0]
                    myHand = lst2[1]
                    '''
                    print('hand#: ' + handNumber)
                    print('table#: ' + tableNumber)
                    print('my seat num: ' + mySeatNum)
                    print('my seat: ' + mySeat)
                    print('my hand: ' + myHand)
                    '''
                    knowSeat = True
                    knowHand = True
                    mySeatNum = 0
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
            myHandEval = communityCards
            myHand = myHand.strip()
            myHandEval.append(myHand[:3])
            myHandEval.append(myHand[-2:])


            myHandEval = changeHand(myHandEval)
            print(readHand(sorted(myHandEval,key=getRanking,reverse=True)))

            print(evaluateHand(myHandEval))
        if "SUM" in x:
            knowSeatNum = False
            holeCards = False
            knowSeat = False
            knowHand = False
            handNumber = ''
            tableNumber = ''
            communityCards = []
    #end seat set ups

print(getData(directory, handHistory))
