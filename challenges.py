# checking repeating letters in sentences 
repeating_characters = []
def dup_check(sentence):
    words = sentence.split()
    for word in words:
        for letter in word:
            if word.count(letter)>1:
                repeating_characters.append(letter)
    return set(repeating_characters)


#morse code 

def morse_code(message):
    codes = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    monte_message = ''

    message = message.upper()
    for letter in message:
        if letter != '':
            monte_message += codes[letter]
        else:
            monte_message += ''
    return monte_message

# tellling that a month in a particular year has a friday 13th
from datetime import datetime

def find_date(m, y):
    d = datetime(y, m, 13)
    if d.weekday() == 4:
        return True
    else:
        return False
#m = int(input('Enter the month: '))
#y = int(input('enter they year (YYYY): ' ))

# finding a website by its ipaddress

import socket

def find_domain(website):

    try:
        address = socket.gethostbyaddr(website)[2]
    except socket.herror:
        address = 'not found'
    
    return address

#ip = input('enter website address: ')

# getting first_name: John, last_name: Doe, Index: 123
def parse_string(text):
    st = [s for s in text.split('0')]
    parsed_string = [x for x in st if x != '']
    
    first_name = parsed_string[0]
    last_name = parsed_string[1]
    index = parsed_string[2]

    result = {
        'first_name':first_name,
        'last_name': last_name,
        'index': index,
    }
    return result


parse = "John000Doe000123" 



def decimal_to_hex(string):
    our_list = []
    for letters in string:
        new_let = hex(ord(letters))[2:]
        our_list.append(new_let)

    return "".join(our_list) 
#out_come = decimal_to_hex('string')
#print(out_come)

#checking if a given string is a regex
import re 

def find_re(string):

    try:
        re.compile(string)
        return True

    except re.error:
        return False

#print(find_re('[\]')) should return False


