#!/bin/sh

SPARK="/usr/local/bin/spark"
CURL="/usr/bin/curl"
AWK="/usr/bin/awk"
GREP="/usr/bin/grep"
TAIL="/usr/bin/tail"
HEAD="/usr/bin/head"
URL="https://rate.bot.com.tw/xrt/flcsv/0/L3M/JPY"

if [ ! -f "${SPARK}" ]; then
    echo "Install spark utility please."
    exit 1
fi

if [ ! -f "${CURL}" ]; then
    echo "Install curl please."
    exit 1
fi

${CURL} ${URL} --silent | ${GREP} JPY | ${AWK} -F ',' '{print $14*1000}' | ${HEAD} -n 60 | ${TAIL} -r | ${SPARK}
