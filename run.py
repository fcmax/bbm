# coding: utf8


import os
import sys


sys.path.append("/Users/max1x2/Devlab/bbm/class/")
import BbmConverter


obj = BbmConverter.someClass()
outFolder = 'out/'

obj.cleanOut(outFolder)

bbmFiles = os.listdir('in/')

for f in bbmFiles:

	obj.readFile('in/'+f)
	match = obj.getBlock('[Match]', '[Results]')
	result = obj.getBlock('[Results]', '[Status]')
	team1 = obj.getBlock('[TeamA]', '[TeamB]')
	team2 = obj.getBlock('[TeamB]', '[Referees]')
	referees = obj.getBlock('[Referees]', '[Events]')
	events = obj.getBlock('[Events]', '[CommonStats]')

	res = obj.getResult(result)
	match = match[2].split(';')[2] + ' - ' + match[3].split(';')[2]

	data = {'resultStr':res, 'result': res['p1'][0]+':'+res['p2'][0]}
	data.update({'match':match})
	data.update({'team1':obj.getPlayers(team1)})
	data.update({'team2':obj.getPlayers(team2)})

	obj.setData(data)

	file = open(outFolder+f+'.xml', 'w')
	file.write(obj.makeXML())
	file.close()
    # I love Ira




#input('Press any key...')




    