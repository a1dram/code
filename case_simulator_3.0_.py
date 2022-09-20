import random
import time
from termcolor import colored

sp = []
bal = 10000
s = 0
# кейс Прорыв
# ----------------------------------------------------------------------------------------------------------------------
prorivSin = [(colored("MP7 | Городская опасность", "blue")),
             (colored("Негев | Пустынная атака", "blue")),
             (colored("SSG 08 | Пучина", "blue")),
             (colored("UMP-45 | Лабиринт", "blue")),
             (colored("P2000 | Слоновая кость", "blue")), ]
prorivPurple = [(colored("Nova | Карп кои", "magenta")),
                (colored("P250 | Сверхновая", "magenta")),
                (colored("ПП-19 Бизон | Осирис", "magenta")),
                (colored("CZ75-Auto | Тигр", "magenta")), ]
prorivPink = [('\033[95mDesert Eagle | Заговор\033[0m'),
              ('\033[95mFive-SeveN | Птичьи игры\033[0m'),
              ('\033[95mGlock-18 | Дух воды\033[0m'), ]
prorivRed = [(colored("p90 | Азимов", "red")),
             (colored("M4A1-S | Сайрекс", "red"))]
prorivKnife = [(colored("★ Нож-бабочка | Кровавая паутина", "yellow")),
               (colored("★ Нож-бабочка | Сажа", "yellow")),
               (colored("★ Нож-бабочка | Северный лес", "yellow")),
               (colored("★ Нож-бабочка | Африканская сетка", "yellow")),
               (colored("★ Нож-бабочка | Градиент", "yellow")),
               (colored("★ Нож-бабочка | Поверхностная закалка", "yellow")),
               (colored("★ Нож-бабочка | Поверхностная закалка - Blue Gem", "yellow")),
               (colored("★ Нож-бабочка", "yellow")),
               (colored("★ Нож-бабочка | Ночь", "yellow")),
               (colored("★ Нож-бабочка | Убийство", "yellow")),
               (colored("★ Нож-бабочка | Патина", "yellow")),
               (colored("★ Нож-бабочка | Пиксельный камуфляж \"Лес\"", "yellow")),
               (colored("★ Нож-бабочка | Городская маскировка", "yellow")),
               (colored("★ Нож-бабочка | Вороненая сталь", "yellow")), ]
# ----------------------------------------------------------------------------------------------------------------------
# Тёмный кейс
# ----------------------------------------------------------------------------------------------------------------------
TemnSin = [(colored("Dual Berettas | Драконий дуэт", "blue")),
           (colored("FAMAS | Выживший", "blue")),
           (colored("Glock‑18 | Призраки", "blue")),
           (colored("MAC-10 | Хроматика", "blue")),
           (colored("MAG-7 | Ядро кобальта", "blue")),
           (colored("SCAR-20 | Зеленый морпех", "blue")),
           (colored("XM1014 | Скумбрия", "blue")), ]
TemnPurple = [(colored("Автомат \"Галиль\" | Невозмутимость", "magenta")),
              (colored("M249 | Космический воитель", "magenta")),
              (colored("MP7 | Особая доставка", "magenta")),
              (colored("P250 | Охотник", "magenta")), ]
TemnPink = [('\033[95mG3SG1 | Поток\033[0m'),
            ('\033[95mAK-47 | Снежная буря\033[0m'),
            ('\033[95mSSG 08 | Большая пушка\033[0m'), ]
TemnRed = [(colored("USP-S | Подтверждённое убийство", "red")),
           (colored("M4A1-S | Золотая спираль", "red"))]
TemnKnife = [(colored("★ Тычковые ножи | Кровавая паутина", "yellow")),
             (colored("★ Тычковые ножи | Сажа", "yellow")),
             (colored("★ Тычковые ножи | Северный лес", "yellow")),
             (colored("★ Тычковые ножи | Африканская сетка", "yellow")),
             (colored("★ Тычковые ножи | Градиент", "yellow")),
             (colored("★ Тычковые ножи | Поверхностная закалка", "yellow")),
             (colored("★ Тычковые ножи | Поверхностная закалка Blue Gem", "yellow")),
             (colored("★ Тычковые ножи", "yellow")),
             (colored("★ Тычковые ножи | Ночь", "yellow")),
             (colored("★ Тычковые ножи | Убийство", "yellow")),
             (colored("★ Тычковые ножи | Патина", "yellow")),
             (colored("★ Тычковые ножи | Пиксельный камуфляж \"Лес\"", "yellow")),
             (colored("★ Тычковые ножи | Городская маскировка", "yellow")),
             (colored("★ Тычковые ножи | Вороненая сталь", "yellow")), ]
