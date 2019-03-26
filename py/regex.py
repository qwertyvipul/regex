import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-.555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "start a sentence and then bring it to an end"

### pattern to match
pattern = re.compile("abc")

### to find patters
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[5:8])