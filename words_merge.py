import re
import difflib
input_str = "a OR b c z d OR e f OR g OR h OR i"

def generate_sentences(input_string):
    tokens = re.split(r'\s+|OR', input_string)
    return tokens

def buckets():
    bucket1 = []
    bucket2 = []
    bucket3 = []
    separated = generate_sentences(input_str)
    for each_word in separated:
        if each_word != '':
            bucket1.append([each_letter for each_letter in each_word])
    for i in range(len(bucket1)):
        
        for j in range(i+1, len(bucket1)):
            diff = difflib.ndiff(bucket1[i], bucket1[j])
            diff_ratio = sum(1 for d in diff if d[0] != ' ') / max(len(bucket1[i]), len(bucket1[j]))
            if diff_ratio > 0.4:  # threshold for difference
                bucket2.append(''.join(bucket1[i])+ ' ' + ''.join(bucket1[j]))
                 
    return bucket2




output = buckets()
print(output)
