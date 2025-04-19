import random

def printdictionary(dictionary:dict):
    new_dict = {}
    for key, value in dictionary.items():
        print(f"{key}")
        for k, v in value.items():
            print(f"\t{k}\n\t\t{v}")

def sort_dict(dictionary:dict):
    for key, value in sorted(dictionary.items()):
        print(f"{key}:\n\t{value}")

def reverse_dict(dictionary:dict):
    for key, value in sorted(dictionary.items(), reverse=True):
        print(f"{key} \n\t{value}")

def sort_dict_values(dictionary: dict):
    for key, value in dictionary.items():
        print(f"{key}:")
        for k,v in sorted(value.items()):
            print(f"\n\t{k}: \n\t\t{v}")

def get_char_frequency(text:str):
    duplicate = []
    dictionary = {}
    for char in text:
        if char in duplicate:
            continue
        if char == " ":
            continue
        if char == ".":
            continue
        if char == ",":
            continue
        dictionary[char] = text.count(char)
        if text.count(char) >= 2:
            duplicate.append(char)
    return dictionary

def compare_dicts_simple(dict_a, dict_b):
    if len(dict_a) == len(dict_b):
        if (dict_a.keys() == dict_b.keys()):
            return f"{dict_a} and {dict_b} are EQUALS"

def compare_dicts(dict_a, dict_b):
    equals = {}
    if len(dict_a) == len(dict_b):
        for key_a, value_a in dict_a.items():
            for key_b, value_b in dict_b.items():
                if (key_a == key_b) and (value_a == value_b):
                    equals[key_a] = value_a
                    break
    if len(equals) == len(dict_a):
        return f"{dict_a} and {dict_b} are EQUALS on: \n{equals}"

if __name__ == "__main__":
    s = "The cats are very super duper cute"
    list_num = [random.randint(10, 90) for i in range(10)]
    list_words = ['kiwi', 'banana', 'strawberry', 'orange', 'blueberry', 'mango', 'pear', 'apple', 'rasperry', 'melon',
                  'papaya', 'watermelon']
    tuple_months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December')
    set_colors = {'blue', 'red', 'green', 'purple', 'orange', 'black', 'white', 'grey', 'yellow', 'magenta', 'pink',
                  'brown'}
    dictionary = {
                 "solrac": {
                            'name': 'CaloBeto',
                            'number': list_num[3],
                            'month': tuple_months[7],
                            'fruit': list_words[2],
                            'color': 'blue',
                            'likes': 'cars',
                            'hobbies': 'soccer',
                            'movies': 'Aladdin',
                            },
                "nquiroz": {
                            'name': 'Jessica P.',
                            'number': list_num[5],
                            'month': tuple_months[3],
                            'fruit': list_words[1],
                            'color': 'pink',
                            'likes': 'baby braqui',
                            'hobbies': 'singing',
                            'movies': 'princess movies',
                            },
                "yuyis": {
                         'name': 'Yu',
                         'number': list_num[random.randint(0,9)],
                         'month': tuple_months[9],
                         'fruit': list_words[5],
                         'color': 'purple',
                         'likes': 'shopping',
                         'hobbies': 'cooking',
                         'movies': 'As good as it gets',
                         },
                 }
    data_structure_dict = {'string': s,
                   'list_num': list_num,
                   'list_words': list_words,
                   'tuple': tuple_months,
                   'set': set_colors,
                   'dictionary': dictionary,
                   }
    print(dictionary)
    print(data_structure_dict)
    print(data_structure_dict['tuple'][7])
    print(data_structure_dict['dictionary']['yuyis']['movies'])
    printdictionary(dictionary)
    print(dictionary['yuyis']['name'])
    print(dictionary.keys())
    array = list(dictionary.values())
    print(array)
    print(array[0]['name'])
    dictionary['caloeduardo'] = {'name': 'Calitos'}
    dictionary['Camelit'] = {'name': 'Carmen Q'}
    printdictionary(dictionary)
    print(dictionary.get('caloeduardo'))
    print(dictionary['caloeduardo'])
    print(dictionary.popitem())
    dictionary.pop('caloeduardo')
    printdictionary(dictionary)
    del dictionary['yuyis']
    print("NOT SORTED")
    printdictionary(dictionary)
    print("SORTED")
    sort_dict(dictionary)
    print("REVERSED")
    reverse_dict(dictionary)
    print("SORTING KEY VALUES")
    sort_dict_values(dictionary)
    text= "hoolaa"
    print(get_char_frequency(text))
    text = "A list is a data structure that holds an ordered collection of items for example you can store a sequence of items in a list. This is easy to imagine if you can think of a shopping list where you have a list of items to buy, except that you probably have each item on a separate line in your shopping list whereas in Python you put commas in between them"
    print(get_char_frequency(text))

    dict_a = {"a": "hola",
              "b": 12345,
              "c": ['a', 'b', 'c'],
              }
    dict_b = dict_a.copy()
    print(compare_dicts(dict_a, dict_b))

    freq_dict = get_char_frequency(text)
    print(freq_dict)
    order_by_values = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    print(order_by_values)
    order_val2 = sorted(dictionary.items(), key=lambda x: x[1])
    print(order_val2)
