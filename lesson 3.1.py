def num_translate(num):
    if num == "one":
        return "один"
    elif num == "two":
        return "два"
    elif num == "three":
        return "три"
    elif num == "four":
        return "четыре"
    elif num == "five":
        return "пять"
    elif num == "six":
        return "шесть"
    elif num == "seven":
        return "семь"
    elif num == "eight":
        return "восемь"
    elif num == "nine":
        return "девять"
    elif num == "ten":
        return "десять"
    else:
        return None


a = input("Введите число на английском:  ")
print(num_translate(a))
