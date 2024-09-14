datasummary = {}
datakeys = []


def readdata():
    global datakeys, datasummary
    f1 = open('input.txt', 'r')
    line = f1.readline()
    while line:
        data = line.strip().split(",")
        for dataitem in data:
            if dataitem in datasummary:
                datasummary[dataitem] += 1
            else:
                datasummary[dataitem] = 1
                datakeys.append(dataitem)
        line = f1.readline()
    f1.close()


def processdata():
    global datakeys
    for i in range(len(datakeys) - 1):
        for j in range(i+1, len(datakeys)):
            if datakeys[i] > datakeys[j]:
                datakeys[i], datakeys[j] = datakeys[j], datakeys[i]


def printdata():
    global datakeys, datasummary
    f2 = open('output.txt', 'w')
    for key in datakeys:
        f2.write('{}: {}\n'.format(key, datasummary[key]))
    f2.close()


# Calling the functions
readdata()
processdata()
printdata()
