def readFile():
    f = open('c:/1.bbm', 'r')
    lines = f.read()
    f.close()
    return lines

def getBlock(data, startWord, endWord):
    start = data.find(startWord)
    end = data.find(endWord)
    text = data[start+len(startWord)+1:end-1]
    list = text.split('\n')
    return list



lines = readFile()
afisha = getBlock(lines, '[Match]', '[Results]')
team1 = afisha[2].split(';')[2]
team2 = afisha[3].split(';')[2]

results = getBlock(lines, '[Results]', '[Status]')
result = results[0].split(';')
points1 = result[0::2]
points2 = result[1::2]
#some commited line

print points2





#out = readBlock(fileData, '[Match]', '[Results]')

#for a in lines:
    #print a
    