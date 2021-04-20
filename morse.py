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
    return return_text
