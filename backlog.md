The todo list for everything. 
## administrative
* send meeting summary.
* send thesis and summary of the work completed. 
* process documents: q, startnotat

## Thesis
* Correct from feedback. 
* Tweet examples should be high quality financial tweets. Examples should
contain hashtags and $STO stuffs, users. 
* Find out how many articles I have to read. 
* prototype: Write System specification
* Re review the read articles with machine learning vs statistical classification in mind. 
* Separate articles on statistical and NLP approaches. 
* Expand in the matter of meta data / features in a tweet. 
* define what a trend is. (price or volume, can compare with both)
* "twitter can be used to predict trends", statement or question?
* How do I express a sentiment? 
* Go over articles and look at NLP.
* References chapter should be numbered the same way as everything else. main.tex 
* Resume of what meta data exists in a tweet. Input to state of the art and data. 
* Read more articles.  
* RQ: Rewrite research questions. 

## Experiments / research
* Find out how much of a tweet is useful. 
* Explore trends in trade volume. 
* Explore the meta data we can get from twitter (not tweets).
* Is change in market volume related to change in tweet volume? Or the other way around?
* why are the modal weak and modal strong separate? 
* figure out how I express sentiment. 
* find out if IBM Watson has used some smart NLP algorithms or techniques fro classification of processing.  
* Can the topic detection of Watson be useful? 
* meta data: followers, retweets, etc. 
* Compile an overview of the language used in twitter. 
* Create 7 additional datasets
	* = 70k tweets
	* then run some statistics on the datasets.

## Code
* get the prototype to 
* Get two tweet dataset. 1k tweets. test and training. 
* Get meta data from twitter. 
* POS: part of speech. 
* Clustering of similar tweets.
* Clustering of tweets on users/location/language
* topic detection of tweets, Finance? 
* Take into consideration the different dictionaries. 
* Take negation into consideration in the classification. 
* Tweet credibility. (how much weight should credibility add?) 
	* Based on followers
	* http://people.fas.harvard.edu/~astorer/twitter/twitter.html
		* 4.4.3 Getting a user and all their friends and followers
	* The more the tweet is propagated info the social sphere the more weight it gets. 
	*  
* TwitterAPI/sample - how many tweets do we get?
	* https://dev.twitter.com/docs/api/1.1/get/statuses/sample
* Create a query set for acquiring data. 
	* a query string that has different words to broaden the dataset. 
	* 1000 chars. 
	* this OR maybe OR that
* Dictionary creation. Create from previously non classified words.
* look into the time perspectives. tweets from today has to correlate with financial data from today. 
* Trend aggregation: aggregate a trend based on classification data and other datapoints.  
	* this is a pint based system where each part gives points to an aggregated whole. 
	* this can then be compared to the financial data of the same day. 
