#!/usr/bin/env python3

knight_info = {}

with open("../DATA/knights.txt") as KN:
    for line in KN:
        (name,title,color,quest,comment) = line[:-1].split(":")
        knight_info[name] = [title,color,quest,comment]
    
for name,info_list in knight_info.items():
    print("name:",name,"title:",info_list[0])
