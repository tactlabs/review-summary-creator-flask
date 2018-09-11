#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Feb 27, 2018

Course work: 

@author: raja

Source:

Cite:
    Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''

# Import necessary modules
import json
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

EMOTION_METER_PAR = 3
WORD_LENGTH_PAR = 1
LINES_PAR = 2

def get_lines_in_array(filename):    
    with open(filename) as f:
        content = f.readlines()
        
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    
    #print(content)  
    return content

def is_invalid_content(content):
    
    # if only 3 words, ignore it
    if(len(content.split()) < WORD_LENGTH_PAR):
        return True
    
    return False

def sort_dict_reverse(d):
    s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    
    return s

sid = SentimentIntensityAnalyzer()

def get_sentiment(sentence):
        
    #print(sentence)

    ss = sid.polarity_scores(sentence)
    
    #print(type(ss['pos']))

    positive_meter = round((ss['pos'] * 10), 2) 
    negative_meter = round((ss['neg'] * 10), 2)
    
    '''
    for k in sorted(ss):
        #print(ss)
        print('{0}: {1}, '.format(k, ss[k]), end = '')
    '''
    
    #print('positive : {0}, negative : {1}'.format(positive_meter, negative_meter))
    
    #print()
    
    return positive_meter

def get_pros_summary(content):
    
    contents = content.splitlines()    
    print(contents)
    
    #content1 = [x.strip() for x in contents]
    
    #print(content1)  
    #return content
    
    pro_meter_dict = {}
    
    lines_counter= 0
    
    total_contents = len(contents)
    for x in range(total_contents):
        
        if(is_invalid_content(contents[x])):
            continue
        
        emotion_meter = get_sentiment(contents[x])
        
        # if meter is less than 5, ignore them
        if(emotion_meter < EMOTION_METER_PAR):
            continue
        
        pro_meter_dict[contents[x]] = emotion_meter
        
        print('---')
        #print(contents[x])        
        
    sorted = sort_dict_reverse(pro_meter_dict)    
    print(pro_meter_dict)
    
    content2 = ""
    for k, v in sorted:
        lines_counter = lines_counter + 1
        
        if(lines_counter > LINES_PAR):
            continue                

        print(k, v)
        
        content2 = k + "<br>"
    
    return content2
    
def main():    
    #print(data)
    
    contents = get_lines_in_array('pros.txt')
    
    #print(contents)
    
    pro_meter_dict = {}
    
    lines_counter= 0
    
    total_contents = len(contents)
    for x in range(total_contents):
        
        if(is_invalid_content(contents[x])):
            continue
        
        emotion_meter = get_sentiment(contents[x])
        
        # if meter is less than 5, ignore them
        if(emotion_meter < EMOTION_METER_PAR):
            continue
        
        pro_meter_dict[contents[x]] = emotion_meter
        
        #print('---')
        #print(contents[x])        
        
    sorted = sort_dict_reverse(pro_meter_dict)    
    #print(pro_meter_dict)
    
    for k, v in sorted:
        lines_counter = lines_counter + 1
        
        if(lines_counter > LINES_PAR):
            continue                

        print(k, v)
    
if __name__ == '__main__':
    main()