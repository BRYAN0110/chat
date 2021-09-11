with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    word = s[1:]
    time = s[0][:5]
    name = s[0][5:]
    print(time, ' ', name, ' ', word)