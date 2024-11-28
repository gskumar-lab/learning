unsorted = 'animals.txt'
sorted_file = 'sorted_animals.txt'
templist = []

with open(unsorted, 'r') as infile:
    for animal in infile:
        templist.append(animal.strip()) 


templist.sort()


with open(sorted_file, 'w') as outfile:
    for animal in templist:
        outfile.write(animal + '\n') 

