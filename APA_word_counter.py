#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Pulkit Garg
# Script to count the number of words in an essay
# formatted in APA

import docx
import re
import sys

# checking if the citation is valid in terms of APA
def APA_in_text(word):
    if re.search("\((.+)\,(.+)\)", word):
        print(word)
        return True
    return False

# opening and parsing the doc file
def file_opener(fileName, ref_head):
    
    # variable to count the number of words
    words = 0
    
    # variable to check when does the citation occurs
    checkpoint = False
    
    # variable to count the number of words in a valid citation
    check_count = 0
    
    # variable to form a string containing the whole citation
    citation = ''
    
    doc = docx.Document(fileName)
    for line in doc.paragraphs:
        for word in line.text.split():
            words+=1
            
            # start of the in-text citation
            if word.find('(') != -1:
                checkpoint = True
            
            # end of the citation
            if word.find(')') != -1:
                checkpoint = False
                citation = citation + word
                if APA_in_text(citation):
                    check_count+=1
                citation = ''
            
            if checkpoint:
                citation = citation + word
                check_count+=1
                
            if word == ref_head:
                return words - check_count - 1
    return words

def main():
    fileName = ''
    ref_head = ''
    
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        ref_head = sys.argv[2]
    else: 
        fileName = \
            input('Please enter the name of the file in which you want to count the number of words '
                  )
        ref_head = input('Enter the heading for references in your document: ')
    
    print('APA In-Text Citations')    
    count = file_opener(fileName, ref_head)
    print('Number of words excluding the in-text citations and', ref_head, 'section: ', count)
    
if __name__ == '__main__':
    main()