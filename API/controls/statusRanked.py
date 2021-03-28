from bs4 import BeautifulSoup
import requests
import re
import json

class PontosRanked:

    def __init__(self):
        self.nick = None
        self.rank = None
        self.points = None
        self.icon = None
        self.total_win = None
        self.total_lose = None

    def connect(self,nickname):
        self.nick = re.sub('[+]',' ',nickname)
        
        result = requests.get('https://br.op.gg/summoner/userName='+nickname)
        html_content = result.content
        self.soup = BeautifulSoup(html_content,'html.parser')
        return self.status_ranked()

    def status_ranked(self):
        list_status = []
        # rank
        for result in self.soup.find_all('div',class_='TierRank'):
            self.rank = result.text
        # points
        for result in self.soup.find_all('span',class_='LeaguePoints'):
            self.points = re.sub('\t','',result.text)
        # icon
        for result in self.soup.find_all('div',class_='SummonerRatingMedium',href=True):
            print(result)
        # total win
        for result in self.soup.find_all('span',class_='wins'):
            self.total_win = result.text
        # total lose
        for result in self.soup.find_all('span',class_='losses'):
            self.total_lose = result.text

        return self.status_update()

    def status_update(self):
        status_list = []
        status_dict = {'nick':self.nick,
                            'rank':self.rank,
                            'points':self.points,
                            #'icon':self.icon,
                            'total_win':self.total_win,
                            'total_lose':self.total_lose}

        status_list.append(status_dict)
        print(status_list)
        return status_list
            
    