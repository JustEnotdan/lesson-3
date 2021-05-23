from random import randint


def get_jokes(n):
    jokes_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(n):
        a = nouns[randint(0, 4)] + " " + adverbs[randint(0, 4)] + " " + adjectives[randint(0, 4)]
        jokes_list.append(a)
    return jokes_list


num = int(input("Сколько шуток вы хотите?  "))

print(get_jokes(num))
