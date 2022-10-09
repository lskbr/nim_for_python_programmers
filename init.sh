#!/bin/bash
# Extract strings from an md file and creates po file
#
# Usage:
# ./init.sh FILE LANG

FILE=${1:-Nim-for-Python-Programmers}
LANG=${2:-pt_br}

[ ! -d "locale/${LANG}/LC_MESSAGES/" ] && mkdir -p locale/${LANG}/LC_MESSAGES/
md2po ${FILE}md --save --po-filepath locale/${LANG}/LC_MESSAGES/${FILE}.po


