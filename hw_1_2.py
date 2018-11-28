#  -*- coding: utf-8 -*-
# Question 2
# Design a phone book program. In this program, we can think of a phone book
# as a collection of friends, associates, family with their information such
# as a telephone number, email address, name and location.
# Design a simple program that gets the names from a random list like:
# names = [‘peter’, ‘mary’, ‘jane’]
# location = [‘stockholm’, ‘goteborg’, ‘helsingborg’]
# This is my answer:
#            def phoneBook(names, location):
#                return dict(zip(names, location))
# Please design an algorithm, that will create key value pairs
# of name and location at the end, use constructs like for-loops.
# (Optional) Extra credit: You can make your application return
# data or output that looks fancier:
# {
#                   ‘peter’: { ‘location’: ‘stockholm’},
#                   ‘mary’: { ‘location’: ‘goteborg’},
#                   ‘jane’: { ‘location’: ‘helsingborg’},
# }


# create phone book dictionary where
# key = name, value = dict with city, phone, email

def book(names, city, phone, email):
    return {n: {'city': c, 'phone': p, 'email': e + '@.gmail.com'}
            for n, c, p, e in zip(*[names, city, phone, email])}


# create the dict name, city, phone, email
names = [
    'Breanna',
    'Tamia',
    'Aylin',
    'Keyla',
    'Jayla',
    'Ashton',
    'Matteo',
    'Terrence',
    'Holden',
    'Rodney'
]

city = [

    'Rosario, Argentina',
    'Guadalajara, Mexico',
    'Cali, Colombia',
    'Chengdu, China',
    'Tehran, Iran',
    'Changsha, China',
    'Delhi, India',
    'Kathmandu, Nepal',
    "T'bilisi, Georgia",
    'Moscow, Russia'
]

phone = [
    '555-111-111-111',
    '555-222-222-222',
    '555-333-333-333',
    '555-444-444-444',
    '555-555-555-555',
    '555-666-666-666',
    '555-777-777-777',
    '555-888-888-888',
    '555-999-999-999',
    '555-000-000-000',
]

email = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
]

print(book(names,city,phone,email))