#!/bin/bash
# Use a po file to recreate the translated md file.
# Trues to use pandoc to render the translated file in html format on the current  folder
#
# Usage:
# ./gera.sh FILE LANG

FILE=${1:-Nim-for-Python-Programmers}
LANG=${2:-pt_br}

po2md ${FILE}.md -p locale/${LANG}/LC_MESSAGES/${FILE}.po --save locale/${LANG}/LC_MESSAGES/${FILE}.md
pandoc -f gfm locale/${LANG}/LC_MESSAGES/${FILE}.md -t html -o ${FILE}.html
