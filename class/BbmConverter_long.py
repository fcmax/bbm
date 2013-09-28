# coding: utf8

class someClass:
    file = 'c:/f.bbm'

    def setData(self, data):
        self.dataDict = data
    

    def readFile(self):
        f = open(self.file, 'r')
        text = f.read().decode('Windows-1251')
        self.fileData = text.encode('utf8')
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
            player.setAttribute('ext_id', str(pl['ext_id']))
            player.setAttribute('number', str(pl['number']))
            player.setAttribute('sname', str(pl['sname']))
            player.setAttribute('fname', str(pl['fname']))
            player.setAttribute('is_start', str(pl['is_start']))
            player.setAttribute('point', str(pl['point']))
            player.setAttribute('fg2m', str(pl['fg2m']))
            player.setAttribute('fg2a', str(pl['fg2a']))
            player.setAttribute('fg3m', str(pl['fg3m']))
            player.setAttribute('fg3a', str(pl['fg3a']))
            player.setAttribute('ftm', str(pl['ftm']))
            player.setAttribute('fta', str(pl['fta']))
            player.setAttribute('assist', str(pl['assist']))
            player.setAttribute('steal', str(pl['steal']))
            player.setAttribute('block', str(pl['block']))
            player.setAttribute('rebdef', str(pl['rebdef']))
            player.setAttribute('reboff', str(pl['reboff']))
            player.setAttribute('turnover', str(pl['turnover']))
            player.setAttribute('foulopp', str(pl['foulopp']))
            player.setAttribute('foulpers', str(pl['foulpers']))
            player.setAttribute('time_played_sec', str(pl['time_played_sec']))
            player.setAttribute('time_played_min', str(pl['time_played_min']))
            team.appendChild(player)

        team = doc.createElement('team')
        team.setAttribute('pos', '2')
        match.appendChild(team)
        for pl in data['team2']:
            player = doc.createElement('player')
            player.setAttribute('ext_id', str(pl['ext_id']))
            player.setAttribute('number', str(pl['number']))
            player.setAttribute('sname', str(pl['sname']))
            player.setAttribute('fname', str(pl['fname']))
            player.setAttribute('is_start', str(pl['is_start']))
            player.setAttribute('point', str(pl['point']))
            player.setAttribute('fg2m', str(pl['fg2m']))
            player.setAttribute('fg2a', str(pl['fg2a']))
            player.setAttribute('fg3m', str(pl['fg3m']))
            player.setAttribute('fg3a', str(pl['fg3a']))
            player.setAttribute('ftm', str(pl['ftm']))
            player.setAttribute('fta', str(pl['fta']))
            player.setAttribute('assist', str(pl['assist']))
            player.setAttribute('steal', str(pl['steal']))
            player.setAttribute('block', str(pl['block']))
            player.setAttribute('rebdef', str(pl['rebdef']))
            player.setAttribute('reboff', str(pl['reboff']))
            player.setAttribute('turnover', str(pl['turnover']))
            player.setAttribute('foulopp', str(pl['foulopp']))
            player.setAttribute('foulpers', str(pl['foulpers']))
            player.setAttribute('time_played_sec', str(pl['time_played_sec']))
            player.setAttribute('time_played_min', str(pl['time_played_min']))
            team.appendChild(player)

        doc.normalize()
        return doc.toprettyxml(indent="  ")



        
        
        

            
            
        




        
        
    
    

  