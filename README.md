# CausalAnalysis_TermPaper
This repo contains Stuff for the term paper of the course "Applied Causal Analysis" @University of Mannheim Spring 2020, the term paper is called:

## From Fiction to Reality: As Hate Speech Spread So Does Hate Crime? A Twitter Investigation

## Research Question
Since my adolescents I am interested on the impact of online social media on the real life society. So it is no surprise that I wrote my bachelor's thesis about echo chambers in political twitter networks in Germany. I also see mostly the same opinion on policy choices every day on my Instagram feed, until a few days ago a sparsely known acquaintance share a conspiracy theory video. At this time I realized that my Instagram feed is also a filter bubble or rather an echo chamber. So my origin idea was to investigate Twitter in respect of conspiracy theories during the corona virus, but this emphasize as very difficult. Additionally, I search for datasets  I could use for a causal analysis but the topics I got by this were, in my opinion, not very groundbreaking. So my decision went to the impact of online hate speech on real life crime. It turned out that this topic was examined rarely.  Based on this my research question should be: "Is there a causal effect of Twitter hate speech on real life hate crime during the refugee crises in Germany?"

## Literature Review
Since online social networks have developed their prominence in recent times the research of those is rarely as well. The focus is mainly on network analysis, only a few scientists investigate the online hate speech in social networks (see Chan et al. 2016; Awan & Zempi 2016; Hanzelka & Schmidt 2017; M�ller & Schwarz 2019a, 2019b; Ozalp et al. 2019). Chan and colleagues (2016) shows that the availability of broadband increases political motivated hate crime in the time period of 2001 until 2008 in the United States of America. But these crimes occurred in areas with higher levels of racism anyway. An evidence of the connection between online hate speech and real life political motivated hate crime is lacking. Awan and Zempi (2016) point out that there is an increased number of hate crime, offline and online, against Muslims after Islamic terrorist attacks in Paris and Tunisia in 2015, and in Woolwich, United Kingdom, in 2013. They also implicate that the borders between online and offline are unclear. That political motivated hate speech nearly always comes from the right-wing has shown Hanzelka and Schmidt (2017). They follow a more qualitative approach and only focused on the German anti Islam movement PEGIDA and Initiatives against Islam from the Czech Republic. A correlation between anti Islam Tweets and hate crime against Muslims in the US during the presidential election campaign of Donald Trump was found by M�ller and Schwarz (2019a) as well as a causal effect of online hate speech on Facebook predicts real life crime against refugees in Germany during the refugee crisis (2019b). The latter is the most related study to my research topic. However, their focus was on Facebook and not on Twitter as well as only post from the right-wing party "Alternative f�r Deutschland" (AfD, English: Alternative for Germany) and not a sample of hate comments of all German users. 

## Theory
The theory of homophily and echo chambers states that people with similarity characteristics like sociodemographic, intrapersonal, moral concept, behavioral or similar (McPherson 2001), come together more often. This provides homogenous social networks and can be applied on online social networks as well (Kersting & Mehl 2018).  I will focus on the political homophily of the right-wing. This homophily can result in an echo chamber. Metaphorically speaking, an echo chamber describes a (filter-) bubble in which only one's own view of the world holds (Rokeach 1960, Jamieson & Cappella 2008). Other views cannot hold and will be declared as wrong as well as the own view of the world is overestimated and overrated. Therefore, I imply that if one's is in an online echo chamber these views become more acute, and then eventually they leave the anonymous space of the Internet and become real life actions. Furthermore, is there a salience event, terrorist attack by a foreigner or new law enforcement for example, the event is more discussed by the news as well as in the Internet. So there is a higher discussion during salient events and as a result of this the following hypotheses are proposed:
H1: If there is no salient event the lower are the hate speeches on Twitter.
H2: The lower the online hate speeches the lower the real life hate crimes.