# ----------------------------------------------------------------------------------------------------------------------
# Перчаточный кейс
# ----------------------------------------------------------------------------------------------------------------------
PerchSin = [(colored("MAG-7 | Эхолот", "blue")),
            (colored("Glock-18 | Литьё", "blue")),
            (colored("P2000 | Дерн", "blue")),
            (colored("CZ75-Auto | Полимер", "blue")),
            (colored("MP7 | Перистое облако", "blue")),
            (colored("Galil AR | Чёрный песок", "blue")),
            (colored("MP9 | Пыльный осадок", "blue")), ]
PerchPurple = [(colored("Nova | Ядозуб", "magenta")),
               (colored("Dual Berettas | Королевская чета", "magenta")),
               (colored("M4A1-S | Взгляд в прошлое", "magenta")),
               (colored("USP-S | Сайрекс", "magenta")),
               (colored("G3SG1 | Жало", "magenta"))]
PerchPink = [('\033[95mP90 | Неглубокая могила\033[0m'),
             ('\033[95mSawed-Off | Принцесса пустошей\033[0m'),
             ('\033[95mFAMAS | Механо-пушка\033[0m'), ]
PerchRed = [(colored("SSG 08 | Пламя дракона", "red")),
            (colored("M4A4 | Облом", "red"))]
PerchGloves = [(colored("★ Мотоциклетные перчатки | Spearmint", "yellow")),
               (colored("★ Мотоциклетные перчатки | Boom!", "yellow")),
               (colored("★ Мотоциклетные перчатки | Cool Mint", "yellow")),
               (colored("★ Мотоциклетные перчатки | Eclipse", "yellow")),
               (colored("★ Водительские перчатки | Diamondback", "yellow")),
               (colored("★ Водительские перчатки | Lunar Weave", "yellow")),
               (colored("★ Водительские перчатки | Crimson Weave", "yellow")),
               (colored("★ Водительские перчатки | Convoy", "yellow")),
               (colored("★ Перчатки спецназа | Forest DDPAT", "yellow")),
               (colored("★ Перчатки спецназа | Crimson Kimono", "yellow")),
               (colored("★ Перчатки спецназа | Emerald Web", "yellow")),
               (colored("★ Перчатки спецназа | Foundation", "yellow")),
               (colored("★ Перчатки «Бладхаунд» | Guerrilla", "yellow")),
               (colored("★ Перчатки «Бладхаунд» | Charred", "yellow")),
               (colored("★ Перчатки «Бладхаунд» | Snakebite", "yellow")),
               (colored("★ Перчатки «Бладхаунд» | Bronzed", "yellow")),
               (colored("★ Спортивные перчатки | Pandora's Box", "yellow")),
               (colored("★ Спортивные перчатки | Superconductor", "yellow")),
               (colored("★ Спортивные перчатки | Hedge Maze", "yellow")),
               (colored("★ Спортивные перчатки | Arid", "yellow")),
               (colored("★ Обмотки рук | Slaughter", "yellow")),
               (colored("★ Обмотки рук | Badlands", "yellow")),
               (colored("★ Обмотки рук | Leather", "yellow")),
               (colored("★ Обмотки рук | Spruce DDPAT", "yellow")),
               ]
# ----------------------------------------------------------------------------------------------------------------------
# Гамма-кейс
# ----------------------------------------------------------------------------------------------------------------------
GamSin = [(colored("P250 | Железное покрытие", "blue")),
          (colored("Five-SeveN | Неистовый даймё", "blue")),
          (colored("ПП-19 Бизон | Жнец", "blue")),
          (colored("SG 553 | Полет", "blue")),
          (colored("Tec-9 | Ледниковый покров", "blue")),
          (colored("Nova | Экзо", "blue")),
          (colored("MAC-10 | Плотоядный", "blue")), ]
GamPurple = [(colored("P90 | Воин дорог", "magenta")),
             (colored("Sawed-Off | В центре внимания", "magenta")),
             (colored("AUG | Аристократ", "magenta")),
             (colored("AWP | Фобос", "magenta")),
             (colored("Револьвер R8 | Перезагрузка", "magenta"))]
