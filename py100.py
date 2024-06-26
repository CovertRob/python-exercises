
# Use Python's string methods on the string 'Captain Ruby' to 
#create a string with the value 'Captain Python'.

def trans():
    word = 'Captain Ruby'
    word.replace('Ruby', 'Python')
    print(word)

def greet(iso):
    match iso:
        case 'en':
            print('Hi!')         # Hi!
        case 'fr':
            print('Salut!')         # Salut!
        case 'pt':
            print('Ola!')         # Olá!
#greet('en')

def extract_language(locale):
    print(locale[:2])

extract_language('en_US.UTF-8')




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

#print(len(phrase))

phrase2 = 'confetti floating everywhere'
#print(phrase2.upper())
#print(phrase2)

name = 'Roger'
name2 = 'DAVE'
#print(name.casefold() == 'RoGeR'.casefold())
#print(name.casefold() == name2.casefold())

line = """A pirate I was meant to be!
Trim the sails and roam the sea!"""

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

#print('x' in char_sequence)

def is_empty(input):
    return not input

#print(is_empty('mars'))

def is_empty_or_blank(input):
    return not input or input.isspace()

#print(is_empty_or_blank(''))

phrase3 = 'launch school tech & talk'

#print(phrase3.title())

def starts_with(string, prefix):
    return string.startswith(prefix)

def count_substrings(string, substring):
    return string.count(substring)

scores = [96, 47, 113, 89, 100, 102]

high_scores = [score for score in scores if score >= 100]

#List exercises -------------------------------------------
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
def list_iterator(place, list):
    for item in list:
        if item == place:
            return True
        
    return False

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

# def combiner(passcode_list):
#     combined_passcode = ''
#     for item in passcode_list:
#         combined_passcode = combined_passcode + item + '-'
#     return combined_passcode

# print(combiner(passcode))
        
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
joined_passcode = ''

for i in range(len(passcode)):
    if i > 0:
        joined_passcode += '-'

    joined_passcode += passcode[i]

#print(joined_passcode)  # 11-jZ5-hQ3f*-8!7g3-p3Fs

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for i in range(len(grocery_list)):
    print(grocery_list.pop(0))
    print(i)

#print(grocery_list)

#Dictionary exercises -----------------------------------------------


car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year']= 2003

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage')

vehicle = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },

}

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for num in numbers.values():
    half_numbers.append(num // 2)

#print(half_numbers)

half_numbers = [(value // 2) for value in numbers.values()]  ## using list comprehension


#print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for elem in numbers.items():
    print(f'A {elem[0]} number is {elem[1]}')
# or
for key, value in numbers.items():
    print(f"A {key} number is {value}.")



