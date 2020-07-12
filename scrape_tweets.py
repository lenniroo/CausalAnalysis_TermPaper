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

tweets_hs1 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 1, 1), enddate = dt.date(2015, 1, 16), lang = lang)

tweets_hs2 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 2, 7), enddate = dt.date(2015, 2, 21), lang = lang)

tweets_hs3 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 6, 10), enddate = dt.date(2015, 6, 24), lang = lang)

tweets_hs4 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 6, 19), enddate = dt.date(2015, 7, 3), lang = lang)

tweets_hs5 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 9, 2), enddate = dt.date(2015, 9, 16), lang = lang)

tweets_hs6 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 9, 10), enddate = dt.date(2015, 9, 24), lang = lang)

tweets_hs7 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 9, 25), enddate = dt.date(2015, 10, 9), lang = lang)

tweets_hs8 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 11, 6), enddate = dt.date(2015, 11, 20), lang = lang)

tweets_hs9 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 11, 25), enddate = dt.date(2015, 12, 9), lang = lang)

# =============================================================================
# df_flu = pd.DataFrame(t.__dict__ for t in tweets_flu)
# df_asy = pd.DataFrame(t.__dict__ for t in tweets_asy)
# df_mi = pd.DataFrame(t.__dict__ for t in tweets_mi)
# =============================================================================
df_hs1 = pd.DataFrame(t.__dict__ for t in tweets_hs1)
df_hs2 = pd.DataFrame(t.__dict__ for t in tweets_hs2)
df_hs3 = pd.DataFrame(t.__dict__ for t in tweets_hs3)
df_hs4 = pd.DataFrame(t.__dict__ for t in tweets_hs4)
df_hs5 = pd.DataFrame(t.__dict__ for t in tweets_hs5)
df_hs6 = pd.DataFrame(t.__dict__ for t in tweets_hs6)
df_hs7 = pd.DataFrame(t.__dict__ for t in tweets_hs7)
df_hs8 = pd.DataFrame(t.__dict__ for t in tweets_hs8)
df_hs9 = pd.DataFrame(t.__dict__ for t in tweets_hs9)

# =============================================================================
# df_flu.to_csv(os.path.join(path,r'Scrape_f_jan.csv'), index = False, encoding = 'utf-8')
# df_asy.to_csv(os.path.join(path,r'Scrape_a_jan.csv'), index = False, encoding = 'utf-8')
# df_mi.to_csv(os.path.join(path,r'Scrape_m_jan.csv'), index = False, encoding = 'utf-8')
# =============================================================================
df_hs1.to_csv(os.path.join(path,r'Scrape_hs1_jan_n.csv'), index = False, encoding = 'utf-8')
df_hs2.to_csv(os.path.join(path,r'Scrape_hs2_feb_n.csv'), index = False, encoding = 'utf-8')
df_hs3.to_csv(os.path.join(path,r'Scrape_hs3_jun_n.csv'), index = False, encoding = 'utf-8')
df_hs4.to_csv(os.path.join(path,r'Scrape_hs4_jun_n.csv'), index = False, encoding = 'utf-8')
df_hs5.to_csv(os.path.join(path,r'Scrape_hs5_sep_n.csv'), index = False, encoding = 'utf-8')
df_hs6.to_csv(os.path.join(path,r'Scrape_hs6_sep_n.csv'), index = False, encoding = 'utf-8')
df_hs7.to_csv(os.path.join(path,r'Scrape_hs7_okt_n.csv'), index = False, encoding = 'utf-8')
df_hs8.to_csv(os.path.join(path,r'Scrape_hs8_nov_n.csv'), index = False, encoding = 'utf-8')
df_hs9.to_csv(os.path.join(path,r'Scrape_hs9_dec_n.csv'), index = False, encoding = 'utf-8')