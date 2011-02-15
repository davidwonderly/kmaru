#!/bin/bash

if [ "x$1" != "x--raw" ]; then
	TEXT=`./checkin.sh --raw`

	if [ $? -ne 0 ]; then
		echo "Failure. Sending out an email"
		echo "$TEXT" | /usr/sbin/sendmail -t -bm -v
	fi

	exit 0
fi

RUNSTAMP=`date "+%s"`

# L:
# L: kmaru-api-tests.py            [  ok  ]
# L: kmaru-lcia-tests.py           [  ok  ]
# L:
# B: paultag@ubuntu.com
# P: 2
# F: 0

# N - Note          ( crap )
# L - Log           ( save )
# B - who to Bug       "
# P - Pass             "
# F - Fail             "

RUNLOG=`./run.sh`
ERRORS=$?
SAVE="/whube/"
OUTPUTURL="http://logs.whube.com/"

SUBJECT="You have a test failure on kmaru"
DEVELADDR="paultag@gmail.com"
FROM="kmaru@whube.com"

MESSAGE="Dear Hacker,

You've recently checked code into the kmaru project.
Thank you so much for your work, but there's been a
core API test failure. Since you're the last one to
push code in, we expect people to always check tests
before sending merges in.

"

SIG="Thanks so much again,
The Whube Daemon (On behalf of the project)
"

if [ $ERRORS -ne 0 ]; then
	mkdir $SAVE/$RUNSTAMP
	mv ./logs/* $SAVE/$RUNSTAMP/
	WHOTOBUG=`echo "$RUNLOG" | \
		grep "B: " | \
		awk '{print $2}'`
	echo "Subject: $SUBJECT"
	echo "From: Kmaru Bitching Daemon <$FROM>"
	echo "To: John Q. Hacker <$WHOTOBUG>"
	echo "CC: Paul Tagliamonte <$DEVELADDR>"
	echo ""
	echo "$MESSAGE"
	echo "You can find the logs on the web[1]."
	echo ""
	echo "[1]: $OUTPUTURL$RUNSTAMP/"
	echo ""
	echo "$SIG"

	exit $ERRORS
fi
