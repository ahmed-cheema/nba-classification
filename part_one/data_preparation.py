import pandas as pd
import numpy as np

#############################
# now, all 22 dataframes can be merged into one: df

df = df[['PLAYER_NAME','AGE','GP','MIN','FGM','FGA','FG3M','FG3A','FTM','FTA','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','PTS']]

df = pd.merge(df,pfin[['PLAYER_NAME','POSITION']],on='PLAYER_NAME')

df = pd.merge(df,pd.get_dummies(df.POSITION), left_index=True, right_index=True) # one-hot encoding on position to create three columns: C, G, F

df = pd.merge(df,db[['PLAYER_NAME','PLAYER_HEIGHT_INCHES','PLAYER_WEIGHT','NET_RATING','OREB_PCT','DREB_PCT','USG_PCT','TS_PCT','AST_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df2[['PLAYER_NAME','CONTESTED_SHOTS','CONTESTED_SHOTS_2PT','CONTESTED_SHOTS_3PT','DEFLECTIONS','CHARGES_DRAWN','SCREEN_ASSISTS','SCREEN_AST_PTS','OFF_LOOSE_BALLS_RECOVERED','DEF_LOOSE_BALLS_RECOVERED','LOOSE_BALLS_RECOVERED','OFF_BOXOUTS','DEF_BOXOUTS','BOX_OUT_PLAYER_TEAM_REBS','BOX_OUT_PLAYER_REBS','BOX_OUTS']],on='PLAYER_NAME',how='left')
    
df = pd.merge(df,df3[['PLAYER_NAME','PASSES_MADE','PASSES_RECEIVED','FT_AST','SECONDARY_AST','POTENTIAL_AST','AST_PTS_CREATED']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df4[['PLAYER_NAME','DIST_MILES','DIST_MILES_OFF','DIST_MILES_DEF','AVG_SPEED','AVG_SPEED_OFF','AVG_SPEED_DEF']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df5[['PLAYER_NAME','TOUCHES','FRONT_CT_TOUCHES','TIME_OF_POSS','AVG_SEC_PER_TOUCH','AVG_DRIB_PER_TOUCH','PTS_PER_TOUCH','ELBOW_TOUCHES','POST_TOUCHES']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df6[['PLAYER_NAME','DRIVE_PTS','DRIVE_FG_PCT','CATCH_SHOOT_PTS','CATCH_SHOOT_FG_PCT','PULL_UP_PTS','PULL_UP_FG_PCT','PAINT_TOUCH_PTS','PAINT_TOUCH_FG_PCT','POST_TOUCH_PTS','POST_TOUCH_FG_PCT','ELBOW_TOUCH_PTS','ELBOW_TOUCH_FG_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df7[['PLAYER_NAME','D_FGM','D_FGA','D_FG_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df8[['PLAYER_NAME','OFF_RATING','DEF_RATING','AST_RATIO','PACE','PIE']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df9[['PLAYER_NAME','PTS_OFF_TOV','PTS_2ND_CHANCE','PTS_FB','PTS_PAINT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df10[['PLAYER_NAME','DEF_WS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df11[['PLAYER_NAME','AVG_REB_DIST','REB_CHANCE_PCT','REB_CHANCE_PCT_ADJ','REB_CHANCES','REB_CONTEST_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df12[['PLAYER_NAME','RAFGM','RAFGA','RAFG_PCT','PFGM','PFGA','PFG_PCT','MRFGM','MRFGA','MRFG_PCT','LCFG3M','LCFG3A','LCFG3_PCT','RCFG3M','RCFG3A','RCFG3_PCT','CFG3M','CFG3A','CFG3_PCT','ABFG3M','ABFG3A','ABFG3_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df13[['PLAYER_NAME','PCT_FGA_2PT','PCT_FGA_3PT','PCT_PTS_2PT','PCT_PTS_2PT_MR','PCT_PTS_3PT','PCT_PTS_FB','PCT_PTS_FT','PCT_PTS_OFF_TOV','PCT_PTS_PAINT','PCT_AST_2PM','PCT_UAST_2PM','PCT_AST_3PM','PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df14[['PLAYER_NAME','PCT_FGM','PCT_FGA','PCT_FG3M','PCT_FG3A','PCT_FTM','PCT_FTA','PCT_OREB','PCT_DREB','PCT_REB','PCT_AST','PCT_TOV','PCT_STL','PCT_BLK','PCT_BLKA','PCT_PF','PCT_PFD','PCT_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df15[['PLAYER_NAME','ISO_POSS_PCT','ISO_EFG_PCT','ISO_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df16[['PLAYER_NAME','PRBH_POSS_PCT','PRBH_EFG_PCT','PRBH_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df17[['PLAYER_NAME','PRRM_POSS_PCT','PRRM_EFG_PCT','PRRM_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df18[['PLAYER_NAME','SU_POSS_PCT','SU_EFG_PCT','SU_PTS']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df19[['PLAYER_NAME','DRIVES','DRIVE_AST_PCT','DRIVE_PASSES_PCT']],on='PLAYER_NAME',how='left')

df = pd.merge(df,df20[['PLAYER_NAME','PER','OWS','WS','WS/48','OBPM','DBPM','BPM','VORP']],on='PLAYER_NAME',how='left')

#############################
# feature engineering

df['TIME_OF_POSS_36'] = 36*(df['TIME_OF_POSS']/df.MIN)
df['OFB_PCT'] = 1-(df['TIME_OF_POSS']/df.MIN)
df['PCT_PTS_ISO'] = df.ISO_PTS / df.PTS
df['PCT_PTS_PRBH'] = df.PRBH_PTS / df.PTS
df['PCT_PTS_PRRM'] = df.PRRM_PTS / df.PTS
df['PCT_PTS_SU'] = df.SU_PTS / df.PTS
df['PCT_PTS_DRIVES'] = df.DRIVE_PTS / df.PTS

df['FG2M'] = df.FGM - df.FG3M
df['FG2A'] = df.FGA - df.FG3A

df['FG_PCT'] = df.FGM/df.FGA
df['FG2_PCT'] = df.FG2M/df.FG2A
df['FG3_PCT'] = df.FG3M/df.FG3A
df['FT_PCT'] = df.FTM/df.FTA

df['AST_TO'] = df.AST/df.TOV
df['MPG'] = df.MIN/df.GP
df['EFG'] = (df.FG2M + 1.5*df.FG3M) / df.FGA
df['FTR'] = df.FTA/df.FGA

# convert volume stats to per-36 stats

for n in ['FGM','FGA','FG2M','FG2A','FG3M','FG3A','FTM','FTA','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','PTS','CONTESTED_SHOTS','CONTESTED_SHOTS_2PT','CONTESTED_SHOTS_3PT','DEFLECTIONS','CHARGES_DRAWN','SCREEN_ASSISTS','SCREEN_AST_PTS','OFF_LOOSE_BALLS_RECOVERED','DEF_LOOSE_BALLS_RECOVERED','LOOSE_BALLS_RECOVERED','OFF_BOXOUTS','DEF_BOXOUTS','BOX_OUT_PLAYER_TEAM_REBS','BOX_OUT_PLAYER_REBS','BOX_OUTS','PASSES_MADE','PASSES_RECEIVED','FT_AST','SECONDARY_AST','POTENTIAL_AST','AST_PTS_CREATED','DIST_MILES','DIST_MILES_OFF','DIST_MILES_DEF','TOUCHES','FRONT_CT_TOUCHES','ELBOW_TOUCHES','POST_TOUCHES','DRIVE_PTS','CATCH_SHOOT_PTS','PULL_UP_PTS','PAINT_TOUCH_PTS','POST_TOUCH_PTS','ELBOW_TOUCH_PTS','D_FGM','D_FGA','PTS_OFF_TOV','PTS_2ND_CHANCE','PTS_FB','PTS_PAINT','REB_CHANCES','RAFGM','RAFGA','PFGM','PFGA','MRFGM','MRFGA','LCFG3M','LCFG3A','RCFG3M','RCFG3A','CFG3M','CFG3A','ABFG3M','ABFG3A','ISO_PTS','PRBH_PTS','PRRM_PTS','SU_PTS','DRIVES','DRIVE_PTS']:
    
    df[n] = 36*(df[n]/df.MIN)
    
# final cleaning up

df['PLAYER_WEIGHT'] = pd.to_numeric(df['PLAYER_WEIGHT'])
df['PER'] = pd.to_numeric(df['PER'])
df['OWS'] = pd.to_numeric(df['OWS'])
df['WS'] = pd.to_numeric(df['WS'])
df['WS/48'] = pd.to_numeric(df['WS/48'])
df['OBPM'] = pd.to_numeric(df['OBPM'])
df['BPM'] = pd.to_numeric(df['DBPM'])
df['DBPM'] = pd.to_numeric(df['BPM'])
df['VORP'] = pd.to_numeric(df['VORP'])
df['AST_RATIO'].replace(np.inf,df.AST,inplace=True)

df.fillna(0, inplace=True)
