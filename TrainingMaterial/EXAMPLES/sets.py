#!/usr/bin/env python3

PYTHONS = {'Idle', 'Chapman', 'Cleese', 'Jones',
    'Gilliam', 'Palin'}

FAWLTY = frozenset({'Cleese', 'Cleveland'})

PYTHONS.add('Innes')

print("pythons", PYTHONS)
print("FAWLTY", FAWLTY)
print("pythons&FAWLTY", PYTHONS & FAWLTY)
print("pythons|FAWLTY", PYTHONS | FAWLTY)
print("pythons^FAWLTY", PYTHONS ^ FAWLTY)
print("pythons-FAWLTY", PYTHONS - FAWLTY)
