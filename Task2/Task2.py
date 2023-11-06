import re
def matchText(text):
    matches = re.findall(r'(?:^|[^уеыаоэяиюё]|[а-яА-Я0-9ёЁ_-]*[^уеыаоэяиюё \n])[уеыаоэяиюё]{2}(?: |[^уеыаоэяиюё \n][а-яА-Я0-9ёЁ_-]* )[а-яА-Я0-9ёЁ_-]*', text, flags=re.MULTILINE)
    #print(matches)
    for match in matches:
        match = re.search(r'[а-яА-Я0-9ёЁ_-]+ [а-яА-Я0-9ёЁ_-]+', match)[0]
        vowels = 0
        secondWord = re.search(r' [а-яА-Я0-9ёЁ_-]*', match)[0]
        for s in secondWord:
            if s in 'уУеЕыЫаАоОэЭяЯиИюЮёЁ':
                vowels += 1
        if vowels <= 3:
            print(re.search(r'[а-яА-Я0-9ёЁ_-]*', match)[0])
matchText('Кривошеее существо гуляет по парку')
matchText('еее ее е е е ее ееее е-е -е е- ее- -ее е-е-ее-е---е- е--ее--е е-е-е- е--е -е -е -е-еее-е -ее- апр ее -')
matchText('В этом предложении пять слов')
matchText('Этому предложению недостаёт шесть слов, чтобы их было пятнадцать')
matchText('оо опо оо опопо оо опопопо')
