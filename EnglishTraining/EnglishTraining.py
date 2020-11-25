# Программа "English Training"
# Реализованы следующие возможности:
#

import copy, random

print()
print('Вас приветствует программа "English Training"!')
EasyEnglishWords = ['food', 'bike', 'apple', 'do', 'mean']
EasyRussianWords = ['еда', 'велосипед', 'яблоко', 'делать', 'иметь в виду']
EasyEnglishWordsTraining = []
EasyRussianWordsTraining = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
            'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r',\
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    print('Меню\n')
    print('1. Просмотреть слова для тренировки')
    print('2. Добавить слово для тренировки')
    print('3. Начать тренировку')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')

    # Выход из программы

    if userChoice.lower() == 'выход':
        exit()

    # Вывод слов для тренировок на экран

    if (userChoice == '1'):
        print()
        if len(EasyEnglishWords) == 0:
            print('Ваш список слов пуст!\n')
        else:
            number = 1
            print('─' * 43)
            print('|  №  |      Слово      |     Перевод     |')
            print('─' * 43)
            for i in range(len(EasyEnglishWords)):
                print('|{:^5d}| {:<15} | {:<15} |'\
.format(number, EasyEnglishWords[i], EasyRussianWords[i]))
                print('─' * 43)
                number += 1

    # Добавить слова для тренировки

    if (userChoice == '2'):
        add = True
        print()
        print('Добавление слова для тренировки')
        enWord = input('Введите слово на английском языке: ')
        ruWord = input('Введите перевод слова на русском языке: ')
        print('-' * 43)
        for i in range(len(EasyEnglishWords)):
            if enWord.lower() == EasyEnglishWords[i]:
                print('\nТакое слово уже есть в Вашем списке!')
                add = False
                break
        if add == True:
            EasyEnglishWords.append(enWord.lower())
            EasyRussianWords.append(ruWord.lower())
            print('\nСлово "', enWord, '" добавлено!')
        print()

    if (userChoice == '3'):

        # Выбор типа тренировки

        while True:
            EnglishWordsTraining = copy.deepcopy(EasyEnglishWords)
            RussianWordsTraining = copy.deepcopy(EasyRussianWords)

            print()
            print('Выберите тип тренировки:')
            print('1. Слово-перевод')
            print('2. Перевод-слово')
            print('3. Правописание')
            print('\nДля того, чтобы вернуться в предыдущее меню, \
наберите "Назад""\n')
            userChoiceTraining = input('Выберите пункт меню: ')

            # Возврат к предыдущему меню

            if userChoiceTraining.lower() == 'назад':
                break

            # Тренировка на знание перевода (с английского на русский)

            if (userChoiceTraining == '1'):
                print()
                print('\nТренировка "Слово-перевод"\nВыберите верный \
перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(EnglishWordsTraining) - 1)
                    if EnglishWordsTraining[trueTranslate] == 'None':
                        while EnglishWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(EnglishWordsTraining) - 1)                       
                    print('Выберите верный перевод: ',\
                          EnglishWordsTraining[trueTranslate])
                    for i in range(len(EasyRussianWords)):
                        print(str(i + 1), ') ', EasyRussianWords[i])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer == str(trueTranslate + 1):
                        EnglishWordsTraining.\
                        remove(EnglishWordsTraining[trueTranslate])
                        EnglishWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(EnglishWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

            # Тренировка на знание перевода (с русского на английский)

            if (userChoiceTraining == '2'):
                print()
                print('\nТренировка "Перевод-слово"\n\
Выберите верный перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(RussianWordsTraining) - 1)
                    if RussianWordsTraining[trueTranslate] == 'None':
                        while RussianWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(RussianWordsTraining) - 1)                       
                    print('Выберите верный перевод: ',\
                          RussianWordsTraining[trueTranslate])
                    for i in range(len(EasyEnglishWords)):
                        print(str(i + 1), ') ', EasyEnglishWords[i])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer == str(trueTranslate + 1):
                        RussianWordsTraining.\
                        remove(RussianWordsTraining[trueTranslate])
                        RussianWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(RussianWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

            # Тренировка на правописание

            if (userChoiceTraining == '3'):
                print()
                print('\nТренировка "Правописание"\n\
Введите верный перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(RussianWordsTraining) - 1)
                    if RussianWordsTraining[trueTranslate] == 'None':
                        while RussianWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(RussianWordsTraining) - 1)                       
                    print('Введите верный перевод: ',\
                          RussianWordsTraining[trueTranslate])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer.lower() == EnglishWordsTraining[trueTranslate]:
                        RussianWordsTraining.\
                        remove(RussianWordsTraining[trueTranslate])
                        RussianWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(RussianWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break
    print()
