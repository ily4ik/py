import random

def game():
    arr = pickword()
    word = arr[0]
    hint = arr[1]
    state = 1
    gues = '='
    fin = list(word)
    while gues != word.lower():
        draw(state)
        fin = comp(list(word.lower()), list(gues.lower()), list(fin))
        print("".join(fin))
        print(hint)
        state += 1
        gues = input('Догадки? ').lower()
        if state >= 7:
            print('Вы проиграли')
            return
    print('Вы выйграли!')

def pickword():
    words = readfile("words")
    word = words[random.randint(0, len(words)-1)].split(', ')
    return word

def readfile(name):
    f = open(f"{name}.txt", encoding='utf-8')
    words = f.read().split('\n')
    f.close()
    return words

def draw(state):
    f = open(f"{state}.txt", encoding='utf-8')
    print(f.read())
    f.close()

def comp(word1, word2, final):
    if word1 == final:
        for i in range(0,len(word1)):
            final[i] = '-'
    for i in range(0,min(len(word1),len(word2))):
        if word2[i] == word1[i]:
            final[i] = word1[i]
    return final
game()
