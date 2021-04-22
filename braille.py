from lib import Braille


def braille_code(text):
    answer = list()
    return_text = list()
    text = text.lower().split()
    for i in range(len(text)):
        for j in range(len(text[i])):
            answer.append(Braille[text[i][j]])
        return_text.append(''.join(answer))
        answer.clear()
    return '  '.join(return_text)


def debraille_code(text):
    return_text = list()
    text = text.lower().split()
    for i in text:
        for k in i:
            for j in Braille:
                if Braille[j] == k:
                    return_text.append(''.join(j))
        return_text.append(' ')
    return ''.join(return_text)
