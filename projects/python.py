f = open("score.txt", 'r', True)
while True:
    
    line = f.readline()
    if not line: break
    print(line)

f.close()

print line.replace('-', ',')
