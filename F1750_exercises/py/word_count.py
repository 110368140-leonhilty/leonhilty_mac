
def word_count(filename):
    result={
        'Characters' : 0,
        'Word' : 0,
        'Unique words' : 0,
        'Lines' : 0
    }
    unique_words =set()
    with open(filename, 'r') as f :
        for line in f:
            words = line.split()
            result['Lines'] += 1
            result['Characters'] += len(line)
            result['Word'] += len(words)
            unique_words.update(words)
    for key, value in result.items():
        print(f'{key}:{value}')

word_count('F1750_exercises/py/data/text.txt')
    
