import telebot
import logging
import random

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) 

# import constans
from telebot import types

bot = telebot.TeleBot('774606011:AAHQzvuc97_YZYevL7LCJMh1tQkHdx3pjbA')
users = [410819637,329546876,591563627,513810155,645413390,544744166,514280124,558012259,933053790,301595058,431874826,725985865, 596672708,  443286422,  803899880,727629595,   573147939,        906970322,      542536111,    805166711,         927139023                       , 490528542     ,    934559656     , 410498438  ,  141083256,        374386376,   1153311022,    793089330,   531553285,  856420893,  525598059, 1121853974,    276667391,    914587344,   802459626,  517822953,   748026571,       835950936,   633195004,   807308376,     803452035,              223508200,     989253411,    818569405,    909583342,      538382824,  521140981,  1265568714,   466829080,  1071975476,   942458930,    751880788,    510451786,      668394665      , 711128851,    477861785,  468033104,    1038064476,     411467807,     268056638,       282970170,     487632083,    1114816841,         1119983052 ,   764883981 ,     1181396737, 914166356,      666165868     , 441937522, 849951686,     761328878,     1017341255   , 701264921,      1179091466,  914166356,   1277803311,      975495600,       1362656180,    901739410,      900481908,      389641524,     532517776,       715466005,       901739410,       560912405,       896310777,     436679970,      423012979,        1070269781,     290137143,    458130014,     907218362,   260590376,    589700747,   628131677,     465354836,   1060987866,    399377643,    355185570,  366240022,  617929990, 984185462,  982702076,  561725836,   309697506, 674698133,  1399983833,   900315030, 476800911,   379202773, 394424128, 625176973,   1384882453, 676543691,  625176973,  272177628,   1394344523,  1147669472, 696611370,  853217074,  1039630690, 760342877,   1014753974,  494619796,  466510262,   1202718965,   818569405,   233796308, 429168251,   1014753974, 792774683,  488261313,  649147906,  610167809,   760342877, 502291018,  1370525794, 599758620, 583827920, 1240388984, 782486934, 488802242,698582654, 14592351, 533005935, 765615424, 219627801, 632281856,   190086956,  899668417, 685767776,  622906331  ,899007965,  531287510, 706720454, 834263729,  160366076, 909543137, 561647142, 834263729, 566069039, 455950277, 1212826764,     411628179]
#         Стеблина              ЕГ                         Nikolay   Мельник  Veronika  ДеЛаВега   одесд2   АтельеЛилу Самотохина Воротынцева Bogdanovich Trone GrandeCube44     КостенкоОльга    Steblinaxiaomi      Hanna       Ошманина Ирина    Елена Городничая шик николаев      Hommie           Старинец          Max IT       Настя рыжий кот    Турик      Семенова И.      Дуденко Н.  Шевченко И.  Ирина Sh   Каспрук Н.  Беличенко А.  Шевцова К.   Бухаловская   Турик2       Батист       Декорейшн Киев  Цапок Инна,   Салаш Нина   Бойчук Елена  Ольга Маковская/Структуре    Шторград  Алтунина Т.   Лора Маэстро   Дарина Маэстро  Приемова    Гиза Лена   Озерова     скороход К   Скороход Л    Евтушенко Н    Грайпоинт    Бариба Анна     Артуэль Марина   Мыцык         Ткачук Т     Ткачук В     Самотохина      Демьян Мороз   Тюльпан Марина   Ньюволл          Донская      Савельева Ирина Дарина Головкина  Шелея Светлана   Федорец         Чумак Леся  Сухорукова Анна     Artemida  Бельэтаж   Белоусова Т    Яна Бекетова   K.O.R.A design   VG Interior Леся Чумак    Калина Нина И    Калина Ирина    Алена Росетти   Ирина Маэстро   Анжелика Хар  Мялковская Юля   Шпортун Ольга   Нила Харьков шр   маэстро ирина   Бергман Лариса    Каштан Анна    магнитЮля      Галя настарчук    Дисасле Елена  Ткалич Настя   Гайворонская    Дуденко     Фиранка    Дробот С       Алина Маэстро   Зудина Артель Маркова  Хайменова Екат МаксимДубл   Сингаевская  Гнездо Оля Даниленко Т   Батист   Крушевская Н    Привалова Св Манеж  Нюанс Нюанс Галран  Жарникова Шишлачева Стелла БроварыОльга попова Прованс  Марченко Л.   Ольга Тв ким Харьк   Думитрук   Литом    Литом Ира авесоль  Баровская Лиля   Анна Кинзерская  Лаурэль   Хомми  Ная Дизайн  Захаренко Оля Надя Новый Простир   Лариса Н П  Оксана Сансара ( Мир пола)   Женя Старченко ( Беркович)  Хомми  ДианаЛена Лианна Юля Шкребтий  Олена   Лаурэль Хом Ирина Жилинская  Алла ткач Годована О  Наталья от Годованой Елена эфес,Дилия Домио,Елена Домио, Aleksandra Домио, Инсайт Yuliya Skobletska, Инсайт Natalia,Ray Николаем мебель Шик Аня, Лучко Светлана, Момот Алеся Юлия Захарова  Шторы Люкс Тищенко Людмила Галерея Виарди, Allagio Артфешн Тая Мандерс рыбалко Москаленко Ная Таня   Ная Аня  Дорнум Андрей Васильева Рыбак Давиденко, Броневичева Донум,


