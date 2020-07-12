# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:56:35 2020

@author: Lennart
"""

from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os

path = 'C:\\Users\\Lennart\\Documents\\GitHub\\CausalAnalysis_TermPaper\\'

lang = "german"


tweets_hs9 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 11, 25), enddate = dt.date(2015, 12, 9), lang = lang)


df_hs9 = pd.DataFrame(t.__dict__ for t in tweets_hs9)

df_hs9.to_csv(os.path.join(path,r'Scrape_hs9_dec_n.csv'), index = False, encoding = 'utf-8')