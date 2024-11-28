
with open('file.txt') as file:

    line_number=1

    for line in file:
        
        print(str(line_number)+": "+line.strip())
        line_number+=1

file.close()



