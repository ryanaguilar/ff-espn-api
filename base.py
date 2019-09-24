from ff_espn_api import League
import pprint
import requests
import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Numeric
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

league_id = 372479
year = 2019
espn_s2 = 'AEAaGZHXv3kXMPXr4viwCvBYoTDLFWY8fQG7LQSLknXFpqPSSFRH2W0MSAXTTEGMWJg00zr4dLi8KPcEaqU3wLHgsyPWAp0evnI3BEdazrgInOkk55O3GScldvWUSV7bumfB%2FzGvdJu9cV7XyFpiS5I%2Bfiq31y3CrNFsIWmOZS7nh1Y7ouyoak0fpn8rBDx1OpbyuSo6b28Ff6gJ1qZaFZhNmMLVHFyCS5puOXA7yqH3VDHrGDktg9MqYJ2ZkTyMh9LcEqPij8doi1oCUMyDk52z'
SWID = 'C6F96922-51CD-484F-8A11-92181C47554F'
league_id2 = 12132683
league = League(league_id, year, espn_s2, SWID)
scoringleaders = league._return_scoring_leaders('2')

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
    weekly = Table('mytable', meta,
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
                    Column('ff_team', String),
                    Column('onteam_status', String),
                    Column('on_team_id', Integer),
                    Column('pro_team_id', Integer),
                    Column('position_id', Integer),
                    Column('jersey', Integer),
                    Column('bye_wk', Integer),
                    Column('position_name', String)
                   )
    weekly.create(engine)


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
        self.jersey = self['player'].get('jersey')
        #self.stats = self['player']['stats']
        self.position_id  = self['player']['defaultPositionId']
        try:
            self.bye_wk = self['player']['outlooks']['outlooksByeWeek']
        except KeyError:
            self.bye_wk = '0'
        #self. = self['player']['stats'][-1]['stats'][]
        try:
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
            self.receptions = self['player']['stats'][-1]['stats'].get('41', 0)
            self.receiving_yds = self['player']['stats'][-1]['stats'].get('42', 0)
            self.receiving_tds = self['player']['stats'][-1]['stats'].get('43', 0)
            self.tar = self['player']['stats'][-1]['stats'].get('58', 0)
            self.twopc = self['player']['stats'][-1]['stats'].get('62', 0)
            self.fg = self['player']['stats'][-1]['stats'].get('83', 0)
            self.fga = self['player']['stats'][-1]['stats'].get('84', 0)
            self.fg39 = self['player']['stats'][-1]['stats'].get('80',0)
            self.fga39 = self['player']['stats'][-1]['stats'].get('81',0)
            self.fg49 = self['player']['stats'][-1]['stats'].get('77',0)
            self.fga49 = self['player']['stats'][-1]['stats'].get('78',0)
            self.fg50 = self['player']['stats'][-1]['stats'].get('74',0)
            self.fga50 = self['player']['stats'][-1]['stats'].get('75',0)
            self.xp =self['player']['stats'][-1]['stats'].get('86',0)
            self.xpa =self['player']['stats'][-1]['stats'].get('87',0)

            self.position_name = self.position_map()
            self.ff_team = self.ff_team_map()
            self.pro_team = self.pro_team_map()

            self.df_dict = {
                'id':self.id,
                'name':self.name,
                'on_team_id':self.on_team_id,
                'pro_team_id':self.pro_team_id,
                'jersey':self.jersey,
                'position_id':self.position_id,
                'bye_wk':self.bye_wk,
                'pts':self.pts,
                'avg_pts':self.avg_pts,
                'attempts':self.attempts,
                'completed':self.completed,
                'passing_yds':self.passing_yds,
                'completion_pct':self.completion_pct,
                'interceptions':self.interceptions,
                'passing_tds':self.passing_tds,
                'rushing_tds':self.rushing_tds,
                'rushing_yds':self.rushing_yds,
                'rushes':self.rushes,
                'receptions':self.receptions,
                'receiving_yds':self.receiving_yds,
                'receiving_tds':self.receiving_tds,
                'tar':self.tar,
                'twopc':self.twopc,
                'position_name':self.position_map(),
                'ff_team':self.ff_team_map(),
                'pro_team':self.pro_team_map(),
                'fg':self.fg,
                'fga':self.fga,
                'fg39':self.fg39,
                'fga39':self.fga39,
                'fg49':self.fg49,
                'fga49':self.fga49,
                'fg50':self.fg50,
                'fga50':self.fga50,
                'xp':self.xp,
                'xpa':self.xpa
        }
        except KeyError:
            self.df_dict = {}

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
            12:'HOG',
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

    def load_row(self, engine, table, player):
        stmt = table.update().values(player)

    def load_all(self):
        engine = create_engine('sqlite+pysqlite:///sqlite3.db')
        #Session = sessionmaker(bind=engine)
        #session = Session()
        #Base = declarative_base()
        meta = MetaData()
        weekly = Table('mytable', meta,
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
                    Column('ff_team', String),
                    Column('onteam_status', String),
                    Column('on_team_id', Integer),
                    Column('pro_team_id', Integer),
                    Column('position_id', Integer),
                    Column('jersey', Integer),
                    Column('bye_wk', Integer),
                    Column('position_name', String)

                    )
        weekly.create(engine)


