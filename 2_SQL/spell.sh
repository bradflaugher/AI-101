cat hamlet.txt |
tr A-Z a-z | # convert to lower case
tr -d ',.:;()?!' | # remove punctuation, ...
tr ' ' '\n' | # split words into lines
sort | # sort words of document
uniq | # eliminate duplicates
comm -23 - dictionary.txt # print lines found in input but not in dictionary