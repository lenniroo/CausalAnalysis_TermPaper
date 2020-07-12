# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:52:53 2020

@author: Lennart
"""


from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os

path = 'C:\\Users\\Lennart\\Documents\\GitHub\\CausalAnalysis_TermPaper\\'

lang = "german"

tweets_hs8 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR mutombo OR bongo OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 11, 6), enddate = dt.date(2015, 11, 20), lang = lang)

df_hs8 = pd.DataFrame(t.__dict__ for t in tweets_hs8)

df_hs8.to_csv(os.path.join(path,r'Scrape_hs8_nov_n.csv'), index = False, encoding = 'utf-8')
