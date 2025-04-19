import base64
from codecs import ignore_errors
from mimetypes import init
from ntpath import join
import math
import time
import random

def hello(name_n: str):
    name = input('What is your name? ')
    print(f'Hello {name.lower()}')

    name_c = "cArLos"
    print('name_c is of type ', type(name_c))
    if isinstance(name_c, str):
        print(f"Hello papa {name_c.title()}")
    else:
        print("Not an string!")

    print(f"\nAlso hello {name_n.upper()}")

    name_yu = 'yuyis'
    last_name = "Q."
    last_name_ch = 'Zhang'
    print(name_yu + " " + last_name)
    print(name_yu, last_name_ch, "Number of y's {0}".format(name_yu.count('y')))

def manually_order(lista):
    #lista = [1, 2, 3, 4, 5, 6]
    print('\nGiven order: {0}, {1}, {2}, {3}, {4}, {5}'.format(*lista))
    print('\nInverse order: {5}, {4}, {3}, {2}, {1}, {0}'.format(*lista))

def strip_replace_union(message: str):
    # Remove leading and trailing whitespces with STRIP
    phrase = " Hola Yu "
    print(f"\nMrs{phrase}"+"Q.")
    ######## STRIP #######
    stripped = phrase.strip() # stripping only the spaces before and after the word
    print(f"Mrs{stripped}"+"Q.")

    # Locating spaces
    print(f"\nFirst space in message located at: {message.find(' ')}")

    print("\n"+message)

    # Using str.replace to replace whitespaces with 
    ######## REPLACE #######
    replaced = message.replace(' ', '%')
    print(f"\n{replaced}")

    # Put together characters in a string
    ######## JOIN #######
    join_msg = "".join(message)
    print("\n" + join_msg)

    # METHOD 1: Strip all white spaces in message with REPLACE
    print("\n"+ message.replace(' ', ''))

    # REPLACING chars
    print("%".join(message))
    print(message.replace(" ", "%"))

    # Counting all spaces
    count = 0
    for character in message:
        if character == " ":
            count += 1
    print(f"\nNumber of total spaces is: {count}\n")

    # Separate chars in  msg
    lista = list(message) #-> List of chars
    print(lista)

    # Separate words in msg with SPLIT
    ######## SPLIT #######
    splitted = message.split() #-> List of words
    print(splitted)

    # METHOD 2: Putting togheter what was splited
    print("\n" + "".join(splitted))

def manipulate_str(msg: str):
    print("\n" +  msg.swapcase())
    print("\n" +  msg.casefold())
    print("\n" +  msg.expandtabs())
    txt = "My name is Ståle"
    print(txt.encode())
    print(msg.encode(encoding="ascii", errors="ignore"))

    if msg.startswith('T'):
        print('\nMessage starts starts with T')
    elif msg.startswith('A'):
        print('\nMessage starts starts with A')
    else:
        pass

    if msg.endswith('w'):
        print('\nMessage ends with w')
    elif msg.endswith('.'):
        print('\nMessage ends with .')
    else:
        pass

    print("the lowest index letter 'm' is at : ", msg.index('m'))
    print("the highest letter 'm' is at : ", msg.rindex('m'))
    try:
        print("the index letter 'x' is at : ", msg.index('x')) # if not found it will give an exception
    except ValueError as err:
        print(err)
    print("the lowest letter m is found at: ", msg.find('m'))
    print("the highest letter m is found at: ", msg.rfind('m'))
    print("the lowest letter m is found at: ", msg.find('x')) # if not fournd it will return -1 
    msg_list = msg.split()
    print(msg_list)
    print("who is located at: " + str(msg_list.index('who')))

def reverse_name(name):
    listed_name = list(name)
    lista = []
    for i in range(len(name) - 1, -1, -1):
        lista.append(listed_name[i])
    print("Original name: {Oname}".format(Oname=name))
    print("Reversed name: {Rname}".format(Rname="".join(lista)))

def splitting_joining(text):
    list_text = list(text)
    print(list_text)
    text_months="January,February,March,April,May,June,July,August,September,October,November,December"
    print("".join(list_text))
    to_list = text_months.split(",")
    print(to_list)
    print(", ".join(to_list))
    print(text.upper())
    print(text.capitalize())

def in_in_not(message):
    print("Message : {0}".format(message))
    print(f"Message contains 'never'? {'never' in message}")
    print(f"Message contains 'yuya'? {'yuya' in message}")
    print(f"Message doesn't contain 'carlangas'? {'carlangas' not in message}")

