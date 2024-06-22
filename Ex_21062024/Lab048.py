
pramod_details2 = \
    {"name": "Pramod",
     "90": 34.34,
     "isMale": True,
     "Address": "KA"
     }

print(pramod_details2.get("Address"))
print(pramod_details2["Address"])
print(pramod_details2.values())
print(pramod_details2.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95, 'd': 95}
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for k, v in my_dict.items():
    print(k, v)



my_dict = dict()
my_dict['z'] = 45
my_dict['b'] = 12
my_dict['w'] = 32
my_dict['c'] = 11
my_dict['d'] = 19
print(my_dict)

for k,v in my_dict.items():
    print(k,v)