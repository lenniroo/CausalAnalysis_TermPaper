# -*- coding: utf-8 -*- 

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2015,1,1)
end_date = dt.date(2015,12,31)

limit = 10000
lang = "german"

tweets = query_tweets("Flüchtling", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

dr.to_csv(r'\Users\Lennart\Documents\GitHub\CausalAnalysis_TermPaper/\Scrape.csv', index = False)
