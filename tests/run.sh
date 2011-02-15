#!/bin/bash

BLAMEGAME=`git log | head -n 3 | grep Author | sed -r -e "s/^.*[\ <]([^,:]+@[^>]+).*$/\1/g"`

if [ -d ./logs/ ]; then
	rm -rf logs
fi

mkdir logs

echo "N: Startting off tests"
echo "N: If there's an issue, we're yelling at: $BLAMEGAME"
echo "L: "

GOODNESS=0
FAILNESS=0

for x in `ls *tests*`; do
	LOG=`./$x 2>&1`
	ERRS=$?
	MODIFIER="null"

	if [ $ERRS -ne 0 ]; then
		echo -e "L: $x \t\t [ [31mfail[0m ]"
		let FAILNESS=$FAILNESS+1
		MODIFIER="failed"
	else
		echo -e "L: $x \t\t [  [34mok[0m  ]"
		let GOODNESS=$GOODNESS+1
		MODIFIER="success"
	fi

	echo "$LOG" > ./logs/$x-$MODIFIER.log.txt
done

echo "L: "
echo "B: $BLAMEGAME"
echo "P: $GOODNESS"
echo "F: $FAILNESS"

if [ $FAILNESS -gt 0 ]; then
	exit 1
else
	exit 0
fi
