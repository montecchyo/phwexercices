the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'penies', 2, 'dimes', 3, 'quarters']


#for number in the_count:
#    print(f"This is count {number}")

elements = []
for i in range(6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Element was {i}")

elements.append(1)

for i in elements:
    print(f"Element was {i}")