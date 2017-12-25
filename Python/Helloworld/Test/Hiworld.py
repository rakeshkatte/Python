'''
Created on Dec 23, 2017

@author: Rakesh
'''
cleanWords = {}
excludedWords = ['i', 'am', 'are', 'is', 'you',
                 'your', 'he', 'she', 'a', 'and', 'of',
                 'or', 'by', 'was', 'has', 'good', 'as',
                 'give', 'him', 'it', 'her', 'will', 'to', 'we']
moduleName = ['claims', 'claim', 'mfm', 'edi',
              'ba', 'billing', 'payment', 'payments']
symbols = '~!@#$%^&*()_+\`-={}|[]\:\";\'<>?,./'


class jiraData:
    def __init__(self, jiraID):
        self.wordRep = 1
        self.jiraID = []
        self.jiraID.append(jiraID)

    def __repr__(self):
        return '%s, %s' % (self.wordRep, self.jiraID)


def parseStr(seedStr):
    primaryList = seedStr.lower().strip('\n').split('\t')
    print primaryList
    if len(primaryList) < 4:
        print('%s - Incorrect format' % (seedStr))
        return
    ticketContent = primaryList[1] + ' ' + primaryList[2]
    seedlist = ticketContent.split()
    uniqueWords = []
    for item in seedlist:
        addUniqueWord(item, uniqueWords, primaryList[0], primaryList[3])


def addUniqueWord(item, uniqueWords, jiraID, component):
    for sym in range(len(symbols)):
        item = item.replace(symbols[sym], '')
    if len(item) > 0:
        if item.startswith(component) or component.startswith(item):
            return
        if item not in excludedWords and item not in uniqueWords:
            uniqueWords.append(item)
            item = component + '_' + item
            if item in cleanWords:
                cleanWords[item].wordRep += 1
                cleanWords[item].jiraID.append(jiraID)
            else:
                cleanWords[item] = jiraData(jiraID)


def parseFile():
    inFile = open('Test.txt', 'r')
    for line in inFile.readlines():
        parseStr(line)
    for key, value in sorted(cleanWords.iteritems(),
                             key=lambda item: item[1].wordRep, reverse=True):
        print "%s, %s" % (key, value)


parseFile()
