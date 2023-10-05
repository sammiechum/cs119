#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:04:37 2023

@author: sammiechum
"""

import re
import string
import sys
# import gzip
# import zipfile

# with zipfile.ZipFile('/Users/sammiechum/Downloads/prez_speeches.zip', 'r') as prez_zip:
#     # Loop through the files in the zip folder
#     for prez_gz in prez_zip.infolist():
#         speech_text = prez_zip.read(prez_gz.filename)

# print(speech_text)

library = []
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text

with open('/Users/sammiechum/Downloads//AFINN.txt', 'r') as file:
    for line in file:
        words = line.split()
        dict = {
            "word": words[0],
            "value": words[1] }
        library.append(dict)
        
for line in sys.stdin:
    cleaned = clean_text(line)
# cleaned = "i like you so much"

words = cleaned.split()
for word in words:
    for i in range (len(library)):
        if (library[i]["word"] == word):
            key = word
            value = library[i]["value"]
            print(key,"\t",value)



# J's sample mapper
# def main(argv):
#     line = sys.stdin.readline()
#     pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
#     try:
#         while line:
#             for word in pattern.findall(line):
#                 print ("LongValueSum:" + word.lower() + "\t" + "1")
#             line = sys.stdin.readline()
#     except EOFError as error:
#         return None

# if __name__ == "__main__":
#     main(sys.argv)