@bot.message_handler(commands=['start'])

def handle_start(message, text=True):
    if message.from_user.id in users:
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('📚 Suerte Elegancia collection', '📚 Suerte mebel')
        #user_markup.row('📚 Запросить прайс:', '📖 Запрос на наличие Suerte', '❓ Задать вопрос')
        #user_markup.row('📞 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
        if text:
            bot.send_message(message.from_user.id, 'Приветствую ✌ {} выберите пункт меню: ⬇'.format(message.from_user.first_name),
                         reply_markup=user_markup)
        else:
            bot.send_message(message.from_user.id, 'Выберите пункт меню ⬇',
                         reply_markup=user_markup)
                         
    else:
        bot.send_message(message.from_user.id, 'Для получения доступа к информации, отправьте этот id на телеграм @SuerteSupport, {}, id - {}'
                         .format(message.from_user.first_name, message.from_user.id))
                         
@bot.message_handler(content_types=['comand'])
def log(message):
    print("<!------!>")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id), message.text))
                        
       
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.from_user.id in users:
       if message.text == "📚 Suerte Elegancia collection":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Запросить прайc', ' 📥 Запросить наличие на складе', '📢   Задать вопрос по Suerte' )
    #    manager_markup.row('🔎 Запросить прайc', ' 📥 Запросить наличие тканей Suerte', '📢   Задать вопрос по Suerte' )
         manager_markup.row('📞 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
        
       elif message.text == "🔎 Запросить прайc":
         bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/1gXRc6xPUmX4dNPvNfvC7leIifBUlNvEJ7-L-QzEdnh0/view")
          #keyboard = telebot.types.InlineKeyboardMarkup()
          #                                  url_button = types.InlineKeyboardButton(text="Нажмите чтобы перейти на прайс-лист",
          #                             url="https://docs.google.com/spreadsheets/d/1gXRc6xPUmX4dNPvNfvC7leIifBUlNvEJ7-L-QzEdnh0/edit#gid=1265136000")
          #keyboard.add(url_button)
          #bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти на Google Docs.", reply_markup=keyboard)
        
       elif message.text == "📢   Задать вопрос по Suerte":
         bot.send_message(message.from_user.id, "Напишите свой вопрос на телеграм @Suertesupport")
         log(message)
       elif message.text == "📞 Позвонить в компанию":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клиент менеджеры', 'Региональные менеджеры по городам', 'Бренд менеджеры')
         phone_markup.row('Офис менеджер', 'Горячая линия директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup)
        
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Запросить прайc', ' 📥 Запросить наличие на складе', '📢   Задать вопрос по Suerte' )
         manager_markup.row('📞 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
       
       elif message.text == "📥 Запросить наличие на складе":
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Коллекция Suerte', '📚 L1nkstudio')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=sklad_markup)
        
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Запросить прайc', ' 📥 Запросить наличие на складе', '📢   Задать вопрос по Suerte' )
         manager_markup.row('📞 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)

      
       elif message.text == "Горячая линия директора":
         bot.send_message(message.from_user.id, 'Елена Геннадьевна\n' +
                '\n' +
                '📱 +38 (067) 401 32 03\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 director@daylight.com.ua')
       
       elif message.text == "Клиент менеджеры":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Юлия Липовая', 'Екатерина Бычковская')
         phone_markup.row('Екатерина Некипелая', 'Лилия Пинчук')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup)   
         
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клиент менеджеры', 'Региональные менеджеры по городам', 'Бренд менеджеры')
         phone_markup.row('Офис менеджер', 'Горячая линия директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup) 
           
                
       elif message.text == "Региональные менеджеры по городам":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Киев', 'Харьков', 'Львов')
         phone_markup.row('Днепр', 'Одесса')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup)   
        
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клиент менеджеры', 'Региональные менеджеры по городам', 'Бренд менеджеры')
         phone_markup.row('Офис менеджер', 'Горячая линия директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup) 
        
         
       elif message.text == "Киев":
         bot.send_message(message.from_user.id, 'Светлана Турик\n' +
                '\n' +
                '📱 +38 (067) 445 32 05\n' +
                '\n' +
                '☎ +38 (044) 545 60 70\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 tur@daylight.com.ua')
         bot.send_message(message.chat.id, 'Шевцова Екатерина\n ' +
                 '\n'
                 '📱   +38 (067) 767-87-86 \n' +
                 '\n'
                 '☎️  +38 (044) 545-60-70 \n' +
                 '\n'
                 '📲️  +38 (093) 767-87-86 \n' +
                 '\n'
                 '📧 suerte2@daylight.com.ua \n' +
                 '\n'
                  , )
       elif message.text == "Харьков":
         bot.send_message(message.chat.id, 'Беличенко Анна \n '+
        '\n'
                        '📱   +38 (066) 831 89 69  \n'+
                         '\n'
                         '☎️  +38 (067) 502 89 92 \n'+
                         '\n'
                         '📲️  +38 (057) 728 23 14 \n'+
                         '\n'
                         '📧anna@daylight.com.ua \n'+
                         '\n'
                         ,)
       elif message.text == "Львов":
        bot.send_message(message.chat.id, 'Бакун Юлия \n ' +
                         '\n'
                         '📱   +38 (066) 831 89 69  \n' +
                         '\n'
                         '☎️  +38 (067) 502 89 92 \n' +
                         '\n'
                         '📲️  +38 (057) 728 23 14 \n' +
                         '\n'
                         '📧 sales.lviv@daylight.com.ua \n' +
                         '\n', )
       elif message.text == "Днепр":
         bot.send_message(message.chat.id, 'Дуденко Наталья \n ' +
                         '\n'
                         '📱   +38 (067) 450 00 79  \n' +
                         '\n'
                         '☎️  +38 (099)401 36 16  \n' +
                         '\n'
                         '📧 dneprdl@daylight.com.ua \n' +
                         '\n'
                         )
       elif message.text == "Одесса":
        bot.send_message(message.chat.id, 'Семенова Инна \n ' +
                                                '\n'
                         '📱   +38 (067) 504 91 09 \n' +
                         '\n'
                         '☎️  +38 (099)401 36 16  \n' +
                         '\n'
                         '📧 sales.odessa@daylight.com.ua  \n' +
                         '\n'
                         )
         
       elif message.text == "Бренд менеджеры":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Suerte Elegancia', 'FR One Margo Iliv', 'Suerte mebel, Link Studio, Adora')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup)           
         
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клиент менеджеры', 'Региональные менеджеры по городам', 'Бренд менеджеры')
         phone_markup.row('Офис менеджер', 'Горячая линия директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=phone_markup) 
                
       elif message.text == "Suerte Elegancia":
         bot.send_message(message.chat.id, 'Старинец Наталья  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38(067) 405-66-74 \n' +
                         '\n'
                         '☎️@TelegramStarinets \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
                
       elif message.text == "FR One Margo Iliv":
           bot.send_message(message.chat.id, 'Самотохина Елена \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38 (067)245-10-57 \n' +
                         '\n'
                         '☎️  +38 (067)245-10-57 \n' +
                         '\n' +
                         '📧 bm2@daylight.com.ua\n' +
                         '\n')
       elif message.text == "Suerte mebel, Link Studio, Adora":
         bot.send_message(message.chat.id, 'Cтеблина Елена  \n ' +
                         '\n'
                         '📱 +38 (067) 247 42 22 \n' +
                         '\n'
                         '📱 +38 (067) 524-59-09\n' +
                         '\n'
                         '📧  fibre@daylight.com.ua\n' +
                         '\n'
                         '@HelenDaylight\n')
                
                
       elif message.text == "📚 Коллекция Suerte":
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Hазад') #английская буква H
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "↩Hазад": #английская буква H
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Коллекция Suerte', '📚 L1nkstudio')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=sklad_markup)
         
       elif message.text == "📥 Запросить наличие на складе":
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Коллекция Suerte', '📚 L1nkstudio')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=sklad_markup)
         
       
       elif message.text == "A":
         tkaniA_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniA_markup.row('Ancona discount', 'Aria', 'Atlanta', 'Aurora discount')
         tkaniA_markup.row('↩Назaд')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniA_markup)
       elif  message.text == "Ancona discount":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1atBkKXvtfQ2MinOTYjk8e9TnH5k_vqVp") 
       elif  message.text == "Aria":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1QQA05iPsiIcyKR4JhAifi8dBqDyEHymM")
       elif  message.text == "Atlanta":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1jpJflxr2q41F2ypWoofvwaa_znneW98s")         
       elif  message.text == "Aurora discount":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1QOOH2BtdY5JIplEzVAUCWmzElc6ZA7t6") 
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         #1111tkani_markup.row('↩Назад')
         tkani_markup.row('↩Hазад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "B":
         tkaniB_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniB_markup.row('Bavaria', 'Beatrice', 'Bergamo', 'Bianca')
         tkaniB_markup.row('Boston', 'Braveheart','Brooklyn')
         tkaniB_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniB_markup)
       elif  message.text == "Bavaria":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1YuGjRkjqEmrUcOhoZZBrb6SUqYgtjgBJ") 
       elif  message.text == "Beatrice":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=12Et-KunPoG5oc12ozVRMI1oWUQEtjyq_")
       elif  message.text == "Bergamo":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1qxb3wPmGzY7sfOyprZjQwfhJpYBgFZy9")         
       elif  message.text == "Bianca":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Qakr5RRUPMlvr_SRXr7knb4IJ3NmzmLb") 
       elif  message.text == "Boston":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1LqB-SZ30HLo-WgUx5yzs66Rg2m2_e3bH")
       elif  message.text == "Braveheart":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1K4AEclmzJF6u-6-fK3I_qJGutNpbx1hX")
       elif  message.text == "Brooklyn":
                bot.send_message(message.from_user.id, "https://drive.google.com/file/d/14pkyLSIvzyYtCGv18m3AmiOtu9d1HG_R")                
      
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "C,D": 
         tkaniCD_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniCD_markup.row('Calista', 'Chelsea', 'Chalet', 'Chicago')
         tkaniCD_markup.row('Convoy','Dallas', 'Diamante')
         tkaniCD_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniCD_markup)
       elif  message.text == "Calista":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1o2lpU4Ibz6Y9J8Lh78Y4Dz0sGAnP5udW") 
       elif  message.text == "Chelsea":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1cfEx30MVeOpPfyoIc8qCs80SFgF0usz_")
       elif  message.text == "Chalet":
                bot.send_message(message.from_user.id, "https://drive.google.com/file/d/1O88M6DgG0yp3B7K_0e5ggmcL09aAU0Dj")         
       elif  message.text == "Chicago":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1wZ3T95WSOicfo_ZEBAG_JZDFtSy-00FF") 
       elif  message.text == "Convoy":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1AuokqT046PSaH8gc5p3kfjoxzdCLEi7G")
       elif  message.text == "Dallas":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Ya96HAdCuzAxSnQ0tl_zsJYi5RExazex")
       elif  message.text == "Diamante":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1kWRc2O33gQbunHXbxZyWZXGVf1UUMqaM")   
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "E,F,G": 
         tkaniEFG_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniEFG_markup.row('Elegante', 'Feliche', 'Florence', 'Fuji dim-out')
         tkaniEFG_markup.row('Gentleman','Georgia', 'Grace', 'Garden')
         tkaniEFG_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniEFG_markup)
       elif  message.text == "Elegante":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1TZLoXkyKhD2VLbsm2hHMRYE3hOk49SNk") 
       elif  message.text == "Feliche":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1qRDw2DwHctVvLabGNsvoqjjpUrt_AJ84")
       elif  message.text == "Florence":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1dhWXBTtqia9QsqXUSI3_-zzsBw7MZfpc") 
       elif  message.text == "Fuji dim-out":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1JAO-WsJ1Ry-7sF3b0ji04Gbwr8A0vpM5")
       elif  message.text == "Gentleman":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1yCVam7nUTTlft0r-69IqQsBfhVYNG4VN")
       elif  message.text == "Georgia":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1aaFTNEmBoAJsB7yIpxv283Uh9OljzPtZ")
       elif  message.text == "Grace":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1gemqzPNNr6h_OWzOndhwbxV9koI5ShJv")
       elif  message.text == "Garden":
                bot.send_message(message.from_user.id, "https://drive.google.com/file/d/1gKR1Y7yUJSVZGHXDRBlGxoZzZi_druIK/view?usp=sharing")          

      
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "H,I,J": 
         tkaniHIJ_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniHIJ_markup.row('Historia', 'Houston', 'Isabella', 'Janett')
         tkaniHIJ_markup.row('Journal','Georgia', 'Grace')
         tkaniHIJ_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniHIJ_markup)
       elif  message.text == "Historia":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1VnW_IBoUGRAXhAuuwym5ItQEQutZTu-J") 
       elif  message.text == "Houston":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Iktr7TFjwUFSNTYvdLpLuqXqYzKN7fwv")
       elif  message.text == "Isabella":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1y5LyQNiiD-BqAYXs0INTOaF5X67h82lU") 
       elif  message.text == "Janett":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1mwDGKneUYI4C5k3EqHZPbStYLHZxCEHK")
       elif  message.text == "Journal":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1t67x5M9EjY0Z-S-3oEV30GxpR5kzwDS2")
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "L": 
         tkaniL_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniL_markup.row('Lion', 'Lluvia', 'Loreto', 'Lure trevira')
         tkaniL_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniL_markup)
       elif  message.text == "Lion":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=101gAN25jTQgG7cg0VJzQuVpVWiA_f12I") 
       elif  message.text == "Lluvia":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=16GK9J3CwLUyXjl2dPcwhP0oSJ2_8eEz0")
       elif  message.text == "Loreto":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1F68xTYKnL-rEgovRxuhM-QHV52s0792O")         
       elif  message.text == "Lure trevira":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=147fhYHLZZleTn-llPl3pshOw9JYsadp1") 
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "M,N":
         tkaniMN_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniMN_markup.row('Malta','Millenium', 'Mist', 'Montana', 'Monte Carlo')
         tkaniMN_markup.row('Monterey', 'Natural', 'New York', 'Novara')
         tkaniMN_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniMN_markup)
       elif  message.text == "Malta":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1mYJmfOo8J57jTEiHgpFbIsj-f6qeBs8x")
       elif  message.text == "Millenium":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1mYJmfOo8J57jTEiHgpFbIsj-f6qeBs8x") 
       elif  message.text == "Mist":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1KYuUKn70GMUwJWehEhJdjSEXB2oR6Esj")
       elif  message.text == "Montana":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1CpiUIk3U49oQ4hMVyCqxWTgglfsXliUr")         
       elif  message.text == "Monte Carlo":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1ssnAv0Q0KxmiUEQufIMLbJnOWGkuEQuR")
       elif  message.text == "Monterey":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1NqAGe5nuAvkrx5UXMqhuJfEeEdcJTuHu") 
       elif  message.text == "Natural":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=189OzVG82ay8kci1Ujv1q6w1OpAgNF81D")
       elif  message.text == "New York":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1ad9-3OOSP2f4isw7mkGwXDWk2RWGHTbR")         
       elif  message.text == "Novara":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1HwIF3r4nnrmdjZ1KpqsA2jmfuTNmGUZv")
      
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
      
       elif message.text == "O,P":
         tkaniOP_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniOP_markup.row('Olivia', 'Paola', 'Philadelphia', 'Polo', 'Pure Linen')
         tkaniOP_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniOP_markup)
       elif  message.text == "Olivia":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=13RtCafYZAQO-FvK0XSIycGDK9op4hnhd") 
       elif  message.text == "Paola":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1tA0MCAmG7uGFxZWgOvG7_KgbJpBrHvnc")
       elif  message.text == "Philadelphia":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Cz5BRjGPt2jZ8PnD0_80Ss089zP30j0a")         
       elif  message.text == "Polo":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1DBWP-4EY-eBLNNpRHpKMFwB3nCfI9_OS")
       elif  message.text == "Pure Linen":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1UCoxbv_I3yqNydkO2F9EheyHKJIfoKpi")
        
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)   
         
       elif message.text == "R": 
         tkaniR_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniR_markup.row('Reach', 'Renato', 'Reni', 'Residence')
         tkaniR_markup.row('Riviera', 'Rodos')
         tkaniR_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniR_markup)
       elif  message.text == "Reach":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1rR2Fbp2wtf4-WYce_um9E6BO4ZRoJtS-") 
       elif  message.text == "Renato":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1qz4OuHX9SNlJcBZYF9hLLj2dyCYto8bg")
       elif  message.text == "Reni":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1YQu4QhwTrFGjImEJRHiG5qi8puOjVGid")         
       elif  message.text == "Residence":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1auFOPE9Hy_UB73RKS89iYQjXELXsm7Iu")
       elif  message.text == "Riviera":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1-8gUlQR6CwPVoc7X83cnlRZH4HY-G65B")         
       elif  message.text == "Rodos":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1khnR-gfAAtjyUTbFWmlTnE1w5_Ou2ZI9") 
        
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)     
         
       elif message.text == "S,T":
         tkaniST_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniST_markup.row('Sabina','Shetland', 'Smart', 'Sorrento', 'Swan')
         tkaniST_markup.row('Tiffany','Times','Tokyo','Tweed')
         tkaniST_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniST_markup)
       elif  message.text == "Sabina":
                bot.send_message(message.from_user.id, "https://drive.google.com/file/d/1yRZM0lQIM1RhTkzMlxc1qWteQabeD1-5/view?usp=sharing")
       elif  message.text == "Shetland":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1yxirp5WdwFG6ctmhNMmLkGctAf93AUGP") 
       elif  message.text == "Smart":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1-6GazB7WNTsIQVGrNyZyAiSfbcziqsBu")
       elif  message.text == "Sorrento":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=17ZdT2Zu7CgGbVyb6_F9Rtf7-vf-ifazK")         
       elif  message.text == "Swan":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=197cjrZEJ7yeBC59qsbjj2MGwx9xqaHr_")
       elif  message.text == "Tiffany":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=13nEdG8WpCUpYsXJ7iMavorkfrvUtZ6YD")
       elif  message.text == "Times":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=13nEdG8WpCUpYsXJ7iMavorkfrvUtZ6YD")         
       elif  message.text == "Tokyo":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1ET3gO0ARYJtDnzaJjdrGsh3hRFnJOA97")         
       elif  message.text == "Tweed":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Ih-DxOsIuKArQ26hrGFnUutoyJr4FwzU") 
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "V,W":
         tkaniVW_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniVW_markup.row('Velutto', 'Vera', 'Verona', 'Violett')
         tkaniVW_markup.row('Vito', 'Vitoria', 'Wool')
         tkaniVW_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберете ткань ⬇", reply_markup=tkaniVW_markup)
       elif  message.text == "Velutto":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1M_ocsjXs1Qdhzw-UJ0J-JCCY84lpFaa1") 
       elif  message.text == "Vera":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1GSWQ_nffHQHgnFgfLcOHX85LYK69mp-d")
       elif  message.text == "Verona":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1RIork8N2cEOHEdRvIkd_0cx0UvxE8vO8")        
       elif  message.text == "Violett":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=173lui1UXCDdX3B72vjtz64bDtgjCy3C3")         
       elif  message.text == "Vito":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1sTwCAYU2YHwotnEMcmMiJeJQ2PQLzNT3") 
       elif  message.text == "Vitoria":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1ANKo5tbckMMxz3uVJwBfiUaSbD59olBt")         
       elif  message.text == "Wool":
                bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1Jxmp048sVVfOCZU718ip-_gQ6SY7Tfh9") 
         
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M,N', 'O,P', 'R', 'S,T','V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Выберете каталог, указав его первую букву ⬇", reply_markup=tkani_markup)
         
         #bot.send_message(message.from_user.id,
         #             "Задайте свой вопрос здесь @HelenDaylight")
         

         #keyboard = types.InlineKeyboardMarkup(row_width=3)
         #url_button = types.InlineKeyboardButton(text="Ancona discount",
         #                                       url="https://drive.google.com/open?id=1atBkKXvtfQ2MinOTYjk8e9TnH5k_vqVp")
         #keyboard.add(url_button)
         #url_button = types.InlineKeyboardButton(text="Aria",
         #                                       url="https://drive.google.com/open?id=1QQA05iPsiIcyKR4JhAifi8dBqDyEHymM")
         #keyboard.add(url_button)
         #url_button = types.InlineKeyboardButton(text="Atlanta",
         #                                       url="https://drive.google.com/open?id=1jpJflxr2q41F2ypWoofvwaa_znneW98s")
         #keyboard.add(url_button)
         #url_button = types.InlineKeyboardButton(text="Aurora discount",
         #                                       url="https://drive.google.com/open?id=1QOOH2BtdY5JIplEzVAUCWmzElc6ZA7t6")
         #keyboard.add(url_button)
         #bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  A ", reply_markup=keyboard)
 
        
        
        
        
        
        
       elif message.text == "📚 Suerte mebel":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('📚 Запросить прайс:', '📖 Запрос на наличие', '❓ Задать вопрос')
         manager_markup.row('📲 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
    
       elif message.text == "❓ Задать вопрос":
         bot.send_message(message.from_user.id,
                         "Задайте свой вопрос здесь @HelenDaylight")

       elif message.text == "📚 Запросить прайс:":
         bot.send_message(message.from_user.id,
                         "Отправьте свой e-mail сюда @HelenDaylight")

       elif message.text == "📖 Запрос на наличие":
         skladm_markup = telebot.types.ReplyKeyboardMarkup()
         skladm_markup.row('📚 Suerte', '📚 L1nkstudio')
         skladm_markup.row('⬅ Нaзад') #английская первая а
         bot.send_message(message.from_user.id, "Выберете нужный вам вариант ⬇", reply_markup=skladm_markup)
         
       elif message.text == "📚 Suerte":
           bot.send_message(message.from_user.id, "https://drive.google.com/file/d/1K2S7eQ2eS-5UYyAltnxGx1YaTc_D2LdJ/")

       elif message.text == "📚 L1nkstudio":
           bot.send_message(message.from_user.id, "https://drive.google.com/file/d/1gKR1Y7yUJSVZGHXDRBlGxoZzZi_druIK/view?usp=sharing/")

       elif message.text == "📚 Цены на ткани:":
         catalog_markup = telebot.types.ReplyKeyboardMarkup(True, False)
         catalog_markup.row('Suerte', 'Elegancia')
         catalog_markup.row('Margo', '⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите каталог ⬇", reply_markup=catalog_markup)

       elif message.text == "Suerte":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1JXSkU19DT_eFPFlfKr0B_paIHdDdl2MX")
       elif message.text == "Elegancia":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1cK-A-K619t_dsX8uVcEzmoyWqPByG102")
      # elif message.text == "Iliv":
      #   bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1DeU1C4DM7fkdiv9Yl5B7qxSbZ33zlIGu")
       elif message.text == "Margo":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1D68f0227yf_Jz7aSBp9MDR2vB_8Mn61-")
     #  elif message.text == "FR-One":
     #    bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1qARBc1Vv6e9eMRKeKa4wZajrDrqsOabn")


       elif message.text == "📲 Позвонить в компанию":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('Рук.направления Елена Стеблина', 'Директор', 'Офис менеджер')
         manager_markup.row('Екатерина Бычковская', 'Лилия Пинчук', 'Юлия Липовая','Екатерина Некипелая')
         manager_markup.row('⬅ Нaзад') #английская первая а 
         bot.send_message(message.from_user.id, "Выберите менеджера ⬇", reply_markup=manager_markup)

       elif message.text == "Лилия Пинчук":
         bot.send_message(message.from_user.id, 'Лиля Пинчук\n' +
                'Менеджер отдела продаж\n' +
                '\n' +
                '📱 +38 (067) 405 66 84\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager1@daylight.com.ua ')
       elif message.text == "Юлия Липовая":
         bot.send_message(message.from_user.id, 'Юлия Липовая\n' +
                'менеджер отдела продаж\n' +
                '\n' +
                '📱 +38 (067) 240 12 34\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager2@daylight.com.ua')
       elif message.text == "Екатерина Бычковская":
         bot.send_message(message.from_user.id, 'Екатерина Бычковская \n' +
                'менеджер отдела продаж\n' +
                '\n' +
                '📱 +38 (067) 327 80 81\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager3@daylight.com.ua')
       elif message.text == "Екатерина Некипелая":
         bot.send_message(message.from_user.id, 'Екатерина Некипелая \n' +
                'менеджер отдела продаж\n' +
                '\n' +
                '📱 +38 (067) 564 10 15\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager4@daylight.com.ua')
       elif message.text == "Офис менеджер":
         bot.send_message(message.from_user.id, 'Офис менеджер\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 office-assistant@daylight.com.ua')
       elif message.text == "Рук.направления Елена Стеблина":
         bot.send_message(message.from_user.id, 'Стеблина Елена\n' +
                '\n' +
                '📱 +38 (067) 247 42 22\n' +
                '\n' +
                '📱 +38 (067) 524-59-09\n' +
                '\n' +
                '📧 fibre@daylight.com.ua\n' +
                '\n' +
                '@HelenDaylight')
       elif message.text == "Директор":
         bot.send_message(message.from_user.id, 'Елена Геннадьевна\n' +
                '\n' +
                '📱 +38 (067) 401 32 03\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 director@daylight.com.ua')
       
       elif message.text == "⬅ Нaзад": #английская первая а 
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('📚 Запросить прайс:', '📖 Запрос на наличие', '❓ Задать вопрос')
         manager_markup.row('📲 Позвонить в компанию', '👍 Facebook', '📸 Instagram')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
       
       elif message.text == "⬅ Назад":
        handle_start(message, text=False)

       elif message.text == "👍 Facebook":
        bot.send_message(message.from_user.id, "https://www.facebook.com/suerte.elegancia/?fref=mentions")

       elif message.text == "📸 Instagram":
        bot.send_message(message.from_user.id, "https://www.instagram.com/suerte.elegancia/")

       elif message.text == "⬅ Назад":
        handle_start(message, text=False)
    else:
        bot.send_message(message.from_user.id, 'Для получения доступа к информации, отправьте этот id на телеграм @SuerteSupport, {}, id - {}'
                         .format(message.from_user.first_name, message.from_user.id))

bot.polling(none_stop=True)

