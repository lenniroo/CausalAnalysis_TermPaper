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

begin_date = dt.date(2015, 1, 1)
end_date = dt.date(2015, 12, 31)

lang = "german"

tweets = query_tweets("flüchtlinge OR flüchtling OR asylant OR asylanten OR migrant Or migranten", 
                      begindate = begin_date, enddate = end_date, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv(os.path.join(path,r'Scrape3.csv'), index = False, encoding = 'utf-8')
