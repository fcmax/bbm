# coding: utf8


import os

class someClass:

    def setData(self, data):
        self.dataDict = data
    


    def readFile(self, file):
        f = open(file, 'r')
        #text = f.read().decode('Windows-1251')
        text = f.read()
        #self.fileData = text.encode('utf8')
        self.fileData = text
        f.close()


    def getBlock(self, startWord, endWord):
        start = self.fileData.find(startWord)
        end = self.fileData.find(endWord)
        text = self.fileData[start+len(startWord)+1:end-1]
        data = text.split('\n')
        data.remove('')
        return data

    def getResult(self, resBlock):
        result = resBlock[0].split(';')
        return {'p1': result[0::2], 'p2':result[1::2]}


    #############
#######################

    def getPlayers(self, team):
        team = team[2:]
        pl = []
        for row in team:
            r = row.split(';')
            if(int(r[0]) < 100):
                if (r[2]=='0'):
                    r[2]='100'

                p = {'ext_id':r[1], 'number':r[2], 'sname':r[3], 'fname':r[4], 'is_start':r[11], 'point':r[23],
                     'fg2m':r[24], 'fg2a':r[25], 'fg3m':r[26], 'fg3a':r[27],'ftm':r[28], 'fta':r[29], 'assist':r[30],
                     'steal':r[32], 'block':r[33], 'rebdef':r[34], 'reboff':r[35], 'turnover':int(r[37])+int(r[38]),
                     'foulopp':r[36], 'foulpers':r[39], 'time_played_sec':r[42], 'time_played_min':self.getMinutes(r[42])}
                pl.append(p)
        return pl

#####################
    #############

    
    def getMinutes(self, seconds):
        m, s = divmod(int(seconds), 60)
        h, m = divmod(m, 60)
        return "%d:%02d" % (m, s)


    def cleanOut(self, folder):
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception, e:
                print e
        return 'true'



    def makeXML(self):
        from xml.dom.minidom import Document
        data = self.dataDict
        doc = Document()
        match = doc.createElement('match')
        match.setAttribute('name', data['match'])
        match.setAttribute('result', data['result'])
        match.setAttribute('t1Points', "|".join(data['resultStr']['p1']))
        match.setAttribute('t2Points', "|".join(data['resultStr']['p2']))
        doc.appendChild(match)

        team = doc.createElement('team')
        team.setAttribute('pos', '1')
        match.appendChild(team)
        for pl in data['team1']:
            player = doc.createElement('player')
            for k,v in pl.items():
                player.setAttribute(k, str(v))
            team.appendChild(player)
            team.appendChild(player)

        team = doc.createElement('team')
        team.setAttribute('pos', '2')
        match.appendChild(team)
        for pl in data['team2']:
            player = doc.createElement('player')
            for k,v in pl.items():
                player.setAttribute(k, str(v))
            team.appendChild(player)

        doc.normalize()
        return doc.toprettyxml(indent="  ")



        
        
        

            
            
        




        
        
    
    

  