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