import os

def file_reader():
    text_array = []
    with open('file1.txt', 'r') as f:
        text_in_it = [txt for txt in f.readlines()]
        for text in text_in_it:
            text = text.strip()
            text_array.append(text)
        return text_array
def write_file():
    file1_reader = file_reader()
    if not os.path.exists('file2.txt'):
        with open('file2.txt', 'w') as f:
            pass 
        
    with open('file2.txt', 'w') as f2:
        for i in range(0, len(file1_reader), 3):
            f2.write(' '.join(file1_reader[i:i+3]) + '\n')

write_file()