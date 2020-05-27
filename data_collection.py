import pandas as pd
import numpy as np
import requests
import json

headers = {'Host': 'stats.nba.com','User-Agent': 'Firefox/55.0', 'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Referer': 'https://stats.nba.com/','x-nba-stats-origin': 'stats','x-nba-stats-token': 'true','DNT': '1',}

ssn = '2019-20'

# retrieve the 22 data sets that will be merged to include all of our final 189 features

#############################
# basic stats

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df = pd.DataFrame.from_records(data, columns=columns) 

#############################
# height / weight

url = 'https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

db = pd.DataFrame.from_records(data, columns=columns) 

#############################
# deflections

url = 'https://stats.nba.com/stats/leaguehustlestatsplayer?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df2 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# passing

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Passing&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df3 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# speed / distance

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=SpeedDistance&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df4 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# touches

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Possessions&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df5 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# scoring

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Efficiency&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df6 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# defense

url = 'https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df7 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# advanced

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df8 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# misc scoring

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Misc&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df9 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# dws

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Defense&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df10 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# rebounding

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Rebounding&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df11 = pd.DataFrame.from_records(data, columns=columns) # rebounding

#############################
# shooting zones

url = 'https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets']['rowSet']
columns = json['resultSets']['headers'][1]['columnNames']

df12 = pd.DataFrame.from_records(data, columns=columns) 

df12.columns = ['PLAYER_ID','PLAYER_NAME','TEAM_ID','TEAM_ABBREVIATION','AGE','RAFGM','RAFGA','RAFG_PCT','PFGM','PFGA','PFG_PCT','MRFGM','MRFGA','MRFG_PCT','LCFG3M','LCFG3A','LCFG3_PCT','RCFG3M','RCFG3A','RCFG3_PCT','CFG3M','CFG3A','CFG3_PCT','ABFG3M','ABFG3A','ABFG3_PCT']

#############################
# assisted / unassisted scoring

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Scoring&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df13 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# usage stats

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Usage&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df14 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# isolation plays

url = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=Isolation&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive'

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df15 = pd.DataFrame.from_records(data, columns=columns) # iso

df15.rename(columns={'POSS_PCT':'ISO_POSS_PCT','EFG_PCT':'ISO_EFG_PCT','PTS':'ISO_PTS'}, inplace=True)

g = df15.groupby(['PLAYER_NAME'])

