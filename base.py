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
        self.on_team_id = self['onTeamId']
        self.pro_team_id = self['player']['proTeamId']
        self.jersey = self['player']['jersey']
        self.stats = self['player']['stats']
        self.position_id  = self['player']['defaultPositionId']
        try:
            self.bye_wk = self['player']['outlooks']['outlooksByeWeek']
        except KeyError:
            self.bye_wk = '0'
        #self. = self['player']['stats'][-1]['stats'][]
        self.pts = self['player']['stats'][-1]['appliedTotal']
        self.avg_pts = self['player']['stats'][-1].get('appliedAverage', 0)
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

        self.position_name = self.position_map()
        self.ff_team = self.ff_team_map()
        self.pro_team = self.pro_team_map()

    def position_map(self):
        position_name = {
            1:'QB',
            2:'RB',
            3:'WR',
            4:'TE',
            5:'K',
            6:'IDP',
            7: 'IDP',
            8: 'IDP',
            9: 'IDP',
            10: 'IDP',
            11: 'IDP',
            12: 'IDP',
            13: 'IDP',
            14: 'IDP',
            15: 'IDP',
            16: 'DST'

        }
        return position_name[self.position_id]

    def ff_team_map(self):
        ff_team_map = {
            0: 'FA',
            1:'KIM',
            2:'FBI',
            3:'LEE',
            4:'CHUB',
            5:'',
            6:'BRY',
            7:'MATT',
            8:'ASS',
            9:'MPB',
            10:'GM',
            11:'GGWL',
            12:'HOG'
            13:'LUER'
        }
        return ff_team_map[self.on_team_id]

    def pro_team_map(self):
        pro_team_map = {
            0:'FA',
            1:'ATL',
            2:'BUF',
            3:'CHI',
            4:'CIN',
            5:'CLE',
            6:'DAL',
            7:'DEN',
            8:'DET',
            9:'GB',
            10:'TEN',
            11:'IND',
            12:'KC',
            13:'OAK',
            14:'LAR',
            15:'MIA',
            16:'MIN',
            17:'NE',
            18:'NO',
            19:'NYG',
            20:'NYJ',
            21:'PHI',
            22:'ARI',
            23:'PIT',
            24:'LAC',
            25:'SF',
            26:'SEA',
            27:'TB',
            28:'WAS',
            29:'CAR',
            30:'JAX',
            31:'',
            32:'',
            33:'BAL',
            34:'HOU'

        }
        return pro_team_map[self.pro_team_id]

    def load_to_sql(self, engine):
        pass


table = Table(
    "week1", metadata,
    Column("id")
)

