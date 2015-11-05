
import re

def vowel_2_index( str ):
    for m in re.finditer('[a|e|i|o|u]+', str, re.IGNORECASE):
        print(str[m.start()])
        print(m.start()+1)
    result = re.sub('[a|e|i|o|u]+', m.start()+1, str)
    print(result)

vowel_2_index('This is my String.')
vowel_2_index('Codewars is the best site!')
