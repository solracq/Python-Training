'''
Decide the message

You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.

For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of: ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
mesage: "phob"
output: "cafe"
alph key
a  -  h
b  -  a
c  -  p
d  -  y
e  -  b
f  -  o
'''
def decode_message(key:str, message:str) -> str:
    # Vars
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dictionary = {}
    duplicates = []
    decoded_list = []
    count = 0

    # Build the subtitution table
    key_nospace = key.replace(" ", "")
    for i in range(len(key_nospace)):
        if key_nospace[i] in duplicates:
            continue
        dictionary[key_nospace[i]] = alphabet[count]
        duplicates.append(key_nospace[i])
        count += 1

    # Verifying that all chars in message exist in the subsitution table
    # for character in message:
    #     if character not in key:
    #         print("message out of range of substitution table")
    #         return -1
    # Decoding
    for i in range(len(message)):
        if message[i] == " ":
            decoded_list.append(" ")
        else:
            decoded_list.append(dictionary[message[i]])
    return "".join(decoded_list)
# Execution
key = "happy boy"
message = "phob"
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"
key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(f"Encoded message: {message2} \nDecoded message: {decode_message(key2, message2)}")