from lib import Azbua_m

vivod = []
text = input().lower().split()
for i in range(len(text)):
    for j in range(len(text[i])):
        vivod.append(Azbua_m[text[i][j]])
    print(' '.join(vivod))
    vivod.clear()
