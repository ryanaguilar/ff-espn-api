from ff_espn_api import League
import pprint
import requests
import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Numeric
import pandas

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

def setup_weekly_table():
    meta = MetaDatat()
    mytable = Table('mytable', meta,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('pts', Numeric),
                Column('attempts', Integer),
                Column('completed', Integer),
                Column('passing_yds', Numeric),
                    Column('completion_pct', Numeric),
                    Column('intercetptions', Integer),
                    Column('passing_tds', Integer),
                    Column('rushes', Integer),
                    Column('rushing_yds', Numeric),
                    Column('rushing_tds', Integer),
                    Column('rushing_tds', Integer),
                    Column('fumbles', Integer),
                    Column('receptions', Integer),
                    Column('receiving_yds', Numeric),
                    Column('receiving_tds', Integer),
                    Column('tar', Integer),
                    Column('twopc', Integer),
                    Column('projection', Numeric),
                    Column('opponent', String),
                    Column('fteam', String),
                    Column('onteam_status', String),
                    Column('proteam', Integer)

    )

def create_dict():
    pass

def insert_sql(player_dict):
    pass

def search_by_name(players, searchname):
    for i,player in enumerate(players):
        if player['player']['fullName'] == searchname:
            print(searchname + ' found')
            return player


class Player(dict):
    def __init__(self, playerlist, name):
        super(Player, self).__init__(search_by_name(playerlist, name))
        self.id = self['id']
        self.name = self['player']['fullName']
        self.stats = self['player']['stats']
        #self. = self['player']['stats'][-1]['stats'][]
        self.pts = self['player']['stats'][-1]['appliedTotal']
        self.avg_pts = self['player']['stats'][-1]['appliedAverage']
        self.attempts = self['player']['stats'][-1]['stats'].get('0', 0)
        self.completed = self['player']['stats'][-1]['stats'].get('1', 0)
        self.passing_yds = self['player']['stats'][-1]['stats'].get('3', 0)
        self.completion_pct = self['player']['stats'][-1]['stats'].get('21', 0)
        self.interceptions = self['player']['stats'][-1]['stats'].get('20', 0)
        self.passing_tds = self['player']['stats'][-1]['stats'].get('4', 0)
        self.rushing_tds = self['player']['stats'][-1]['stats'].get('25', 0)
        self.rushing_yds = self['player']['stats'][-1]['stats'].get('24', 0)
        self.rushes = self['player']['stats'][-1]['stats'].get('23', 0)
        self.recptions = self['player']['stats'][-1]['stats'].get('41', 0)
        self.receiving_yds = self['player']['stats'][-1]['stats'].get('42', 0)
        self.receiving_tds = self['player']['stats'][-1]['stats'].get('43', 0)
        self.tar = self['player']['stats'][-1]['stats'].get('58', 0)
        self.twopc = self['player']['stats'][-1]['stats'].get('62', 0)

    def load_to_sql(self, engine):
        pass


table = Table(
    "week1", metadata,
    Column("id")
)

