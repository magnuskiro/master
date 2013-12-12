master
======

My master Thesis and the work around it.

### Working Title (Temporary)
Tweets correlation between sentiment and opinion, associated with the financial impact of tweets.

### Working Description (Temporary)
The project deals with the correlations between the tweets and the stock value.
The student will start with finding the stock relevant tweets and pre process
them. 

It has been argued that people talk about a company especially when there are
some events that may negatively effect the stock price of the company. The
student will investigate this hypothesis and also analyse the content of tweets
with respect to the sentiment and opinion.

### Latest Release
To be announced.
Estimated 1. Jan 2014. 

### Schedule / Dates
* nov 1: 25 pages. (not reached)
* dec 1: 30 pages, basic classification of tweets, partially working system.
* jan 10: 40 pages, working beta version of system.  
* feb 1: 45 pages, reworked thesis. 
* mar 1: 55 pages, just minor code changes creating results in march. 
* apr 1: 65 pages, all code and results complete. 
* may 1: 70 pages, only finishing touches and proof reading remain.  
* jun 1: finished. 

### Finding relevant articles: 
* http://aclweb.org/anthology
* scholar.google.com 
* http://www.bibsys.no/ 
* http://search.proquest.com
* http://papers.ssrn.com/sol3/DisplayAbstractSearch.cfm
* http://www.sciencedirect.com/

### Buss words
* Twitter 
* Finance
* Trading
* Social media
* Sentiment analysis
* Moving average
* NLP
* Classification 
* Trend detection/analysis

### Quotes
* The trend is your friend

### Forgotten themes
* Event detection of epidemics on twitter. 
* In finance, change in tweet volume indicates a change in price direction. 

### TODO / Stuff to remember 
* Deploying: http://flask.pocoo.org/docs/quickstart/#deploying-to-a-web-server

Meeting Notes 
======

### meeting: date. 
* What has been done?
* What todo the next week.  

## 12.12
Initiate skype meeting. 

## 05.12
#### What has been done?
* datamining part. now has a dataset of 10k tweets. 
* RQ has been updated. 

#### next week
* get a working prototype
* create a scoring system for the twitter trend. 
* search for an academic dataset. 
* data sift?
* create a search corpus. (list of finance words and Hashtags that my dataset can be made of)

## 21.11
User guide.
* config filer. 
* Får ikke lagret filene. 


RQ1: can extract knowledge from tweets to fint the sentiment. 
Spåklig utfordrende. Kveliteter og finurligheter av å finne sentiment til en
tweet. 

RQ2: alle setningen til RQ1. 
RQ2: skrive noe nytt.
RQ2: kan vi bygge en trend kurve fra tweet data. 

RQ3: technical analysis. 

* Tweets example, financial tweets.

* Followers, from a tweet. 
* Sjekk hvilke metadata folk har brukt tidligere. 
* retweet. 

* Resyme over hvilke metadata som fins i en tweet --> inn i state of the art og
  data. 
 
* twitter api. Hvordan man fonner tweets.

* Language overview. Of twitter. 

* korte dokumenter er vanskelige å klassifisere.

* Til Arvid: Sende lure linker til arvid om flask og webutvikling.

* kode dictionary og tweet set. 
* Hvilke ord er det som ikke er klassifisert fra før av. 

* tagging i eksmpler. Hashtag, andre tags. 

* Eksemplene skal være knallgode. 

* $STO, tweet state of the art. 

* Hva kan jeg bytte ut aksje prisen med fra twitter for å aggregere en trend.  

* finne mer ut av hva andre gjør. 

* Skype møte. 

* Sender i løpet av tirsdag. 
* Avtaler skype møte da. 

## 12.11
Snakke med Han i mailen om hva han holder på med. Og hvilket fokus han har. 

Trend in Trade volume 

"twitter can be used to predict trends" statement, or question?

What is trend? Price or volume? 
Tweet volume. 

Metadata i twitter, hvor mange tweets produced today etc.
Twitter volume, in relation to market volume?
Change in volume is change in market volume. 

RQ 1,2 is the same.
How can we decide the sentiment of a tweet. 

RQ: Alignment mellom tweet sentiment and stock market change. 

Tweet sentiment --> market trend. 

Se på sammenheng først, og prediction muligens senere. 

Get metadata from twitter? 

NLP: don't do dependency parsing. 
NLP: part of speech. Spørre Gleb om pos, hands on. 

Finne ut hvordan man uttrykker sentiment. 
Hvordan sier jeg min mening? 
ModalWeak/Strong 
Hvorfor er disse sepparate. 

Tukle med sentiment verdien til et gitt ord. 

Man bruker innholdet i ordbøkene på forskjellige måter. 
Negation. 

Gå over artikler og se på NLP prosesseringen "ikke bra" "less good" "more good"
etc. 

Credibility, litt vekting muligens? 

Do some experiments, get some results. 

* tweet sentiment
* tweet sentiment relation to trade.  
* trend. 

Sende oversikt over hva som er gjort siden sist på epost.

Møtereferat.  

