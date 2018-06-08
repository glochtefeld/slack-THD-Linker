'''
Tests function for RE matching
'''

import re

tryStr = input('test str: ')
#pattern = re.compile('.*\d{4,7}')
if re.search(".*\d{4,7}",tryStr):
    print('Matched')
else:
    print('No match')
