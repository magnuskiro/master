

neg=`cat tweets_classified_manually | ack-grep ^-1, | wc -l`
pos=`cat tweets_classified_manually | ack-grep ^1, | wc -l`
neu=`cat tweets_classified_manually | ack-grep ^0, | wc -l`
err=`cat tweets_classified_manually | grep ^[\^-01] | wc -l`
let sum=$pos+$neg
let tot=$pos+$neg+$neu

echo "neg: $neg" 
echo "pos: $pos" 
echo "neu: $neu" 
echo "sum pos+neg: $sum"
echo "total: $tot" 
echo "error lines: $err" 