## 05.11
No meeting took place. Sending work to supervisor on the 7. 
## 29.10
#### Done?
State of the art is about done. 
Nothing else is done since last time.
#### Until next time: 
Continue to work on the thesis. 
Mode code.  
#### Feedback
* Programmere, bytte på med lesing og koding. 
* R språk ?
* bruke dictionaries, ordbøker i mail. pos/neg

* trenger pos/neg ordbok. 
* Finans relaterte tweets,
* koble dem sammen

* Lese en artikkel hver dag.

* Begynnelsen av nytt fagområde. 
* Litt stykkevis og delt. 

* Coding / system specification as chapter 6. 
* reduserer egen innsats. 
* min approach. 
* Work on this, I know this part well. 

* Skille artikler på machin learnin og statistisk.  

* Naturlig språk / klassifisering. 
*  -||- / kvantitative metoder. 

* statistikk / naturlig språk. 
* Se på artikler igjen og se på forrige punkt. 

* pos => nlp. 

* lerning / not learning

* NLP på bearbeidingen. 

* Gramar, sentences and such. ENGLISH!!

* Clustering på innhold. Finance... 

* læring, ja/nei
* input til læringen? 
* statistisk / nlp. 

* Innholdet, hvor my av en tweet blir faktisk brukt. 

* Viktig å vite hvilken bagasje vi har fra før av. 

* Settning hvor et ord forekommer. 
* explisitt om meta-features. 

* Waht do i get out of each article. 
* lessons learned. 
* background in the articles, IMPORTANT!

* kode med statistikken. 
* Lese mer om sentiment, litt mer i bredden. 

* Noder og kanter i grafene. 

* Mer forståelse, gir bedre resultat. 

* dependency path representation. 

* Jobbe med thesen og koden parallellt. 

## 24.10
#### Since last time 
Restructured the thesis, compliant with NTNU template. 
Course about how to write academic English (Monday).
Started coding. Structure and basic framework use.  
Workstation setup. 
Found article about PoS-tagging of tweets, gate plugin.
Started a journal to keep track of progress on a daily basis. 

#### Problems 
Procrastination and disturbances --> more discipline. 
Not found a word list. Considering to grab one from Gate or something(reverse
engineering). 
To little focus on articles and research. 

#### The next week
Write on the data section. 
Rework the state of the art section. 
Start coding the sentiment classification.  
More focus on research and thesis. 

#### Input from supervisor: 
Send pdf file each wednesday. 
Separate with on lang code / country code. 
Double negation? 
Bi grams. 
Important to write about the stuff I have thought about. 
I focus on this and that. 
Finish state of the art by monday 1800.   



## 15.10
Basic update. Not much done. 
A bit of twitter integration. 
Research questions update. 
Some on state of the art. 

Focusing on the twitter api and classification with positive/negative words
until next time. 
Also working on the state of the art part. 
Until next time: Update the thesis to comply with the AI-masters/ntnu thesis example. 

## 03.10
* not article, Thesis! 
* research question: ... in the stock market. both questions. How does these
  trends compare to the technical analysis in the stock market. 
* navn, innhold, sitering. 
* 4.'sentiment analysis'
* 4.1 remove. 
* 4.2 The use of sentiment for me. 
* 6. Results and discussion. 
* 3. heading, ==> Data retrieval, 
* 4 prototyping and such tings also. 
* 1.1.1, specify the questions 
* 4 = experiments. 
* 1.1.1 which parts of twitter are most useful. 
* 1.1.1 which parts of the twitter sphere results in the best exoeriment
  results. Which twitter sources are most suitable for trend prediction in the
stock market. 
* 1.1.1 look at what sort of credibility level has to be attained to certify
  the quality of the trend prediction. 
* what a stock is is useless information. 
* Physical presentation of twitter and usage. Searches and queries
* om twitter and typical twitter messages. 
* technical analysis 
* experiment with the time frame for the trend. 
* What experiments can and should I do. 
* state of the art, in sentiment, methods used and tagging of words, labeling. 
* 1.1.1 use sentiment analysis on tweets. 
* positive negative terms. <-- get it into the research questions.>
:
* Literature review to get word lists. 
* stop word list for finance. 
* Positive and negative word list. 


#### Begynne artikkellesing med spm. 
* Hvordan tweets blir brukt i den spesifikke artikkelen. 
* event detection. Omhandler tweeten merging? 
* Hva brukte de tweets til? 
* Hva gir denne artikkelen svar på? 

#### Overordna spm.
* Skaffe oversikt over hva tweets blir brukt til i hvilke artikler. 
* Hva er dagens situasjon. Dette er metoden. 
* Kan vi bryte algoritmetrading/speedtradingen. 
* Kan tweets brukes til trendanalyse?
* Hvordan tweets kan benyttes til å gjette trender. 
* Kan man bruke sentiment analyse med twitter til å bestemme en trend. 

#### State of the art 
- hva er twitter
- Hva er sentiment analyse.
- hvordan bruke sentiment analyse i trading. 
- generelt om øko og trading. 
- trending

####
Tanke, future work: Kan talldata brukes? 
Lese kjapt gjennom artikler som er like. 

Til neste gang: Skrive state of the art. 

