def evenFrom200To500():
    #thisList = [i for i in range(200,501,2)]
    thisList = []
    for tmp in range(200,501,2):
        thisList += [tmp]
    return thisList
def manipulateList(theList):
    theList.remove(298)
    theList.remove(412)
    theList.pop()
    thatList = []
    #thatList = [i for i in range(101,196,2)]
    for tmp in range(101,196,2):
        thatList += [tmp]
    theList.extend(thatList)
    return theList
def main():
    theList = evenFrom200To500()
    theList2 = manipulateList(theList)
    #print(theList2)
    print(len(theList2))
    return None
if __name__=='__main__':
    main()
