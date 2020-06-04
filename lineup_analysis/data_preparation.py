import pandas as pd
import numpy as np
import requests
import json

headers = {'Host': 'stats.nba.com','User-Agent': 'Firefox/55.0', 'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Referer': 'https://stats.nba.com/','x-nba-stats-origin': 'stats','x-nba-stats-token': 'true','DNT': '1',}

################################################## TEAM STATS

tm_list = []

for ssn in ['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20']:

    url = 'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='
    
    json = requests.get(url, headers=headers).json()

    data = json['resultSets'][0]['rowSet']
    columns = json['resultSets'][0]['headers']
    
    tm_db = pd.DataFrame.from_records(data, columns=columns)
    
    tm_db['SEASON'] = ssn

    tm_list.append(tm_db)
    
tm_db = pd.concat(tm_list).reset_index(drop=True)

tm_db = tm_db[['TEAM_ID','SEASON','NET_RATING']]
tm_db.columns = ['TEAM_ID','SEASON','TEAM_NET_RATING']

################################################## LINEUP STATS

df_list = []

for ssn in ['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20']:
    
    url = 'https://stats.nba.com/stats/leaguedashlineups?Conference=&DateFrom=&DateTo=&Division=&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=0&VsConference=&VsDivision='

    json = requests.get(url, headers=headers).json()

    data = json['resultSets'][0]['rowSet']
    columns = json['resultSets'][0]['headers']

    df = pd.DataFrame.from_records(data, columns=columns) 
    
    df = df[['GROUP_ID','TEAM_ID','POSS','OFF_RATING','DEF_RATING','NET_RATING']]
    
    df['SEASON'] = ssn
    
    df_list.append(df)

df = pd.concat(df_list).reset_index(drop=True)
    
def player_id(c):
    return c.split('-')[1],c.split('-')[2],c.split('-')[3],c.split('-')[4],c.split('-')[5]
df['id1'],df['id2'],df['id3'],df['id4'],df['id5'] = np.vectorize(player_id)(df.GROUP_ID)

df.id1 = pd.to_numeric(df.id1)
df.id2 = pd.to_numeric(df.id2)
df.id3 = pd.to_numeric(df.id3)
df.id4 = pd.to_numeric(df.id4)
df.id5 = pd.to_numeric(df.id5)

################################################## GET LINEUP AVERAGE POSSESSIONS FOR EACH TEAM

row_list = []

for ssn in ['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20']:
    
    tef = df[df.SEASON == ssn].reset_index(drop=True)
    
    tms = tef.TEAM_ID.unique()
    
    for tm in tms:
        
        tmf = tef[tef.TEAM_ID == tm].reset_index(drop=True)
        
        avg_poss = tmf.POSS.mean()
        
        dict1 = {'TEAM_ID':tm,'SEASON':ssn,'AVG_POSS':avg_poss}
        
        row_list.append(dict1)
        
possdf = pd.DataFrame(row_list)

################################################## GET PLAYER_IDS, TEAM NET RATINGS, CLUSTERS

db = pd.read_csv('https://raw.githubusercontent.com/ahmed-cheema/nba-classification/master/lineup_analysis/player_clusters.csv')

for ssn in ['2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20']:
    
    url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

    json = requests.get(url, headers=headers).json()

    data = json['resultSets'][0]['rowSet']
    columns = json['resultSets'][0]['headers']

    yr_df = pd.DataFrame.from_records(data, columns=columns) 
    
    yr_df['SEASON'] = ssn

    db = pd.merge(db,yr_df[['PLAYER_NAME','SEASON','PLAYER_ID']],on=['PLAYER_NAME','SEASON'],how='left')
    
db.columns = ['PLAYER_NAME','SEASON','cluster','classification','ID14','ID15','ID16','ID17','ID18','ID19','ID20']

def id_condense(id14,id15,id16,id17,id18,id19,id20):
    return int([n for n in [id14,id15,id16,id17,id18,id19,id20] if str(n) != 'nan'][0])
db['PLAYER_ID'] = np.vectorize(id_condense)(db.ID14,db.ID15,db.ID16,db.ID17,db.ID18,db.ID19,db.ID20)

db = db[['PLAYER_NAME','PLAYER_ID','SEASON','cluster','classification']]

################################################## GET PLAYER_IDS, TEAM NET RATINGS, CLUSTERS

tf = pd.merge(df,db[['PLAYER_ID','SEASON','PLAYER_NAME','classification']],left_on=['id1','SEASON'],right_on=['PLAYER_ID','SEASON'])

tf = pd.merge(tf,db[['PLAYER_ID','SEASON','PLAYER_NAME','classification']],left_on=['id2','SEASON'],right_on=['PLAYER_ID','SEASON'])

tf = pd.merge(tf,db[['PLAYER_ID','SEASON','PLAYER_NAME','classification']],left_on=['id3','SEASON'],right_on=['PLAYER_ID','SEASON'])

tf = pd.merge(tf,db[['PLAYER_ID','SEASON','PLAYER_NAME','classification']],left_on=['id4','SEASON'],right_on=['PLAYER_ID','SEASON'])

tf = pd.merge(tf,db[['PLAYER_ID','SEASON','PLAYER_NAME','classification']],left_on=['id5','SEASON'],right_on=['PLAYER_ID','SEASON'])

tf = pd.merge(tf,tm_db[['TEAM_ID','SEASON','TEAM_NET_RATING']],on=['TEAM_ID','SEASON'])

tf = pd.merge(tf,possdf[['TEAM_ID','SEASON','AVG_POSS']],on=['TEAM_ID','SEASON'])

tf.columns = ['group_id','team','poss','ortg','drtg','nrtg','ssn','id1','id2','id3','id4','id5','player_id_1','player_name_1','p1','player_id_2','player_name_2','p2','player_id_3','player_name_3','p3','player_id_4','player_name_4','p4','player_id_5','player_name_5','p5','tm_nrtg','avg_poss']

tf = tf[['team','ssn','poss','tm_nrtg','avg_poss','ortg','drtg','nrtg','p1','p2','p3','p4','p5']]
