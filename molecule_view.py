

print('What does this molecule look like?...')


MOLECULES = []

OXYGEN = r"""
    O=O
"""

WATER = r"""
        O
       / \
      H   H
"""

CAFFEINE = r"""
           O   CH3
      H3C  ||  /
        \N/  \/N\
          |   || /
         //\N/ \N
        O   |
            CH3 

"""

DOPAMINE = r"""
HO     NH2
  \/\/\/
  | |
  /\/
 HO

"""

print()
print('(O) OXYGEN')
print('(W) WATER')
print('(C) CALCIUM')
print('(D) DOPAMINE')
print()
print('Choose one...')

response = input('> ').upper()



if response == 'O':
    print(OXYGEN)

elif response == 'W':
    print(WATER)

elif response == 'C':
    print(CAFFEINE)

elif response == 'D':
    print(DOPAMINE)
