# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:34:22 2020

@author: Lennart
"""


from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os

path = 'C:\\Users\\Lennart\\Documents\\GitHub\\CausalAnalysis_TermPaper\\'

lang = "de"

tweets_hs4 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 6, 19), enddate = dt.date(2015, 7, 3), lang = lang)


df_hs4 = pd.DataFrame(t.__dict__ for t in tweets_hs4)

df_hs4.to_csv(os.path.join(path,r'Scrape_hs4_jun_de.csv'), index = False, encoding = 'utf-8')