def find_word_index(text, word):
    if word in text:
        found = text.find(word)
    else:
        import logging
        log = logging.getLogger()
        log.warn('Word not available in text.')
    print(f"'{word}' was found in '{text}' at index = {found}")

def find_all_words_index(text, word):
    text = text.strip(".")
    to_list = text.split(" ")
    print(f"To list: {to_list}")
    if word in text:
        # for i in range(0, len(to_list) - 1):
        #     if to_list[i] 
        #         print(f"Joined: {new_text}")
        print(f"'{word}' found at index= {text.index(word)}")
    else:
        import logging
        log = logging.getLogger()
        log.warn("word not found in text")

def find_chars_index(string, character):
    for i in range(0, len(string)-1):
        if string.startswith(character, i):
            print(f"Letter '{character}' located at index= {i}")

def is_anagram(string1, string2):
    print(f"Checking if '{string1}' and '{string2}' are anagrams:")
    if sorted(string1) == sorted(string2):
        return True

def reverse_string_1(string):
    return string[::-1]

def reverse_string_2(string):
    list_string = list(string)
    lista = []
    for i in range(len(list_string) - 1, -1, -1):
        lista.append(list_string[i])
    return "".join(lista)

# def reverse_string_3(string):
#     return reverse(string)

def type_var():
    s = "hello"
    slist = list(s)
    num = 123
    print("***Type of vars***")
    if type(s) == str:
        print(type(s))
    else:
        print("Not a string")
    if isinstance(num, int):
        print(type(num))
    else:
        print("Not a num")
    if isinstance(slist, list):
        print(type(slist))
    else:
        print("Not a list")

def remove_vowels(string:str):
    lista = list(string)
    new_lista = []
    vowels = ["a", "e", "i", "o", "u"]
    for character in lista:
        if character not in vowels:
            new_lista.append(character)
    return "".join(new_lista)

def reverse_string(string:str):
    return string[::-1]

def reverse_list(lista:list):
    s = "".join(lista)
    s = s[::-1]
    # return s.split()
    return list(s)

def reverse_bulk_simplified(s, bulk):
    rs = ""
    for i in range(0, len(s) - 1, bulk):
        rs = rs + s[i:i+bulk][::-1]
    return rs

def rotate_string_left(s, n):
    return s[n:] + s[:n]

def rotate_string_right(s, n):
    return s[-n:] + s[:-n]

def urify(s):
    s = s.strip()
    return s.replace(" ", "%20")

def list_vs_for(s):
    print(s)
    print(list(s))
    print([s[i] for i in range(len(s))])
    print([i for i in range(6)])

def for_else(s):
    for i in range(len(s) - 1):
        print(s[i+1], end="")
    else:
        print("\nfinilized!")