def fill_list(scoringleaders):
    players = scoringleaders['players']
    big_list = [Player(players, leader['player']['fullName']).df_dict for leader in players]
    return big_list

def list_to_csv(big_list, file_name):
    df = pd.DataFrame(data=big_list)
    df.to_csv(file_name)

def weekly(previous, current, week):
    df3 = pd.DataFrame()
    df3['id'] = df2['id']
    df3['name'] = df2['name']
    df3['on_team_id'] = df2['on_team_id']
    df3['pro_team_id'] = df2['pro_team_id']
    df3['jersey'] = df2['jersey']
    df3['position_id'] = df2['position_id']
    df3['bye_wk'] = df2['bye_wk']
    df3['pts'] = df2['pts'] - df1['pts']
    df3['avg_pts'] = df2['avg_pts']
    df3['attempts'] = df2['attempts'] - df1['attempts']
    df3['completed'] = df2['completed'] - df1['completed']
    df3['passing_yds'] = df2['passing_yds'] - df1['passing_yds']
    df3['completion_pct'] = df3['completed'] / df3['attempts']
    df3['interceptions'] = df2['interceptions'] - df1['interceptions']
    df3['passing_tds'] = df2['passing_tds'] - df1['passing_tds']
    df3['rushing_tds'] = df2['rushing_tds'] - df1['rushing_tds']
    df3['rushing_yds'] = df2['rushing_yds'] - df1['rushing_yds']
    df3['rushes'] = df2['rushes'] - df1['rushes']
    df3['receptions'] = df2['receptions'] = df1['receptions']
    df3['receiving_yds'] = df2['receiving_yds'] - df1['receiving_yds']
    df3['tar'] = df2['tar'] - df1['tar']
    df3['twopc'] = df2['twopc'] - df1['twopc']
    df3['position_name'] = df2['position_name']
    df3['ff_team'] = df2['ff_team']
    df3['pro_team'] = df2['pro_team']
    df3['fg'] = df2['fg'] - df1['fg']
    df3['fga'] = df2['fga'] - df1['fga']
    df3['fga39'] = df2['fga39'] - df1['fga39']
    df3['fg49'] = df2['fg49'] - df1['fg49']
    df3['fga49'] = df2['fga49'] - df1['fga49']
    df3['fg50'] = df2['fg50'] - df1['fg50']
    df3['fga50'] = df2['fga50'] - df1['fga50']
    df3['xp'] = df2['xp'] = df1['xp']
    df3['xpa'] = df2['xpa'] - df1['xpa']
    return df3