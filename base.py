from ff_espn_api import League
import pprint
import requests
import json

league_id = 372479
year = 2019
espn_s2 = 'AEAaGZHXv3kXMPXr4viwCvBYoTDLFWY8fQG7LQSLknXFpqPSSFRH2W0MSAXTTEGMWJg00zr4dLi8KPcEaqU3wLHgsyPWAp0evnI3BEdazrgInOkk55O3GScldvWUSV7bumfB%2FzGvdJu9cV7XyFpiS5I%2Bfiq31y3CrNFsIWmOZS7nh1Y7ouyoak0fpn8rBDx1OpbyuSo6b28Ff6gJ1qZaFZhNmMLVHFyCS5puOXA7yqH3VDHrGDktg9MqYJ2ZkTyMh9LcEqPij8doi1oCUMyDk52z'
SWID = 'C6F96922-51CD-484F-8A11-92181C47554F'
league_id2 = 12132683
league = League(league_id, year, espn_s2, SWID)
scoringleaders = league._return_scoring_leaders()

def get_stats(player, period):
    stats = player['stats']
    for item in stats:
        if item['id'] == period + '2019':
            objectplayer['pts'] = item['appliedTotal']
            objectplayer['avg_pts'] = item['appliedAverage']
            objectplayer['attempts'] = item['stats']['0']
            objectplayer['completed'] = item['stats']['1']
            objectplayer['passing_yds'] = item['stats']['3']
            objectplayer['completion_pct'] = item['stats']['21']
            #guess objectplayer['interceptions'] = item['stats']['20']
            objectplayer['passing_tds'] = item['stats']['4']
            objectplayer['rushes'] = item['stats']['23']
            objectplayer['rushing_yds'] = item['stats']['24']
            objectplayer['rushing_tds'] = item['stats']['25']
            print(item['appliedTotal'])

def create_dict():
    pass

def insert_sql(player_dict):
    pass

def search_by_name(players, searchname):
    for i,player in enumerate(players):
        if player['player']['fullName'] == searchname:
            print(searchname + ' found')
            return player

stats_map = {
    '0':'attempts',
    '1':'completions',
    '10':'',
    '11':'',
    '12':'',
    '13':'',
    '14':'',
    '155':'',
    '175':''
}

class Player(dict):
    def __init__(self, playerlist, name):
        super(Player, self).__init__(search_by_name(playerlist, name))
        self.id = self['id']
        self.name = self['player']['fullName']
        self.stats = self['player']['stats'][-1]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]
        #self. = self['player']['stats']['stats'][]

