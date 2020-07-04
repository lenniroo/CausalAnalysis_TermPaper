# -*- coding: utf-8 -*- 

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2019,11,1)
end_date = dt.date(2020,5,1)

limit = 10000
lang = "german"

tweets = query_tweets("flüchtling OR Flüchtling", begindate = begin_date, enddate = end_date, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv(r'\Users\Lennart\Documents\GitHub\CausalAnalysis_TermPaper\Scrape.csv', index = False)
