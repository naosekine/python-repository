from termcolor import colored

def separate(func):
    separate = '#####################################################'
    def wrapper(*args, **kwargs):
        print(colored(separate, 'green'))
        result = func(*args, **kwargs)
        print(colored(separate, 'green'))
        return result
    return wrapper

@separate
def talk(word):
    print(colored(word, 'green'))
