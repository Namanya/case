def check_duplicate_letters(sentence):
    string_list = []
    words = sentence.split()
    for word in words:
        for letter in word:
            if word.count(letter) > 1:
                string_list.append(letter)  
    if len(string_list) > 1:
        return True
    else: return False
  
# morse code
def monte_code(message):
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
    coded_letters = []               
    if message != "":
        for letter in message:
            coded_letters.append(codes[letter])
        return coded_letters
mess = "GIZ1A"
my_message = monte_code(mess) 
print(my_message)
    
                      