## Data
To test the hypotheses I will scrape German Tweets with certain hashtags  in the period of 2015 until 2017 and compare them with anti-refugee incidents. Unfortunately, the German government or the German federal criminal police office (Bundeskriminalamt, BKA) do not provide any public data of political motivated crime like the Uniform Crime Report (UCR) in the US, only some annual report as a PDF and news account (Bundeskriminalamt 2020). So I got the data of the anti-refugee incidents from M�ller and Schwarz (2019b). These dataset includes 3,335 incidents of "anti-refugee graffiti, arson of refugee homes, assault, and incidents during protests in Germany between January 2015 and early 2017" (M�ller & Schwarz 2019b, p.8 f.).  Although this data were produced by the Amadeu Antonio Foundation and the NGO "Pro Asyl" it is a high quality dataset, because more than half of the data were reported by the federal government, other were reported by the police and national/local media outlets (M�ller & Schwarz 2019b). The measuring baseline of anti-refugee hate speech in the paper of M�ller and Schwarz (2019b) are the weekly posts of the AfD page which contains the word "Fl�chtling" (refugee). I will also use the weekly number of Tweets which contains hate speech, but in difference to them I will use only negative Tweets of all users. This can be realized by the selection of the hashtags and/or an applied sentiment analysis on these Tweets. 
So I will use a kind of natural experiment with data over time, will measure the hate speech and real life hate crime over the whole time and will use salient events as a treatment. If both, hate speech and hate crime, are increasing and the online hate speech before the real life hate crimes are increasing, then I will received an evidence of my theory. Based on this I use a kind of difference-in-differences method.
Of course I also have to control this analysis for some things, such as general racism level at municipality, population density, refugee density, foreigners' density, digital infrastructure and/or the political orientation in general at the municipalities.  

## Current Problems
Unfortunately, I got no permanently updated dataset of the government which contains every reported anti-refugee incident like the UCR or the Police Data Initiative (PDI) in the United States of America. It is also difficult to measure the control group because it is impossible to match hate speech users with real life hate crime. So the control group is almost non-existent. Moreover, the casual dynamic between online hate speech and real life hate crime is suppositious. There is no real evidence of online hate speech that is matched to precise real life hate crime. A theory that is really appropriate to the dynamic between online hate speech and real life hate crime is kind of also lacking. Additionally, I am not really happy with the homophily and echo chamber approach - this is more a network analysis approach. 

## References
Awan, I., & Zempi, I. (2016). The affinity between online and offline anti-Muslim hate crime: Dynamics and impacts. Aggression and violent behavior, 27, 1-8.
Bundeskriminalamt (2020). Polizeiliche Kriminalstatistik. Retrieved May 12, 2020, from https://www.bka.de/DE/AktuelleInformationen/StatistikenLagebilder/PolizeilicheKriminalstatistik/pks_node.html
Chan, J., Ghose, A., & Seamans, R. (2016). The internet and racial hate crime: Offline spillovers from online access. MIS Quarterly, 40(2), 381-403.
Hanzelka, J., & Schmidt, I. (2017). Dynamics of cyber hate in social media: A comparative analysis of anti-Muslim movements in the Czech Republic and Germany. International Journal of Cyber Criminology, 11(1), 143-160.
Jamieson, K. H., & Cappella, J. N. (2008). Echo chamber: Rush Limbaugh and the conservative media establishment. Oxford University Press.
Kersting, N., & Mehl, M. (2018). Echokammern im deutschen Bundestagswahlkampf 2017. Die ambivalente Rolle der Prominenz. ZParl Zeitschrift f�r Parlamentsfragen, 49(3), 586-602.
McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. Annual review of sociology, 27(1), 415-444.
M�ller, K., & Schwarz, C. (2019a). From hashtag to hate crime: Twitter and anti-minority sentiment. Available here: https://ssrn.com/abstract, 3149103.
M�ller, K., & Schwarz, C. (2019b). Fanning the flames of hate: Social media and hate crime. Available at SSRN 3082972.
Ozalp, S., Williams, M. L., Burnap, P., Liu, H., & Mostafa, M. (2019). Antisemitism on Twitter: Collective efficacy and the role of community organisations in challenging online hate speech. Social Media and Society.
Rokeach, M. (1960). The Open and Closed Mind. Basic Books New York.

