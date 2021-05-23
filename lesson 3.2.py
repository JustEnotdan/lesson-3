def num_translate(num):
    if num == "one":
        return "один"
    elif num == "One":
        return "Один"
    elif num == "two":
        return "два"
    elif num == "Two":
        return "Два"
    elif num == "three":
        return "три"
    elif num == "Three":
        return "Три"
    elif num == "four":
        return "четыре"
    elif num == "Four":
        return "Четыре"
    elif num == "five":
        return "пять"
    elif num == "Five":
        return "Пять"
    elif num == "six":
        return "шесть"
    elif num == "Six":
        return "Шесть"
    elif num == "seven":
        return "семь"
    elif num == "Seven":
        return "Семь"
    elif num == "eight":
        return "восемь"
    elif num == "Eight":
        return "Восемь"
    elif num == "nine":
        return "девять"
    elif num == "Nine":
        return "Девять"
    elif num == "ten":
        return "десять"
    elif num == "Ten":
        return "Десять"
    else:
        return None


a = input("Введите число на английском:  ")
print(num_translate(a))
