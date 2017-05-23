#!usr/bin/python
# coding: utf-8
import re
import collections
def wc(filename):
    with open(filename,'r') as f:
        tokens = f.read()
        #print tokens.strip().split(' ')
        word_count = collections.defaultdict(lambda: 0)
        #print "tokens = ", tokens
        #for token in tokens:
        #    data = re.findall(r'\w',token)
        #    print data
        # 非单词都替换为' '
        data = re.sub(r'[\W\d]',' ',tokens)
        #for c in  data:
        #    print c
        words = data.split(' ')
        print "words = ", words
        #print "words = ", words
        #print "data = ", data
        for w in words:
            word_count[w] += 1
        del word_count['']
        return word_count
if __name__ == '__main__':
    print wc("words.txt")