GamPink = [('\033[95mSCAR-20 | Кровавый спорт\033[0m'),
           ('\033[95mP2000 | Императорский дракон\033[0m'),
           ('\033[95mM4A4 | Безлюдный космос\033[0m'), ]
GamRed = [(colored("Glock-18 | Пустынный повстанец", "red")),
          (colored("M4A1-S | Механо-пушка", "red"))]
GamKnife = [(colored("★ Нож с лезвием-крюком | Легенды", "yellow")),
            (colored("★ Нож с лезвием-крюком | Черный глянец", "yellow")),
            (colored("★ Нож с лезвием-крюком | Гамма-волны - Фаза 1", "yellow")),
            (colored("★ Нож с лезвием-крюком | Гамма-волны - Фаза 2", "yellow")),
            (colored("★ Нож с лезвием-крюком | Гамма-волны - Фаза 3", "yellow")),
            (colored("★ Нож с лезвием-крюком | Гамма-волны - Фаза 4", "yellow")),
            (colored("★ Нож с лезвием-крюком | Гамма-волны - Изумруд", "yellow")),
            (colored("★ Нож с лезвием-крюком | Автотроника", "yellow")),
            (colored("★ Нож с лезвием-крюком | Чистая вода", "yellow")),
            (colored("★ Нож с лезвием-крюком | Ручная роспись", "yellow")),
            (colored("★ Штык-нож M9 | Гамма-волны - Фаза 1", "yellow")),
            (colored("★ Штык-нож M9 | Гамма-волны - Фаза 2", "yellow")),
            (colored("★ Штык-нож M9 | Гамма-волны - Фаза 3", "yellow")),
            (colored("★ Штык-нож M9 | Гамма-волны - Фаза 4", "yellow")),
            (colored("★ Штык-нож M9 | Гамма-волны - Изумруд", "yellow")),
            (colored("★ Штык-нож M9 | Автотроника", "yellow")),
            (colored("★ Штык-нож M9 | Чистая вода", "yellow")),
            (colored("★ Штык-нож M9 | Ручная роспись", "yellow")),
            (colored("★ Штык-нож M9 | Легенды", "yellow")),
            (colored("★ Штык-нож M9 | Черный глянец", "yellow")),
            (colored("★ Складной нож | Легенды", "yellow")),
            (colored("★ Складной нож | Черный глянец", "yellow")),
            (colored("★ Складной нож | Гамма-волны - Фаза 1", "yellow")),
            (colored("★ Складной нож | Гамма-волны - Фаза 2", "yellow")),
            (colored("★ Складной нож | Гамма-волны - Фаза 3", "yellow")),
            (colored("★ Складной нож | Гамма-волны - Фаза 4", "yellow")),
            (colored("★ Складной нож | Гамма-волны - Изумруд", "yellow")),
            (colored("★ Складной нож | Автотроника", "yellow")),
            (colored("★ Складной нож | Чистая вода", "yellow")),
            (colored("★ Складной нож | Ручная роспись", "yellow")),
            (colored("★ Керамбит | Черный глянец", "yellow")),
            (colored("★ Керамбит | Гамма-волны - Фаза 1", "yellow")),
            (colored("★ Керамбит | Гамма-волны - Фаза 2", "yellow")),
            (colored("★ Керамбит | Гамма-волны - Фаза 3", "yellow")),
            (colored("★ Керамбит | Гамма-волны - Фаза 4", "yellow")),
            (colored("★ Керамбит | Гамма-волны - Изумруд", "yellow")),
            (colored("★ Керамбит | Автотроника", "yellow")),
            (colored("★ Керамбит | Чистая вода", "yellow")),
            (colored("★ Керамбит | Ручная роспись", "yellow")),
            (colored("★ Керамбит | Легенды", "yellow")),
            (colored("★ Штык-нож | Легенды", "yellow")),
            (colored("★ Штык-нож | Черный глянец", "yellow")),
            (colored("★ Штык-нож | Гамма-волны - Фаза 1", "yellow")),
            (colored("★ Штык-нож | Гамма-волны - Фаза 2", "yellow")),
            (colored("★ Штык-нож | Гамма-волны - Фаза 3", "yellow")),
            (colored("★ Штык-нож | Гамма-волны - Фаза 4", "yellow")),
            (colored("★ Штык-нож | Гамма-волны - Изумруд", "yellow")),
            (colored("★ Штык-нож | Автотроника", "yellow")),
            (colored("★ Штык-нож | Чистая вода", "yellow")),
            (colored("★ Штык-нож | Ручная роспись", "yellow")),
            ]
