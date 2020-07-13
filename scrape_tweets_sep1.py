# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:38:55 2020

@author: Lennart
"""


from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os

path = 'C:\\Users\\Lennart\\Documents\\GitHub\\CausalAnalysis_TermPaper\\'

lang = "de"

tweets_hs5 = query_tweets("neger OR islamisierung OR multikulti OR nafris OR asyltouristen OR merkel-gaeste OR illegale OR wohlstandsfluechtlinge OR zudringlinge OR musel OR salafistenschwestern OR kampfmuslimas OR burka-frauen OR kloneger OR buntland OR dummstaat OR plemplemland OR schandland OR bundeskloake",
                         begindate = dt.date(2015, 9, 2), enddate = dt.date(2015, 9, 16), lang = lang)

df_hs5 = pd.DataFrame(t.__dict__ for t in tweets_hs5)

df_hs5.to_csv(os.path.join(path,r'Scrape_hs5_sep_de.csv'), index = False, encoding = 'utf-8')
