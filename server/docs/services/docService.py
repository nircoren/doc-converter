# # -*- coding: utf-8 -*-
import re

from pdfminer.high_level import extract_text
import camelot.io as camelot
import uuid
# pdf_path = r"docs\hahira_test.pdf"

# def get_text_from_pdf(file_path):
#     return extract_text(file_path)

# text = get_text_from_pdf(pdf_path)
# text = text.replace('\n', ' ')
# text = text.split(' ')
# text = list(filter(lambda a: a != '', text))
# text = ' '.join(text)
# # print(text)    

import pdfplumber    

def reverse_hebrew_word(word: str) -> str:
    # A regular expression pattern to match Hebrew characters
    hebrew_pattern = r'[\u0590-\u05FF]+'
    
    # Function to reverse Hebrew words
    def reverse_match(match):
        return match.group(0)[::-1]

    # Use the re.sub method to replace Hebrew words with their reversed versions
    return re.sub(hebrew_pattern, reverse_match, word)

def reverse_hebrew_in_list(arr: list) -> list:
    return [format_word(word) for word in arr]


def get_all_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:

        # Extract all text from each page.
        text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text() is not None)

        # page = pdf.pages[0]
        # text = page.extract_text()

        text = text.replace(",", " ").replace(":", " ").replace(".", " ").replace("-", " ").replace("(", " ").replace(")", " ").replace("\"", " ")
        new_text = ''
        # Format text to hebrew
        for row in text.split('\n'):
            new_row = row.split()[::-1]
            new_text += ' '.join(new_row) + ' '
        words_list = new_text.split()
        # If it works without turning string to array, convert this function to get string and r
        formated_words_list = reverse_hebrew_in_list(words_list)
        formated_words_list = ' '.join(formated_words_list)
        return formated_words_list
        # print(get_display(' '.join(text)))   

  

def get_insertion_text(pdf_path, text_mappings):
    filepath = f'../../temp_{uuid.uuid4()}.pdf'
    pdf_path.save(filepath)
    tables = camelot.read_pdf(filepath,line_scale=100)
    texts_to_insert = []
    for text_map in text_mappings:
        extraction_indexes = text_map['extraction']['indexes']
        table = tables[extraction_indexes['table_index']].df
        text = table.iloc[extraction_indexes['row'],extraction_indexes['column']]
        text = format_word(text)
        texts_to_insert.append({ 'insertion': text_map['insertion'] , 'text': text })
    return texts_to_insert

# Format the received text
def format_word(text):
    isNumreic = False
    isHebrew = False
    for char in text:
        if char.isdigit():
            isNumreic = True
        elif char.isalpha():
            isHebrew = True

    if isNumreic and isHebrew:
        text = text
    elif isHebrew:
        text = text[::-1]

    return text

def get_text_to_insert(text_to_insert,pdf_text_list):
    accumilated_text = ''
    for word in pdf_text_list:
        accumilated_text += word + ' '
        res_text = ''
        if text_to_insert['extraction']['text_before'] in accumilated_text:
            skip_count = text_to_insert['extraction']['words_after_anchor'] + 1  if 'words_after_anchor' in text_to_insert['extraction'] else 1
            index = pdf_text_list.index(word) + skip_count
            res_text += pdf_text_list[index]
            index += 1
            if 'text_after' in text_to_insert['extraction']:
                while pdf_text_list[index] != text_to_insert['extraction']['text_after'] and index < len(pdf_text_list):
                    res_text +=  ' ' + pdf_text_list[index] 
                    index += 1
            return res_text
            
'''
1. devide to rows. row before includes, current row includes, row after includes
2. make array with chronological order of words. then i can say word before, word after

'''

def find_words_between(long_text, insertions):
    results = []
    
    for item in insertions:
        extraction = item['extraction']

        is_checkbox = extraction.get('check', False)
        if is_checkbox:
            results.append({ 'insertion': item['insertion'] , 'text': None })
            continue

        text_before = extraction.get('text_before')
        text_after = extraction.get('text_after')
        skip_count = extraction.get('skip_count', 0)
        word_count =  extraction.get('word_count', 0)
        regex = extraction.get('regex')
        # If text_after exists, match until text_after, else match only one word
        if regex:
            pattern = regex
            # match = re.search(pattern1, long_text)
            # if match:
            #     res_text = match.group(1)
        elif word_count:
            pattern = re.escape(text_before) + (r'(?:\s+\w+)' * skip_count) + (r'\s+\w+' * word_count)
        elif text_after:
            pattern = re.escape(text_before) + (r'(?:\s+\w+)' * skip_count) + r'\s+(.+?)\s+' + re.escape(text_after)
        else:
            pattern = re.escape(text_before) + (r'(?:\s+\w+)' * skip_count) + r'\s+(\w+)'
        
        match = re.search(pattern, long_text)
        res_text = match.group(1) if match else None
        if res_text:
            results.append({ 'insertion': item['insertion'] , 'text': res_text })
        
        
    return results
            
# from pypdf import PdfReader

# pdf = PdfReader(pdf_path)
# page = pdf.pages[0]
# text = page.extract_text()
# print(text)
