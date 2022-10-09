# Uses AWS Translate to automaticaly translate a po file (untranslated strings only)
#

import polib
import boto3
import sys

client = boto3.client('translate')

if len(sys.argv) > 2:
    LANG = sys.argv[2]
else:
    LANG = "pt_br"
if len(sys.argv) > 1:
    FILE = sys.argv[1]
else:
    FILE = f'locale/{LANG}/LC_MESSAGES/Nim-for-Python-Programmers2.po'

SOURCE_LANGUAGE = 'en'
if LANG == "pt_br":  # Brazilian portuguese code in AWS Translate is pt
    TARGET_LANGUAGE = 'pt'
else:
    TARGET_LANGUAGE = LANG

po = polib.pofile(FILE)
for entry in po.untranslated_entries():
    print(entry.msgid, entry.msgstr)
    response = client.translate_text(
        Text=entry.msgid,
        TerminologyNames=[
        ],
        SourceLanguageCode=SOURCE_LANGUAGE,
        TargetLanguageCode=TARGET_LANGUAGE,
        Settings={
            'Formality': 'FORMAL',
            'Profanity': 'MASK'
        }
    )
    entry.msgstr = response["TranslatedText"]
po.save()
