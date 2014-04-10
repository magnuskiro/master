
echo "neg, pos, neu, error lines,"
cat tweets_classified_manually | ack-grep ^-1, | wc -l
cat tweets_classified_manually | ack-grep ^1, | wc -l
cat tweets_classified_manually | ack-grep ^0, | wc -l
cat tweets_classified_manually | grep ^[\^-01] | wc -l