def get_substrings(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return lista

def validate_palindrome(s):
    s = s.strip()
    onlyalpha_list = []
    # if "," in s:
    #     s = s.replace(",", "")
    # if ":" in s:
    #     s = s.replace(":", "")
    # if " " in s:
    #     s = s.replace(" ", "")
    i = 0
    end = len(s) - 1
    while i <= end:
        if s[i].isalnum() == True:
            onlyalpha_list.append(s[i])
        i += 1
    s = "".join(onlyalpha_list)
    if s[:].lower() == s[::-1].lower():
        return True
    else:
        return False

def find_substrings(string, substring):
    counter = 0
    for i in range(len(string)):
        if string[i] == substring[0]:
            if string[i:i+len(substring)] == substring:
                print(string[i:i+len(substring)])
                counter += 1
    return counter

def reverse_chunk(s, chunk):
    lista = []
    for i in range(0, len(s), chunk):
        lista.append(s[i:i+chunk][::-1])
    return "".join(lista)

def parenthesis_balancing(s):
    p = list(s)
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    for i in range(len(p)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            if len(stack) > 0 and op[location] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"

def isanagram(s1, s2):
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            return True
        else:
            return False
    else:
        print(f"\n{s1} and {s2} length must be the same")

def fizzbuzz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i != 0:
            print("Fizz")
        elif i % 5 == 0 and i != 0:
            print("Buzz")
        else:
            print(i)


# Driver function
if __name__ == "__main__":
    start_time = time.time()
    lista = [1, 2, 3, 4, 5, 6]
    manually_order(lista)
    message = "Adding Whitespace to Strings with Tabs or Newlines."
    strip_replace_union(message)
    msg = "A person who never made a mistake never tried anything new."
    manipulate_str(msg)
    name = "Kat Q."
    reverse_name(name)
    text = "K is very cover"
    splitting_joining(text)
    in_in_not(msg)
    find_word_index(msg, 'who')
    find_all_words_index(msg, 'who')
    string = "abracadabra!"
    find_chars_index(string, 'a')
    str1 = "cinema"
    str2 = "iceman"
    anagram = is_anagram(str1, str2)
    print(anagram)
    s = "Be hungry, be foolish"
    print(reverse_string_1(s))
    print(reverse_string_2(s))
    type_var()

    s = "Hola Car"
    print(remove_vowels(s))
    print(reverse_string(s))

    list_num = ["1", "2", "3", "4", "5"]
    list_sentence = ["Hello Scratch Cat"]
    print(reverse_list(list_num))

    s="abcdefgh"
    print(reverse_bulk_simplified(s, 3))

    s = "Carlos"
    print(rotate_string_left(s, 1))
    print(rotate_string_right(s, 1))

    s = " Mr. John Smith "
    print(f"{s} URIFY => {urify(s)}")

    s = "un hombre y una mujer"
    list_vs_for(s)

    s = "Python"
    for_else(s)

    s = "BANANA"
    print(s)
    print(get_substrings(s))

    end_time = time.time()
    print(f"\nElapsed time: {math.ceil(end_time - start_time)} seconds")

    s1 = "madam"
    print(f"Is {s1} a palindrome? : {validate_palindrome(s1)}")
    s2 = "testarrosa"
    print(f"Is {s2} a palindrome? : {validate_palindrome(s2)}")
    s3 = "A man, a plan, a canal: Panama"
    print(f"Is {s3} a palindrome? : {validate_palindrome(s3)}")

    string = "TestCaseTestCase"
    substring = "CaseT"
    print("SUBSTRINGS:", find_substrings(string, substring))

    s = "abcdefghijk"
    print(reverse_chunk(s, 3))

    s = "{[()[]{}]}"
    print(s)
    print(parenthesis_balancing(s))

    s1 = "cinema"
    s2 = "iceman"
    print(isanagram(s1, s2))

    s = "Dogs are very super duper cute"
    list_num = [random.randint(10, 90) for i in range(10)]
    list_words = ['kiwi', 'banana', 'strawberry', 'orange', 'blueberry', 'mango', 'pear', 'apple', 'rasperry', 'melon',
                  'papaya', 'watermelon']
    tuple_months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December')
    set_colors = {'blue', 'red', 'green', 'purple', 'orange', 'black', 'white', 'grey', 'yellow', 'magenta', 'pink',
                  'brown'}
    print(f"list num -> tuple: {tuple(list_num)} and \n{tuple(list_words)}")
    print(f"list num -> set: {set(list_num)} and \n{set(list_words)}")
    print(f"tuple -> list: {list(tuple_months)}")
    print(f"tuple -> set: {set(tuple_months)}")
    print(f"set -> list: {list(set_colors)}")
    print(f"set -> tuple: {tuple(set_colors)}")
    print(f"counting the number 'e' in '{s}' is : {s.count('e')}")
    print(f"find first 'e' : {s.find('e')}")
    print(f"find last 'e' : {s.rfind('e')}")
    print(f"find first 'x' : {s.find('x')}")
    print(f"index first 'e' : {s.index('e')}")
    try:
        print(f"index first 'x' : {s.index('x')}")
    except ValueError:
        print(f"Warning: letter 'x' doesn't exist in '{s}'")

    if s.startswith('N'):
        print('hola')
    if s.endswith('e'):
        print('yuyis')
    s = "abcde"
    if s.isalpha():
        print('string is alpha')
    if s.isalnum():
        print('string is alphanumeric')
    if s.isnumeric() == False:
        print('string is not numeric')
    s= s + "12345" + "ababa"
    print(s)
    print(s.replace('a', 'A', 3)) #3 is the number of replacement ocurrences
    s2 = "Cute animals"
    print(s2.split(" ", 1))
    print(s2.rsplit(" ", 1))
    print(s2.partition(" "))
    print(s2.replace('chula', 'super duper chula'))
    print(fizzbuzz())
    