# ----------------------------------------------------------------------------------------------------------------------
print((colored("Вас приветствует сайт pro_cases.com!", "red")))
print("Сегодня", time.strftime(colored("%A, %p;", 'blue')),
      time.strftime(colored("%d.%m.%Y", 'yellow')))
print("Вы зашли на сайт в", time.strftime(colored("%H:%M:%S", 'blue')))
print()
print("Ваш баланс:", (colored(bal, "green")), "рублей")
print("Стоимость ключа:", (colored("155", "green")), "рублей")
print()
print("В наличии есть", (colored("4", "magenta")), "кейса.")
print(
    "Если захотите оставить приз, напишите", colored("Cтоп", 'blue') + ", если же хотите открыть кейс"
                                                                       " - ")
print("Напишите номер кейса, который хотите открыть: ")


def finish():
    global b1
    time.sleep(2)
    print()
    print(colored("Недостаточно средств!", "red"))
    print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
    print("Ваш конечный результат:", (colored(bal, 'green')), "руб.")
    print()
    if (s >= 1) and (s < 6):
        print(colored("Неплохо!", 'cyan'))
    elif (s >= 6) and (s < 15):
        print(colored("Круто!", 'blue'))
    elif (s >= 15) and (s < 20):
        print(colored("Отлично!", 'magenta'))
    elif (s >= 20) and (s < 40):
        print(colored("Вот это да!", 'green'))
    elif (s >= 40) and (s < 50):
        print(colored("Legendary!", 'yellow'))
    elif (s >= 50) and (s <= 100):
        print(colored("Y", 'red') + colored("o", 'yellow') + colored("u", 'cyan'),
              colored("a", 'magenta') + colored("r",
                                                'red') + colored(
                  "e", 'yellow'),
              colored("G", 'cyan') + colored("O", 'magenta') + colored("D", 'red') + colored("!", 'yellow'))
    time.sleep(3)
    b1 = False


