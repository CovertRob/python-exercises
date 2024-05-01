


#Exercises from Functions section

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)
        
#----------------------------------------------------------------------------#
#String exercises
phrase = "These aren't the droids you're looking for."

print(len(phrase))

phrase2 = 'confetti floating everywhere'
print(phrase2.upper())
print(phrase2)

name = 'Roger'
name2 = 'DAVE'
print(name.casefold() == 'RoGeR'.casefold())
print(name.casefold() == name2.casefold())

line = """A pirate I was meant to be!
Trim the sails and roam the sea!"""

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)

def is_empty(input):
    return not input

print(is_empty('mars'))

def is_empty_or_blank(input):
    return not input or input.isspace()

print(is_empty_or_blank(''))

phrase3 = 'launch school tech & talk'

print(phrase3.title())

def starts_with(string, prefix):
    return string.startswith(prefix)

def count_substrings(string, substring):
    return string.count(substring)

scores = [96, 47, 113, 89, 100, 102]

high_scores = [score for score in scores if score >= 100]