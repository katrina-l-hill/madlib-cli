from ast import parse
from os.path import exists
import re

print('\n**Welcome to the madlibs_cli.\nThis process will be just as you think it will. You\'ll be prompted for some input to create a super awesome madlib (yep, like the kind you grew up with (lol)).\nOnce you\'ve run through the process, you\'ll be shown the full text of the madlib with your input.\nEnjoy!')

def read_template(file_path):
    if not exists(file_path):
        raise FileNotFoundError
    output = ''
    with open(file_path, 'r') as reader:
        for line in reader:
            output = output + ' ' + line.strip()
    return output.strip()

def parse_template(contents):
    parts_of_speech = ()
    matches = re.findall('{[a-zA-Z]*}', contents)
    for match in matches:
        parts_of_speech += (match[1:len(match) - 1],)
    clean_text = re.sub('{[a-zA-Z]*}', '{}', contents)
    return clean_text, parts_of_speech

def merge(message, words):
    for i in range(len(words)):
        word = words[i]
        message = re.sub('{}', word, message, 1)
    return message