b1 = True
while b1:
    a = random.randint(0, 400)
    print((colored("1)", "magenta")), colored("Прорыв", 'cyan'))
    print((colored("2)", "magenta")), colored("Тёмный кейс", 'cyan'))
    print((colored("3)", "magenta")), colored("Перчаточный кейс", 'cyan'))
    print((colored("4)", "magenta")), colored("Гамма-кейс", 'cyan'))
    n = input()
    time.sleep(0.5)

    if n == '1':
        s += 1
        bal -= 155
        print("Вы купили кейс", (colored("Прорыв", "cyan")) + ", с вас снялось", (colored("155", "green")),
              "рублей.")
        print("Ваш баланс:", (colored(bal, "green")), "рублей")
        time.sleep(0.2)
        print("")
        print("Выполняется открытие кейса", (colored("Прорыв", "cyan")) + "...")
        print("")
        time.sleep(1)
        if a == 0:
            skin = random.choice(prorivKnife)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(25000, 604300)
            print(f'Флоат: {random.uniform(0, 0.7)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 0) and (a <= 321):
            skin = random.choice(prorivSin)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(1, 8)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 321) and (a <= 385):
            skin = random.choice(prorivPurple)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(40, 178)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 385) and (a <= 398):
            skin = random.choice(prorivPink)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(200, 720)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 398) and (a <= 400):
            skin = random.choice(prorivRed)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(560, 8000)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        if bal < 155:
            finish()

    elif n == '2':
        s += 1
        bal -= 155
        print("Вы купили", (colored("Тёмный кейс", "cyan")) + ", с вас снялось", (colored("155", "green")),
              "рублей.")
        print("Ваш баланс:", (colored(bal, "green")), "рублей")
        time.sleep(0.2)
        print("")
        print("Выполняется открытие", (colored("Тёмного кейса", "cyan")) + "...")
        print("")
        time.sleep(1)
        if a == 0:
            skin = random.choice(TemnKnife)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(5000, 64230)
            print(f'Флоат: {random.uniform(0, 0.7)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 0) and (a <= 321):
            skin = random.choice(TemnSin)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(1, 10)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 321) and (a <= 385):
            skin = random.choice(TemnPurple)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(40, 190)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 385) and (a <= 398):
            skin = random.choice(TemnPink)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(513, 2120)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 398) and (a <= 400):
            skin = random.choice(TemnRed)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(660, 9300)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        if bal < 155:
            finish()

    elif n == '3':
        s += 1
        bal -= 155
        print("Вы купили", (colored("Перчаточный кейс", "cyan")) + ", с вас снялось", (colored("155", "green")),
              "рублей.")
        print("Ваш баланс:", (colored(bal, "green")), "рублей")
        time.sleep(0.2)
        print("")
        print("Выполняется открытие кейса", (colored("Перчаточный", "cyan")) + "...")
        print("")
        time.sleep(1)
        if a == 0:
            skin = random.choice(PerchGloves)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(9300, 574230)
            print(f'Флоат: {random.uniform(0, 0.7)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 0) and (a <= 321):
            skin = random.choice(PerchSin)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(1, 10)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 321) and (a <= 385):
            skin = random.choice(PerchPurple)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(40, 187)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 385) and (a <= 398):
            skin = random.choice(PerchPink)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(200, 820)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 398) and (a <= 400):
            skin = random.choice(PerchRed)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(560, 6000)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        if bal < 155:
            finish()

    elif n == '4':
        s += 1
        bal -= 155
        print("Вы купили", (colored("Гамма-кейс", "cyan")) + ", с вас снялось", (colored("155", "green")),
              "рублей.")
        print("Ваш баланс:", (colored(bal, "green")), "рублей")
        time.sleep(0.2)
        print("")
        print("Выполняется открытие кейса", (colored("Гамма", "cyan")) + "...")
        print("")
        time.sleep(1)
        if a == 0:
            skin = random.choice(GamKnife)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(9000, 782300)
            print(f'Флоат: {random.uniform(0, 0.7)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 0) and (a <= 321):
            skin = random.choice(GamSin)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(1, 12)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 321) and (a <= 385):
            skin = random.choice(GamPurple)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(40, 182)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 385) and (a <= 398):
            skin = random.choice(GamPink)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(200, 720)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        elif (a > 398) and (a <= 400):
            skin = random.choice(GamRed)
            print("Вы выбили: ", skin + '!')
            sp.append(skin)
            x = random.randint(560, 12000)
            print(f'Флоат: {random.uniform(0, 0.9)}')
            time.sleep(0.5)
            print("Эта вещь стоит", (colored(x, "green")), "руб.")
            bal += x
            time.sleep(0.5)
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            print(colored("-------------------------------------------------------", 'yellow'))
            print("Напишите номер кейса, который хотите открыть: ")
        if bal < 155:
            finish()

    elif (n == "СТОП") or (n == "стоп") or (n == "Стоп"):
        if (bal >= 0) and (bal < 2000):
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(colored("Неплохо!", 'cyan'))
            time.sleep(3)
            b1 = False
        elif (bal >= 2000) and (bal < 5000):
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(colored("Круто!", 'blue'))
            time.sleep(3)
            b1 = False
        elif (bal >= 5000) and (bal < 15000):
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(colored("Отлично!", 'magenta'))
            time.sleep(3)
            b1 = False
        elif (bal >= 15000) and (bal < 35000):
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(('\033[95mGodly!\033[0m'))
            time.sleep(3)
            b1 = False
        elif (bal >= 35000) and (bal < 50000):
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(colored("Legendary!", 'yellow'))
            time.sleep(3)
            b1 = False
        elif bal >= 50000:
            print("Ваш баланс:", (colored(bal, "green")), "рублей")
            time.sleep(0.5)
            print("За всё время вы открыли", (colored(s, 'red')), "кейса(ов)")
            time.sleep(1)
            print(colored("Y", 'red') + colored("o", 'yellow') + colored("u", 'cyan'),
                  colored("a", 'magenta') + colored("r",
                                                    'red') + colored(
                      "e", 'yellow'),
                  colored("G", 'cyan') + colored("O", 'magenta') + colored("D", 'red') + colored("!", 'yellow'))
            time.sleep(3)
            b1 = False

print("За всё время вы выбили:")
print('\n'.join(sp))
