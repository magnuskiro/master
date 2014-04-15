

neg=`cat tweets_classified_manually | ack-grep ^-1, | wc -l`
pos=`cat tweets_classified_manually | ack-grep ^1, | wc -l`
neu=`cat tweets_classified_manually | ack-grep ^0, | wc -l`
err=`cat tweets_classified_manually | grep ^[\^-01] | wc -l`
let sum=$pos+$neg
let tot=$pos+$neg+$neu

echo "Manual classification: tweets_classified_manually"
echo "(pos, neg, neu)" 
echo "($pos, $neg, $neu)" 
echo "sum pos+neg: $sum"
echo "total: $tot" 

