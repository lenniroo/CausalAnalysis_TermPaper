# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:10:32 2020

@author: Lennart
"""


from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os

path = 'C:\\Users\\Lennart\\Documents\\GitHub\\CausalAnalysis_TermPaper\\'

lang = "german"


# =============================================================================
# tweets_flu = query_tweets("flüchtlinge OR flüchtling", 
#                       begindate = begin_date, enddate = end_date, lang = lang)
# 
# tweets_asy = query_tweets("asylant OR asylanten", 
#                           begindate = begin_date, enddate = end_date, lang = lang)
# 
# tweets_mi = query_tweets("migrant OR migranten", 
#                          begindate = begin_date, enddate = end_date, lang = lang)
# =============================================================================

tweets_hs1 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 1, 1), enddate = dt.date(2015, 1, 16), lang = lang)

# =============================================================================
# df_flu = pd.DataFrame(t.__dict__ for t in tweets_flu)
# df_asy = pd.DataFrame(t.__dict__ for t in tweets_asy)
# df_mi = pd.DataFrame(t.__dict__ for t in tweets_mi)
# =============================================================================
df_hs1 = pd.DataFrame(t.__dict__ for t in tweets_hs1)


# =============================================================================
# df_flu.to_csv(os.path.join(path,r'Scrape_f_jan.csv'), index = False, encoding = 'utf-8')
# df_asy.to_csv(os.path.join(path,r'Scrape_a_jan.csv'), index = False, encoding = 'utf-8')
# df_mi.to_csv(os.path.join(path,r'Scrape_m_jan.csv'), index = False, encoding = 'utf-8')
# =============================================================================
df_hs1.to_csv(os.path.join(path,r'Scrape_hs1_jan_n.csv'), index = False, encoding = 'utf-8')

