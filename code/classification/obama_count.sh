
neg=`cat obama_tweets_classified_manually | ack-grep ^-1, | wc -l`
pos=`cat obama_tweets_classified_manually | ack-grep ^1, | wc -l`
neu=`cat obama_tweets_classified_manually | ack-grep ^0, | wc -l`
let sum=$pos+$neg
let tot=$pos+$neg+$neu

echo "Manual classification: obama_tweets_classified_manually"
echo "(pos, neg, na)" 
echo "($pos, $neg, $neu)" 
