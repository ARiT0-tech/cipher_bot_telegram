from lib import Morse


def morse(text):
    answer = list()
    return_text = list()
    text = text.lower().split()
    for i in range(len(text)):
        for j in range(len(text[i])):
            answer.append(Morse[text[i][j]])
        return_text.append(' '.join(answer))
        answer.clear()
    return '  '.join(return_text)


def demorse(text):
    answer = list()
    return_text = list()
    text = text.lower().split(' ')
    for i in text:
        if i == '':
            return_text.append(' ')
            continue
        for j in Morse:
            if Morse[j] == i:
                return_text.append(''.join(j))
        answer.clear()
    return ''.join(return_text)
