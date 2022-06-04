import string

def gematria_dict():
    return {char: index
            for index ,char 
            in enumerate(string.ascii_lowercase,1)} #index從1 開始

print(gematria_dict())