df15 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['ISO_POSS_PCT','ISO_EFG_PCT']],weights=x['POSS'],axis=0),['ISO_POSS_PCT','ISO_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['ISO_PTS']).reset_index(drop=False),on='PLAYER_NAME')

#############################
# pnr ball handler

url = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=PRBallHandler&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive'

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df16 = pd.DataFrame.from_records(data, columns=columns) 

df16.rename(columns={'POSS_PCT':'PRBH_POSS_PCT','EFG_PCT':'PRBH_EFG_PCT','PTS':'PRBH_PTS'}, inplace=True)

g = df16.groupby(['PLAYER_NAME'])

df16 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['PRBH_POSS_PCT','PRBH_EFG_PCT']],weights=x['POSS'],axis=0),['PRBH_POSS_PCT','PRBH_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['PRBH_PTS']).reset_index(drop=False),on='PLAYER_NAME')

#############################
# pnr roll man

url = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=PRRollMan&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive'

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df17 = pd.DataFrame.from_records(data, columns=columns) 

df17.rename(columns={'POSS_PCT':'PRRM_POSS_PCT','EFG_PCT':'PRRM_EFG_PCT','PTS':'PRRM_PTS'}, inplace=True)

g = df17.groupby(['PLAYER_NAME'])

df17 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['PRRM_POSS_PCT','PRRM_EFG_PCT']],weights=x['POSS'],axis=0),['PRRM_POSS_PCT','PRRM_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['PRRM_PTS']).reset_index(drop=False),on='PLAYER_NAME')

#############################
# spot up

url = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=Spotup&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=' + str(ssn) + '&TypeGrouping=offensive'

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df18 = pd.DataFrame.from_records(data, columns=columns) 

df18.rename(columns={'POSS_PCT':'SU_POSS_PCT','EFG_PCT':'SU_EFG_PCT','PTS':'SU_PTS'}, inplace=True)
                 
g = df18.groupby(['PLAYER_NAME'])

df18 = pd.merge(g.apply(lambda x: pd.Series(np.average(x[['SU_POSS_PCT','SU_EFG_PCT']],weights=x['POSS'],axis=0),['SU_POSS_PCT','SU_EFG_PCT'])).reset_index(drop=False),pd.DataFrame(g.sum()['SU_PTS']).reset_index(drop=False),on='PLAYER_NAME')

#############################
# drives

url = 'https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Drives&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

df19 = pd.DataFrame.from_records(data, columns=columns) 

#############################
# advanced value stats

df20 = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_advanced.html', header=0)[0][['Player','PER','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']]

df20.columns = ['PLAYER_NAME','PER','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']

df20 = df20[df20.PLAYER_NAME !='Player'].reset_index(drop=True)

df20 = df20.drop_duplicates(subset=['PLAYER_NAME'],keep='first').reset_index(drop=True)

# basketball-reference names sometime differ from stats.nba.com names, so these discrepancies must be fixed

def remove_accents(a):
    return unidecode.unidecode(a)
df20['PLAYER_NAME'] = df20['PLAYER_NAME'].apply(remove_accents)

df20['PLAYER_NAME'].replace({'Robert Williams':'Robert Williams III','Marcus Morris':'Marcus Morris Sr.','Derrick Walton':'Derrick Walton Jr.','Juan Hernangomez':'Juancho Hernangomez','Sviatoslav Mykhailiuk':'Svi Mykhailiuk','Zach Norvell':'Zach Norvell Jr.','Lonnie Walker':'Lonnie Walker IV','Charlie Brown':'Charles Brown Jr.','C.J. Miles':'CJ Miles','Wesley Iwundu':'Wes Iwundu','J.J. Redick':'JJ Redick','B.J. Johnson':'BJ Johnson','Melvin Frazier':'Melvin Frazier Jr.','Otto Porter':'Otto Porter Jr.','James Ennis':'James Ennis III','Danuel House':'Danuel House Jr.','Brian Bowen':'Brian Bowen II','Kevin Knox':'Kevin Knox II','Frank Mason III':'Frank Mason','Harry Giles':'Harry Giles III','T.J. Leaf':'TJ Leaf','J.R. Smith':'JR Smith','Vince Edwards':'Vincent Edwards','D.J. Stephens':'DJ Stephens','Mitch Creek':'Mitchell Creek','R.J. Hunter':'RJ Hunter','Wade Baldwin':'Wade Baldwin IV'},inplace=True)

#############################
# positions

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=C&PlusMinus=N&Rank=N&Season=' +str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

c_df = pd.DataFrame.from_records(data, columns=columns) # CENTERS
    
###

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=G&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

g_df = pd.DataFrame.from_records(data, columns=columns) # GUARDS
    
###

url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=F&PlusMinus=N&Rank=N&Season=' + str(ssn) + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

json = requests.get(url, headers=headers).json()

data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']

f_df = pd.DataFrame.from_records(data, columns=columns) # FORWARDS

c_df['position'] = 'C'
g_df['position'] = 'G'
f_df['position'] = 'F'

pf = pd.concat([c_df,g_df,f_df]).reset_index(drop=True)
pf = pf[['PLAYER_NAME','PLAYER_ID','AGE','MIN','position']]
pf.columns = ['player','player_id','age','mp','position']

row_list = []

for n in pf.player.unique():
    
    tf = pf[pf.player == n].reset_index(drop=True)
    posf = pd.DataFrame(tf.groupby('position')['mp'].sum()).sort_values(by='mp',ascending=False).reset_index(drop=False)
    
    pos1 = posf.position[0]

    if posf.shape[0] > 1:
        pos2 = posf.position[1]
    else:
        pos2 = None
    if posf.shape[0] > 2:
        pos3 = posf.position[2]
    else:
        pos3 = None
    
    dict1 = {'player':n,'pos1':pos1,'pos2':pos2,'pos3':pos3}
    
    row_list.append(dict1)
    
pfin = pd.DataFrame(row_list)[['player','pos1','pos2','pos3']]
pfin.columns = ['PLAYER_NAME','POSITION','pos2','pos3']

#############################
