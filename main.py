import telebot
import logging
import random

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) 

# import constans
from telebot import types

bot = telebot.TeleBot('774606011:AAHQzvuc97_YZYevL7LCJMh1tQkHdx3pjbA')
#bot = telebot.TeleBot('620264496:AAGhmkwE_ayuLOGma76CSvfWB8IX1LySMg4') второй бот
users = [410819637, 329546876, 591563627, 513810155, 645413390,922649159,
#        Стеблина   Строменко                ЕГ                , Барабаш
544744166, 514280124, 558012259, 933053790, 301595058, 431874826, 725985865, 596672708,  443286422,  803899880,  727629595, 
# Nikolay  Мельник    Veronika   ДеЛаВега   одесд2     АтельеЛилу Самотохина Воротынцева Bogdanovich Trone       GrandeCube44        
573147939,     906970322,    542536111,805166711,    927139023,                 490528542,934559656,410498438,141083256,   374386376,1153311022,       
#КостенкоОльга,Steblinaxiaomi,Hanna,    ОшманинаИрина,ЕленаГородничаяШикНиколаев,Hommie,  Старинец, MaxIT,    НастяРыжийКот,Турик,   СеменоваИ.      
793089330,  531553285,  856420893, 525598059, 1121853974,  276667391, 914587344,   802459626, 517822953, 748026571,     835950936,  633195004,         
#ДуденкоН., ШевченкоИ.,  ИринаSh,  КаспрукН., БеличенкоА., ШевцоваК., Бухаловская, Турик2,    Батист,    ДекорейшнКиїв, ЦапокИнна,  СалашНина   
807308376,   803452035,               223508200,989253411, 818569405, 909583342,   538382824,521140981,1265568714,466829080,1071975476,942458930,      
#БойчукЕлена,ОльгаМаковская/Структуре,Шторград,АлтунинаТ.,ЛораМаэстро,ДаринаМаэстро, Приемова,ГизаЛена, Озерова,  СкороходК,СкороходЛ, ЕвтушенкоН    
751880788,  510451786,  668394665,  711128851,  477861785,  468033104, 1038064476, 411467807,   268056638,     282970170, 487632083, 1114816841,      
#Грайпоинт, БарибаАнна, АртуэльМарина, Мыцык,     ТкачукТ,   ТкачукВ,  Самотохина, ДемьянМороз, ТюльпанМарина, Ньюволл,   Донская,   СавельеваИрина 
1119983052 ,     764883981,  1181396737,914166356,666165868,    441937522, 849951686, 761328878,  1017341255, 701264921,   1179091466, 914166356,      
#ДаринаГоловкина,ШелеяСветлана,Федорец, ЧумакЛеся,СухоруковаАнна,Artemida, Бельэтаж,  БелоусоваТ, ЯнаБекетова,K.O.R.ADesign,VGInterior,ЛесяЧумак
1277803311,   975495600,  1362656180,    901739410,    900481908,   389641524,    532517776,   715466005,    901739410,   560912405,    896310777,    
#КалинаНинаИ, КалинаИрина, АленаРосетти, ИринаМаэстро, АнжеликаХар, МялковскаяЮля,ШпортунОльга,НилаХарківШР,МаэстроИрина,БергманЛариса,КаштанАнна,    
436679970, 423012979,    1070269781,  290137143,  458130014,   907218362, 260590376, 589700747, 628131677,    465354836, 1060987866,    399377643,    
#магнитЮля,Галянастарчук,ДисаслеЕлена,ТкаличНастя,Гайворонская,Дуденко,   Фиранка,   ДроботС,   АлинаМаэстро, Зудина,    АртельМаркова, ХайменоваЕкат 
355185570,   366240022,  617929990, 984185462,  982702076,  561725836,   309697506,       674698133, 1399983833, 900315030, 476800911,379202773,   
#МаксимДубл, Сингаевская,ГнездоОля, ДаниленкоТ, Батист,     КрушевскаяН, ПриваловаСвМанеж,Нюанс,     Нюанс,      Галран,    Жарникова, Шишлачева 
394424128,     625176973,  1384882453, 676543691,  625176973,      272177628,1394344523,1147669472,696611370,853217074,     1039630690,     
#СтеллаБровары, ОльгаПопова, Прованс,  МарченкоЛ., ОльгаТвКимХарьк,Думитрук, Литом,     ЛитомИра,  Авесоль,  БаровскаяЛиля, АннаКинзерская,
1014753974,494619796, 466510262,    1202718965,       818569405,  233796308,             429168251,         792774683,488261313,649147906,610167809,   
# Хомми,   НаяДизайн, ЗахаренкоОля, НадяНовыйПростир, ЛарисаН.П., ОксанаСансара(МирПола),ЖеняСтарченко(Беркович),ДианаЛена,Лианна,ЮляШкребтий,Олена, 
760342877,         502291018,      1370525794,599758620,583827920,         1240388984,782486934, 488802242,  698582654,      14592351,               
#ОльгПримаЛаурэль, ИринаЖилинская, Аллаткач, ГодованаО, НатальяотГодованой, Еленаэфес,ДилияДомио,ЕленаДомио, AleksandraДомио, ИнсайтYuliyaSkobletska,  
533005935,       765615424,     219627801,  632281856,     190086956,               899668417,     685767776,  622906331,    899007965,  
#ТищенкоЛюдмила  ГалереяВиарди  Allagio     ИнсайтNatalia, RayНиколаевМебельШикАня, ЛучкоСветлана, МомотАлеся, ЮлияЗахарова, ШторыЛюкс
531287510, 706720454,  834263729,  160366076,  909543137, 561647142, 834263729,    566069039,  455950277, 1212826764, 411628179,        995506134,
#Артфешн,  ТаяМандерс, Рыбалко,    Москаленко, НаяТаня,   НаяАня     ДорнумАндрей, Васильева,  Рыбак,     Давиденко,  БроневичеваДонум, ГалинаГлянц, 
119050642, 777703251,     807587277,    1391383316, 1164610600,   1376870611,     1323866597, 1125309812,     617029686,959015548,917403108,1079325718,
#Глянц,    КсенияЯворская,AlenaЯворская,ГалереяВиарди,Жаккард,GalereyaDecoraЯкуба,ВашИнтерьер,ЛюдмилаДримХаус,ШевчукИлона,Эксклюзив,АМВ,Homefashion, 
865193195,     705536620,617847354,791102868,    1180587203,460845971, 502291018,    612896485,   670529200,     933292102,   1044073420,284361853, 
#ТатьянаХайтек,АлинаХайтек,Ришелье,ФридомНаталья,ЛифарьКатя,ФридомКсю,ЖилинскаяИрина,ИринаРосетти,ТимченкоЛариса,КсенияКошевая,Оксанабух,МарченкоВадим 
160366076,     860433209,    680907645,1055068234,    1385451015, 744800267,        467883820, 452714070, 483233642,  762398556, 130963117, 408547766,
#МоскаленкоЮля,БаригинаИрина,ГораАлла, БычковскаяКатя,VGInterior, ПарижанкаХарків, КучмаНадя, ШарайЛена, Прованс,    Альберо,   Подлесных, СитькоМария
996486894,    976183910,          412673589,   500400928,802250129,49057996,           853993240,740609988,  1005972951, 976540102,  976183910,
#ОсауленкоТаня,СветланаСалонДиана,МарченкоЛюба,Ричхаус,  Ричхаус2, СтайлИнтерьерУльяна,DeGarni,  JustВиктория,AnnaСерго1,NinaСерго2, СветланаБондарь
750424993,    593994710,615493643,688733497,     533853999,273686638, 1109162091,   838499606,    871340761,    752944714,  869047189, 895672692,
#БроварыСтудио,ЯнаЛысак,ДенисШевченко,Даша Кориневич,Цвиркун,   ЛИлу,   МаэстроМарина,ЧерноволоваЛ.,ДеГарниМенеджер2,Dizzroom,  4room,     Чупаха
779447053,   555880439,           356244555,           555880439,            534296286, 453984948,     452140580,   610837741,357608995,  415221499,
#ДианаМыцык, КристинаНовийПростир,Violet17НовийПростир,НовыйпростирКристина, Теламор,   ФедорецНаталья,ФедорецЕлена,АленаЭтюд,ЛюдаГурина, Вартанова
345856716,   648602894,     574100509, 670314877,      761964930,      374364745,   895672692,   1871511483,   
#ЖардисЮлия, АндриенкоЯнина,Бруни,     СветланаМусиюк  Кучма,   Настасьясекретарь,   Чупаха,   Cерго,   ElenaSerdechenko,  
374364745,   359817732,      677388984,      197500624,   1084121634,442272295,505739103,963160070,349692808, 
#НастяСекрет, AnnaДомилСалон,ЗояМаэстроСалон,РитаЧепурина,Меделян,  ГардинияБЦ,AMB1,     AMB2,      Liumanova,  
1037837682,   798399875,  748636866,         1058515068, 533341338,   543238146,      1459262789,   526855240,   981735213,     543799429, 
#ЮляМенедДЛ,   Некипелая, КристинаГоловкина, БорисоваТ,  Декорейшнклаб,Декорейшн клаб2, Afiny,   ИвановаТатьяна,  ИннаЛаврукова,ГригоренкоЕлена,
671713873,   917403108,   981735213,   533005935, 671713873, 44584316,   740703024,   863338389,   637783523,     522697316,   970713832,
#Юля,   ТаняАМВ,   Іванова Тетяна,   ЮляІнсайт,   Vecta Deco,Vano,   КсеніяДаринок,   Калініна,  АннаВасильченко,  МаріяЗахарченко,   ГалінаЗахарченко,
1499901889,   786363009,  1309963836, 1163049072,    1171129587,        544833688,   852761908,720946164,               1032489831,   527672135,
#Ірина,       Сергій,      Альберт,   НагорнаяИрина, КовалекскаяМарина, Nazar Voznyy, Lusori,  ІовенкоОльгаСалоншторАВС,  ОленаБатурська,   BasonOlena,
562393351,   545236603,   1708290601,   724365284,   411727329,   1383648095,   548389510,   636662342,   571021587,  100159895,   1896751197,
#Сакелари,   ІмперіяЛариса,   ІмперіяІра,   Oblyvach,   DovgalTetana,   Алла,   Анісімова,   КатеринаМеланж,   Вахрушева,  Місіва,   Тугушева,
285200434,   324285219,   650887991,   650887991,   100582532,   1131698120,   511855639,   1238624852,   1343343289,  471376062,    591368807,
#Романюк Виктория,   ОльгаГорголь,   СвітланаМірт,   МіртСвітлана,   КраляОля,   ІринаГора,   Сильд,   КатеринаТерем,   Терем Одеса,  ГалінаГалючек,   Крістіна Тугуд,
579320945,   673179779,   702545736,   977921795,     501531880,     1257806310,   615310872,            1872870826,  1030457606, 711050317,
#Barcelona,   КошкінДом,  МаестроАлина,ГубенкоОксана,   АллаТіхонова, ВиженМаргарита,МирославаИваноФранк,Каминская,   Гессо,      ГессоВиктория,
1523859607,        108516274,   561089532,     1744364869,             472672120,   811028535,   1499901889,  639161144,   711050317, 1360961804,
#PerfectIнтерессалон, IнтересАнна, АннаЛюбенько, ТатьянаГармонияСтилей,РозмайАлена ,МарьянаЧеркез ,ГалеряДекоруІрина, Стайл Декор, ViktoriaKrotenko, Atmosfera,
382830775,   866060096,     1100095385,  561345133,   1605174319,1240479647,  469929271,   3616484331, 538498920, 1171129587, 723983854, 1848692380, 1945073424, 1061822043, 796441610, 911681086, 494622405,  816815356, 469507833, 1163049072, 
887321858,
#ЕвсеєваЯна, ElenaLisitsya, ElenaKostina,ЕвгеніяАртіс,ЕленаАртіс,СвiтланаIнтерiо, ІннаОсадча, АльонаСолонуха,  ІринаОдеса, МаріяКоваленвська , Шляхтун Сергій,  МагіяШторОдеса, ШестакБровары, ВеронаОдеса,  Швецмарина,   КрамаренкоАнна,   ЛисенкоНаталя, ВалеріяАрдіхаус, Заброцька,   НагорнаІрина, БезуглаВікторія, 
529585946,   1112456743,     494797403,    1314361182,     515683740,   952931628,      773934549,440498539, 933145828,      496175640, 
#ДианаПаноСтудия, ШевцоваКатя, ОльгаУсевич, ЛаурельАйгуль, ОльгаКарпова,ОльгаБелозерова,Poptsova, Кирил ,    НикитинаТатьяна,СофаКонцептЛьвівТатьяна
600530601,   1390780323,     493000409, 574361077, 553790745,       696554978,       1803608206,    620581882,     402158989, 
#Анастасия,  LesyaSmarovoz,  Салецька, Резнікова,  МерксГусакАнна,  СітіусКатерина,  NuancePolko,   МаестроПоліна, VeronaOdessa(KonevaNatalia), 000000,
756617340,   874375384, 1242251918, 925153884,   1495960256, 1984195362, 836372196, 2057004174, 1530802506, 591022919,
#мандерс, НстудияКР,ОлександраАрдіхаус,Мандерс1,  МаэстроКрасноармЛюбаДизайнер,  Харахаш, Анісімова, ОльгаЗеген, ЮліяЗеген, ДекорЛюкс
330706886,   1479734168, 330706886, 671115542, 706006421,  913054175,  2051078593,   981314316,    1819446380, 264690469, 1186589926, 
#Мінор,      DLS,        Jenya,     ІринаАлсер,Стронова,   Алсер,      ІринаМаестро, ТетянаМаестро, Gardis, Le maison de Garny, марінаMebItal, 
506950652,   1675910258, 1361086987,505518594, 677279305,  1602793411,  1307045126,   2098486901, 539238658, 1058345320, 672362515, 703769371,
#Алла Тімофеєва,Shapoval,Patratiy,ОленаМандерс,   AnoschenkoTetyana,  Жартіс,  DLS,   Мінорі,ІннаЕфір , ОстапенкоТатьяна, Думітрук, ІринаМарініч, Шелея,
911681086,   533690029,  739941051, 397170813, 508819971, 100159895, 840238815,  703769371, 5022240912, 283633260, 710913938, 830874823,366325727,789643601,414190336, 641837284, 895709040, 1540332817, 547405859, 810448909, 1259410473, 677048178, 650085449,  1411651650, 408483065,
#Крамаренко,ІринаПомайда, Мандерс,   Маестро,   Маріна,   Шторград, МорозОксана, мандерс,    Дімолі,     ДаВінчі, Своєрідне, ТаняДейлайт, Komisaruk, ЛесСтрорес, Лессторес, Villagio, БойкоІнна, Світлана, ЕкатеринаМельник, Штори, Дегарни, ОленаГончаренко, Woodsoft, Манеж,
361648431,      425176227,  332979051, 1410386986,  671540342,    5214964625,     629448042, 461473179, 385947998, 5427338717,
#AlonaSolonukha,OliaBudziak,Гачаева, ЛюдмилаБандура,АняАтрощенко, AnastasiaGuzhva,PROSHTOR,  Olena  ,   Гололобова, МагияШтор,
5427338717, 539883822,               5050187427, 399938284,     670529200,    1085532123,  711128851,    309840552,    1152294314, 863338389,
#МагияШтор, JUSTdesignВишгород/Київ, ElenaSubota,КрасовскаяЛена,ТимченкоЛора, ЕленаМаякова, ЛюдмилаМицик,МаэстроПолина,AnnaFreedom,НаталиКалинина,
498309140,   1971239381,  1375265917,      1280819722,                  1173742908,   432391086,  657948670,       582939793,    998025685,
#АлесяАлсер, GarniShtoru, ЛюдмилаDLSмебель, СПДМорозДем'янВолодимирович,ГончарЛюдмила,InnaZalivan,FirgankaUzhgorod,НаталяМаєстро,Valeriia
5102862102,    1983271322,      540183463 , 471180855, 580966498,        5182002644,                 643878911,             595588001,
#OlesyaІнсайт, СвітланаМірПола, Коломієц,   МудраяЮля, RozaBerilishvili, СофвКонцептЛьвовГрейсМебель,ГардиныДримТаунГубенко,NataliPanamarchyk
960880893,      307286419,   552866757,    420360416,  1347607488, 1219653499,     511906590,    1957870191,             
#ВелікдусНаталя,АннаТекстіль,ТетянаГоловко,ElenaGrisha,МебельИрина,TanyaMoskalenko,NadiyaPoltava,АктуальТекстильныйДекор,
5509180212,                       874217255,   598132309,5158607703,5951156317,    106217157,     276435486,
#СалонТвояКiмнатаБровичеваТатьяна,НаталияБурдух,ЮляАлсер,ЮляАлсер,  СтеблинаНовый, АрдихаусЕлена, ВікторіяРолетиЧеркаси
186427769,            5916477090,    1769987580,  372196963,                427884040,           1781875476,  5427338717,
#OleksandraPryadkina, HelenSteblina, Starinets, ЖаннаІвашкевічЖаннаЛіненс, МаэстроВасильковская, Лариса,      МагіяШтор, 
34526008,       312374389,   308573542,         766834044,          500612134,   949552350,540212616,     889943119,  2036746453,
#СергійWoodsun, woodsunНастя, KintBureauМаксим, МаестроЛобановськог,ProproБогдан,ОленаЕтюд,НаталіМірПола, ЮляМірПола, КітасВалентина
488257552,         1660610118, 1739894705,  665920385,1144959202,   833890428, 856420893,         1470473327,541521366,
#СашаПрограміст1С, КостінаЮля, МазурИрина, АннаГавриш,АртемДумітрук,ЮляМаестро,ШевченкоІринаОдеса,LesStores,  MytaHome
541521366, 5522669246,   699577984,  911681086, 494049699,5418620671,        653539467,            00000000000,00000000000]
#MytaHome, АкварельХарків,МомотЛеся ,Краманенко,ОленаНая, ОксанаГрейсЧеркаси,НаталіяРибченкоАлсер, 0000000000000,  00000000000

@bot.message_handler(commands=['start'])

def handle_start(message, text=True):
    if message.from_user.id in users:
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('📚 Suerte collection', '📚 Suerte mebel')
        #user_markup.row('📚 Прайс.Завантажити:', '📖 Запрос на наличие Suerte', '❓ Запитати')
        #user_markup.row('📞 Подзвонити в компанію', '👍 Facebook', '📸 Instagram')
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
       if message.text == "📚 Suerte collection":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Прайc', ' 📥 Наявність на складі на складе', '📢   Запитати по Suerte' )
         manager_markup.row('📞 Подзвонити в компанію','💶💵курс','👍📸🌐 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
        
       elif message.text == "🔎 Прайc":
         bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/1gXRc6xPUmX4dNPvNfvC7leIifBUlNvEJ7-L-QzEdnh0/view",
           disable_web_page_preview = True)
       #elif message.text == "🔎 Прайc":
       #  keyboard = types.InlineKeyboardMarkup()
       #  url_button = types.InlineKeyboardButton(text="Нажмите чтобы перейти на прайс-лист",
       #                                         url="https://docs.google.com/spreadsheets/d/eIifBUlNvEJ7-L-QzEdnh0/edit#gid=1265136000")
       #  keyboard.add(url_button)
       #  bot.send_message(message.chat.id, 'sss', reply_markup=keyboard)



       elif message.text == "📢   Запитати по Suerte":
         bot.send_message(message.from_user.id, "Напишіть своє питання в телеграм @Suertesupport")
         log(message)
       elif message.text == "📞 Подзвонити в компанію":
         phone_markup = telebot.types.ReplyKeyboardMarkup(True, False)
         phone_markup.row('Клієнт менеджери', 'Регіональна менеджери по городам', 'Бренд менеджери')
         phone_markup.row('Офіс менеджер', 'Гаряча лінія директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup)
        
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Прайc', ' 📥 Наявність на складі на складе', '📢   Запитати по Suerte' )
         manager_markup.row('📞 Подзвонити в компанію','💶💵курс','👍📸🌐 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
       
       elif message.text == "📥 Наявність на складі на складе":
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Колекція Suerte', '📚 L1nkstudio', '📚 Outlet')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=sklad_markup)
        
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Прайc', ' 📥 Наявність на складі на складе', '📢   Запитати по Suerte' )
         manager_markup.row('📞 Подзвонити в компанію','💶💵курс','👍📸🌐 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
    
       elif message.text == "💶💵курс":
         bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/rate1C.txt",
         disable_web_page_preview = True)
                         
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Прайc', ' 📥 Наявність на складі на складе', '📢   Запитати по Suerte' )
         manager_markup.row('📞 Подзвонити в компанію','💶💵курс','👍📸🌐 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
       
       elif message.text == "👍📸🌐 Соц. мережі":
         socnet_markup = telebot.types.ReplyKeyboardMarkup()
         socnet_markup.row('👍 Facebook', '📸 Instagram', '🌐 Сайт')
         socnet_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=socnet_markup)
       
       elif message.text == "↩Назад":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('🔎 Прайc', ' 📥 Наявність на складі на складе', '📢   Запитати по Suerte' )
         manager_markup.row('📞 Подзвонити в компанію','💶💵курс','👍📸🌐 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)

       elif message.text == "Гаряча лінія директора":
         bot.send_message(message.from_user.id, 'Олена Геннадіївна\n' +
                '\n' +
                '📱 +38 (067) 401 32 03\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 director@daylight.com.ua')
       
       elif message.text == "Клієнт менеджери":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Юлія Липова', 'Марія Петренко')
         phone_markup.row('Катерина Некипіла', 'Юлія Костенко')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup)   
         
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клієнт менеджери', 'Регіональна менеджери по городам', 'Бренд менеджери')
         phone_markup.row('Офіс менеджер', 'Гаряча лінія директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup) 
           
                
       elif message.text == "Регіональна менеджери по городам":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Київ', 'Харків', 'Львів')
         phone_markup.row('Дніпро', 'Одеса')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup)   
        
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клієнт менеджери', 'Регіональна менеджери по городам', 'Бренд менеджери')
         phone_markup.row('Офіс менеджер', 'Гаряча лінія директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup) 
        
         
       elif message.text == "Київ":
         bot.send_message(message.from_user.id, 'Світлана Турик\n' +
                '\n' +
                '📱 +38 (067) 445 32 05\n' +
                '\n' +
                '☎ +38 (044) 545 60 70\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 tur@daylight.com.ua')
         bot.send_message(message.chat.id, 'Шевцова Катерина \n ' +
                 '\n'
                 '📱   +38 (067) 564 41 09 \n' +
                 '\n'
                 '☎️  +38 (044) 545 60 70 \n' +
                 '\n'
                 '📧 suerte2@daylight.com.ua \n' +
                 '\n'
                  , )
       elif message.text == "Харків":
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
       elif message.text == "Львів":
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
       elif message.text == "Дніпро":
         bot.send_message(message.chat.id, 'Дуденко Наталья \n ' +
                         '\n'
                         '📱   +38 (067) 450 00 79  \n' +
                         '\n'
                         '☎️  +38 (099)401 36 16  \n' +
                         '\n'
                         '📧 dneprdl@daylight.com.ua \n' +
                         '\n'
                         )
       elif message.text == "Одеса":
        bot.send_message(message.chat.id, 'Шевцова Катерина \n ' +
                                                '\n'
                         '📱   +38 (067) 564 41 09 \n' +
                         '\n'
                         '☎️  +38 (044) 545 60 70  \n' +
                         '\n'
                         '📧 suerte2@daylight.com.ua  \n' +
                         '\n'
                         )
         
       elif message.text == "Бренд менеджери":
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Suerte', 'FR One Margo Iliv', 'Suerte mebel, Link Studio, Adora')
         phone_markup.row('↩Нaзад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup)           
         
       elif message.text == "↩Нaзад": #английская первая буква а в слове Назад
         phone_markup = telebot.types.ReplyKeyboardMarkup()
         phone_markup.row('Клієнт менеджери', 'Регіональна менеджери по городам', 'Бренд менеджери')
         phone_markup.row('Офіс менеджер', 'Гаряча лінія директора')
         phone_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=phone_markup) 
                
       elif message.text == "Suerte":
         bot.send_message(message.chat.id, 'Старинець Наталя  \n ' +
                         '\n'
                         'менеджер відділу продажів \n '
                         +
                         '\n'
                         '📱   +38(067) 405-66-74 \n' +
                         '\n'
                         '☎️@TelegramStarinets \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
                
       elif message.text == "FR One Margo Iliv":
           bot.send_message(message.chat.id, 'Самотохіна Олена \n ' +
                         '\n'
                         'менеджер відділу продажів \n '
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
                
                
       elif message.text == "📚 Колекція Suerte":
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Hазад') #английская буква H
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "↩Hазад": #английская буква H
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Колекція Suerte', '📚 L1nkstudio','📚 Outlet')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=sklad_markup)
         
       elif message.text == "📥 Наявність на складі на складе":
         sklad_markup = telebot.types.ReplyKeyboardMarkup()
         sklad_markup.row('📚 Колекція Suerte', '📚 L1nkstudio','📚 Outlet')
         sklad_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=sklad_markup)
         
       
       elif message.text == "A":
         tkaniA_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniA_markup.row('Atlanta', 'Ashley')
         tkaniA_markup.row('↩Назaд')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniA_markup)
       elif  message.text == "Atlanta":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Atlanta.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Ashley":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Ashley.pdf",
                disable_web_page_preview = True)       
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         #1111tkani_markup.row('↩Назад')
         tkani_markup.row('↩Hазад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "B":
         tkaniB_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniB_markup.row('Bamboo', 'Bavaria','Bergamo')
         tkaniB_markup.row('Bianca','Boston','Braveheart','Brooklyn')
         tkaniB_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniB_markup)
       elif  message.text == "Bavaria":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Bavaria.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Bamboo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Bamboo.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Beatrice":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Beatrice.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Bergamo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Bergamo.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Bianca":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Bianca.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Boston":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Boston.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Braveheart":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Braveheart.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Brooklyn":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Brookyn.pdf",
                disable_web_page_preview = True)                
      
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "C,D": 
         tkaniCD_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniCD_markup.row('Calista', 'Celine', 'Chalet')
         tkaniCD_markup.row('Chelsea','Chicago','Choice')
         tkaniCD_markup.row('Convoy','Crystal','Dallas')
         tkaniCD_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniCD_markup)
       elif  message.text == "Calista":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Calista.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Celine":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Celine.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Chelsea":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Chelsea.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Chalet":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Chalet.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Chicago":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Chicago.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Choice":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Choice.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Convoy":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Convoy.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Crystal":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Crystal.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Dallas":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Dallas.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Diamante":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Diamante.pdf",
                disable_web_page_preview = True)   
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "E,F,G": 
         tkaniEFG_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniEFG_markup.row('Elegante', 'Feliche', 'Florence', )
         tkaniEFG_markup.row('Fuji dim-out','Ford','Galaxy','Gentleman')
         tkaniEFG_markup.row( 'Grace', 'Garden','Greenwich blackout')
         tkaniEFG_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniEFG_markup)
       elif  message.text == "Elegante":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Elegant.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Feliche":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Feliche.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Florence":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Florence.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Fuji dim-out":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Fuji.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Ford":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Ford_el.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Galaxy":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Galaxy.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Gentleman":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Gentleman.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Georgia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Georgia.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Grace":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Grace.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Garden":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Garden_collection.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Greenwich blackout":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Greenwich_black_out.pdf",
                disable_web_page_preview = True)          

       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "H,I,J": 
         tkaniHIJ_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniHIJ_markup.row('Houston', 'Hugo')
         tkaniHIJ_markup.row('Isabella', 'Janett')
         tkaniHIJ_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniHIJ_markup)
       elif  message.text == "Historia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Historia.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Houston":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Houston.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Hugo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Hugo.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Isabella":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Isabella.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Janett":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Janett.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Journal":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Journal.pdf",
                disable_web_page_preview = True)
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "L": 
         tkaniL_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniL_markup.row('Linen Story', 'Lluvia', 'Lion', 'Lure trevira')
         tkaniL_markup.row('Light Linen')
         tkaniL_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniL_markup)
       elif  message.text == "Linen Story":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/LinenStory.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Lluvia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Lluvia.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Lion":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Lion.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Loreto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Loreto.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Lure trevira":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Lure_Trevira.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Light Linen":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Light_Linen.pdf",
                disable_web_page_preview = True) 
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
         
       elif message.text == "M":
         tkaniMN_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniMN_markup.row('Malta','Marble','Melanie')
         tkaniMN_markup.row('Michelle','Montana', 'Monte Carlo' )
         tkaniMN_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniMN_markup)
       elif  message.text == "Malta":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Malta.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Marble":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Marble.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Melanie":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Melanie.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Michelle":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Michelle.pdf",
                disable_web_page_preview = True)                  
       elif  message.text == "Millenium":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Millenium.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Mist":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mist.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Montana":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Montana.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Monte Carlo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Monte_Carlo.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Monterey":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Monterey.pdf",
                disable_web_page_preview = True) 
             
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
      
       elif message.text == "N,O,P":
         tkaniNOP_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniNOP_markup.row('Natural', 'New York', 'Novara')
         tkaniNOP_markup.row('Olivia', 'Oprah', 'Paola')
         tkaniNOP_markup.row('Pearl', 'Polo', 'Pure Linen', 'Prado')
         tkaniNOP_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniNOP_markup)
       elif  message.text == "Natural":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Natural.pdf",
                disable_web_page_preview = True)
       elif  message.text == "New York":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/New_York_hanger.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Novara":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Novara.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Olivia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Olivia.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Oprah":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Oprah.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Paola":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Paola.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Pearl":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Pearl.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Philadelphia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Philadelphia.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Polo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Polo.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Pure Linen":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Pure_Linen.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Prado":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Prado.pdf",
                disable_web_page_preview = True)

       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)   
         
       elif message.text == "R": 
         tkaniR_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniR_markup.row('Reach', 'Reni', 'Residence','Richmond')
         tkaniR_markup.row('Riverside dim out M1','Riverside lining fabric M1')
         tkaniR_markup.row('Riviera', 'Rodos','Ruby')
         tkaniR_markup.row('Roissy 360cm','Roissy 420cm', 'Renato')
         tkaniR_markup.row('↩Назaд') #английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniR_markup)
       elif  message.text == "Reach":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Reach.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Reni":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Reni.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Residence":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Residence.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Richmond":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Richmond.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Riverside dim out M1":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Riverside_dim_out_M1_el.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Riverside lining fabric M1":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Riverside_lining_fabric_M1_el.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Riviera":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Riviera.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Rodos":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Rodos.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Roissy 360cm":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Roissy360.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Roissy 420cm":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Roissy_420.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Ruby":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Ruby.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Renato":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Renato_Dallas.pdf",
                disable_web_page_preview = True)        
        
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)     
         
       elif message.text == "S,T":
         tkaniST_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniST_markup.row('Sabina','SantaCruze','Sappho','Sсandi')
         tkaniST_markup.row('Shetland','Shine','Smart','Sorrento')
         tkaniST_markup.row('Space', 'Sunshine print', 'Swan','Tiffany')
         tkaniST_markup.row('Times','Tokyo','Toronto','Tweed')
         tkaniST_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniST_markup)
       elif  message.text == "Sabina":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Sabina.pdf",
                disable_web_page_preview = True)
       elif  message.text == "SantaCruze":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/SantaCruz.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Sappho":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Sappho.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Sсandi":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Scandi.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Shetland":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Shetland.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Shine":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Shine.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Smart":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Smart.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Sorrento":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Sorrento.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Space":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Space.pdf",
                disable_web_page_preview = True)   
       elif  message.text == "Sunshine print":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Sunshineprint.pdf", 
                disable_web_page_preview = True)       
       elif  message.text == "Swan":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Swan.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Tiffany":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Tiffany.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Times":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Times.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Tokyo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Tokyo.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Toronto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Toronto.pdf", 
                disable_web_page_preview = True)         
       elif  message.text == "Tweed":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Tweed.pdf",
                disable_web_page_preview = True) 
       
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
       
       elif message.text == "U,V,W":
         tkaniVW_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniVW_markup.row('Urban','Vegas','Valencia', 'Vera')
         tkaniVW_markup.row('Verona','Violett','Vito', 'Vitoria')
         tkaniVW_markup.row('Volume','Voyage','Wool')
         tkaniVW_markup.row('↩Назaд')#английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniVW_markup)
       elif  message.text == "Urban":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Urban.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Vegas":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Vegas.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Valencia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Valencia.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Velutto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Velutto.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Vera":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Vera.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Verona":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Verona.pdf",
                disable_web_page_preview = True)        
       elif  message.text == "Violett":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Violett.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Vito":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Vito.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Vitoria":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Vitoria.pdf",
                disable_web_page_preview = True)   
       elif  message.text == "Volume":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Volume.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Voyage":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Voyage.pdf",
                disable_web_page_preview = True)               
       elif  message.text == "Wool":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Wool.pdf",
                disable_web_page_preview = True) 
         
       elif message.text == "↩Назaд": #английская вторая буква а в слове Назад
         tkani_markup = telebot.types.ReplyKeyboardMarkup()
         tkani_markup.row('A', 'B', 'C,D', 'E,F,G','H,I,J','L')
         tkani_markup.row('M', 'N,O,P', 'R', 'S,T','U,V,W')
         tkani_markup.row('↩Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=tkani_markup)
         
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
 
        
        
        
       elif message.text == "📚 Outlet":
         outlet_markup = telebot.types.ReplyKeyboardMarkup()
         outlet_markup.row('A,B,C', 'D,E,G,J', 'L,M')
         outlet_markup.row('P,R', 'S,T,U', 'V')
         outlet_markup.row('↩Hазад') #английская буква H
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=outlet_markup) 

       elif message.text == "A,B,C":
         tkaniABC_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniABC_markup.row('Aria', 'Aurora')
         tkaniABC_markup.row('Beatrice', 'Capri')
         tkaniABC_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniABC_markup)
       elif  message.text == "Ancona":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Ancona.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Aria":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Aria.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Aurora":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Aurora.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Beatrice":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Beatriche.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Charlotta":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Charlotta.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Capri":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Capri.pdf",
                disable_web_page_preview = True)  
        
       elif message.text == "D,E,G,J":
         tkaniDEGJ_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniDEGJ_markup.row('Diamante', 'Egipto')
         tkaniDEGJ_markup.row('Eleonora plaine', 'Journal')
         tkaniDEGJ_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniDEGJ_markup)
       elif  message.text == "Diamante":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Diamante.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Egipto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Egipto.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Eleonora plaine":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Eleonor_plain.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Georgia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Georgia.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Journal":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Journal.pdf",
                disable_web_page_preview = True)  

       elif message.text == "L,M":
         tkaniLM_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniLM_markup.row('Loreto', 'Millenium', 'Mist')
         tkaniLM_markup.row('Monterey', 'Mossy Damask')
         tkaniLM_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniLM_markup)
       elif  message.text == "Loreto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Loreto.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Millenium":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Millenium.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Mist":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mist.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Monterey":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Monterey.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Mossy Damask":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mossy_Damask.pdf",
                disable_web_page_preview = True)   

       elif message.text == "P,R":
         tkaniPR_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniPR_markup.row('Philadelphia', 'Prato', 'Piramide')
         tkaniPR_markup.row('Renato', 'Rimini')
         tkaniPR_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniPR_markup)
       elif  message.text == "Philadelphia":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Philadelphia.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Prato":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Prato.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Piramide":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Piramide.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Renato":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Renato-Dallas.pdf",
                disable_web_page_preview = True)  
       elif  message.text == "Rimini":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Rimini.pdf",
                disable_web_page_preview = True)                    
        
       elif message.text == "S,T,U":
         tkaniSTU_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniSTU_markup.row('Shamina', 'Sorrento', 'Toskana')
         tkaniSTU_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniSTU_markup)
       elif  message.text == "Shamina":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Shamina.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Sorrento":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Sorrento.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Toskana":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Toskana.pdf",
                disable_web_page_preview = True)         
       
       elif message.text == "V":
         tkaniV_markup = telebot.types.ReplyKeyboardMarkup()
         tkaniV_markup.row('Valetta Polo', 'Valetta Max ')
         tkaniV_markup.row('Velutto')
         tkaniV_markup.row('↩Назaд.')# английская вторая буква а в слове Назад
         bot.send_message(message.from_user.id, "Выберите ткань ⬇", reply_markup=tkaniV_markup)
       elif  message.text == "Valetta Polo":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Valleta_Polo.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Valetta Max ":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Valetta_Max.pdf",
                disable_web_page_preview = True)
       elif  message.text == "Velutto":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Velutto.pdf",
                disable_web_page_preview = True)         
       elif  message.text == "Vito":
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Vito.pdf",
                disable_web_page_preview = True)  
       elif message.text == "↩Назaд.": #английская вторая буква а в слове Назад
         outlet_markup = telebot.types.ReplyKeyboardMarkup()
         outlet_markup.row('A,B,C', 'D,E,G,J', 'L,M')
         outlet_markup.row('P,R', 'S,T,U', 'V')
         outlet_markup.row('↩Hазад') #английская буква H
         bot.send_message(message.from_user.id, "Виберіть каталог, вказавши його першу букву ⬇", reply_markup=outlet_markup)
      
       elif message.text == "📚 Suerte mebel":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('📚 Прайс.Завантажити:', '📖 Наявність на складі', '❓ Запитати')
         manager_markup.row('📲 Подзвонити в компанію', '💶💵курс', '👍📸 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
    
       elif message.text == "❓ Запитати":
         bot.send_message(message.from_user.id,
                         "Напишіть мені на телеграм @HelenDaylight")

       elif message.text == "📚 Прайс.Завантажити:":
         bot.send_message(message.from_user.id,
                         "https://docs.google.com/spreadsheets/d/14QrnU5nEOEQ-j0A72iNQ-ptDMqFoOldwbGHwjkKrPBI/edit#gid=1844905856")

       elif message.text == "📖 Наявність на складі":
         skladm_markup = telebot.types.ReplyKeyboardMarkup()
         skladm_markup.row('📚 Suerte', '📚 L1nkstudio')
         skladm_markup.row('⬅ Нaзад') #английская первая а
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=skladm_markup)
         
       #elif message.text == "📚 Suerte":
       #    bot.send_message(message.from_user.id, "https://drive.google.com/file/d/12kVC7pWGxq4ffHm4ypqlp_XqKp0ERoMc/view?usp=sharing",
       #    disable_web_page_preview = True)

       elif message.text == "📚 Suerte":
         catalog_markup = telebot.types.ReplyKeyboardMarkup(True, False)
         catalog_markup.row('Вraveheart', 'Вrooklyn','Сhoice', 'Сonvoy')
         catalog_markup.row('Gаrden', 'SаntaCruz','Тrailblazer','Vеgas')
         catalog_markup.row('⬅ Back') 
         bot.send_message(message.from_user.id, "Виберіть каталог ⬇", reply_markup=catalog_markup)
       
       elif  message.text == "Вraveheart": #русская В
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Braveheart.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Вrooklyn": #русская В
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Brooklyn.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Сhoice": #русская С
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Choice.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Сonvoy": #русская С
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Convoy.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Gаrden": #русская а
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Gardencollection.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "SаntaCruz": #русская а
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/SantaCruz.pdf",
                disable_web_page_preview = True) 
       elif  message.text == "Тrailblazer": #русская Т
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Trailblazer.pdf",
                disable_web_page_preview = True)       
       elif  message.text == "Vеgas": #русская е
                bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/Mebel/Vegas.pdf",
                disable_web_page_preview = True) 

       elif message.text == "⬅ Back": 
         skladm_markup = telebot.types.ReplyKeyboardMarkup()
         skladm_markup.row('📚 Suerte', '📚 L1nkstudio')
         skladm_markup.row('⬅ Нaзад') #английская первая а
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=skladm_markup)

       elif message.text == "📚 L1nkstudio":
         catalog_markup = telebot.types.ReplyKeyboardMarkup(True, False)
         catalog_markup.row('🛏️​ Постільна білизна', '🥼 Піжами')
         catalog_markup.row('↩Hазад') #английская буква H
         bot.send_message(message.from_user.id, "Виберіть каталог ⬇", reply_markup=catalog_markup)

       elif message.text == "🛏️​ Постільна білизна":
         bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/bedroom.pdf",
         disable_web_page_preview = True)
        
       elif message.text == "🥼 Піжами":
         bot.send_message(message.from_user.id, "https://suerte-elegancia.com.ua/!TelegramBot/home_closes.pdf",
         disable_web_page_preview = True)

       elif message.text == "📚 Цены на ткани:":
         catalog_markup = telebot.types.ReplyKeyboardMarkup(True, False)
         catalog_markup.row('Suerte', 'Elegancia')
         catalog_markup.row('Margo', '⬅ Назад')
         bot.send_message(message.from_user.id, "Виберіть каталог ⬇", reply_markup=catalog_markup)

       elif message.text == "Suerte":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1JXSkU19DT_eFPFlfKr0B_paIHdDdl2MX",
         disable_web_page_preview = True)
       elif message.text == "Elegancia":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1cK-A-K619t_dsX8uVcEzmoyWqPByG102",
         disable_web_page_preview = True)
      # elif message.text == "Iliv":
      #   bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1DeU1C4DM7fkdiv9Yl5B7qxSbZ33zlIGu")
       elif message.text == "Margo":
         bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1D68f0227yf_Jz7aSBp9MDR2vB_8Mn61-",
         disable_web_page_preview = True)
     #  elif message.text == "FR-One":
     #    bot.send_message(message.from_user.id, "https://drive.google.com/open?id=1qARBc1Vv6e9eMRKeKa4wZajrDrqsOabn")


       elif message.text == "📲 Подзвонити в компанію":
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('Кер.напрямку Cтєбліна Олена', 'Директор')
         manager_markup.row('Офіс менеджер','Юлія Липова','Катерина Некипіла')
         manager_markup.row('⬅ Нaзад') #английская первая а 
         bot.send_message(message.from_user.id, "Виберіть менеджера ⬇", reply_markup=manager_markup)

       elif message.text == "Юлія Костенко":
         bot.send_message(message.from_user.id, 'Юлія Костенко\n' +
                'менеджер відділу продажів\n' +
                '\n' +
                '📱 +38 (067) 405 66 84\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager1@daylight.com.ua ')
       elif message.text == "Юлія Липова":
         bot.send_message(message.from_user.id, 'Юлія Липова\n' +
                'менеджер відділу продажів\n' +
                '\n' +
                '📱 +38 (067) 240 12 34\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager2@daylight.com.ua')
       elif message.text == "Мария Петренко":
         bot.send_message(message.from_user.id, 'Мария Петренко \n' +
                'менеджер відділу продажів\n' +
                '\n' +
                '📱 +38 (067) 327 80 81\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager3@daylight.com.ua')
       elif message.text == "Катерина Некипіла":
         bot.send_message(message.from_user.id, 'Катерина Некипіла \n' +
                'менеджер відділу продажів\n' +
                '\n' +
                '📱 +38 (067) 564 10 15\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 manager4@daylight.com.ua')
       elif message.text == "Офіс менеджер":
         bot.send_message(message.from_user.id, 'Офіс менеджер\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 office-assistant@daylight.com.ua')
       elif message.text == "Кер.напрямку Cтєбліна Олена":
         bot.send_message(message.from_user.id, 'Cтєбліна Олена\n' +
                '\n' +
                '📱 +38 (067) 247 42 22\n' +
                '\n' +
                '📱 +38 (067) 524-59-09\n' +
                '\n' +
                '📧 fibre@daylight.com.ua\n' +
                '\n' +
                '@HelenDaylight')
       elif message.text == "Директор":
         bot.send_message(message.from_user.id, 'Олена Геннадіївна\n' +
                '\n' +
                '📱 +38 (067) 401 32 03\n' +
                '\n' +
                '☎ +38 (044) 545 60 80\n' +
                '\n' +
                '📧 director@daylight.com.ua')
       
       elif message.text == "⬅ Нaзад": #английская первая а 
         manager_markup = telebot.types.ReplyKeyboardMarkup()
         manager_markup.row('📚 Прайс.Завантажити:', '📖 Наявність на складі', '❓ Запитати')
         manager_markup.row('📲 Подзвонити в компанію', '💶💵курс', '👍📸 Соц. мережі')
         manager_markup.row('⬅ Назад')
         bot.send_message(message.from_user.id, "Выберите пункт меню: ⬇", reply_markup=manager_markup)
       
       elif message.text == "⬅ Назад":
        handle_start(message, text=False)
       
       elif message.text == "👍📸 Соц. мережі":
         socnet1_markup = telebot.types.ReplyKeyboardMarkup()
         socnet1_markup.row('👍 Facebook', '📸 Instagram', '🌐 Сайт')
         socnet1_markup.row('📸 Instagram L1nkstudio')
         socnet1_markup.row('⬅ Нaзад') #английская первая а 
         bot.send_message(message.from_user.id, "Виберіть потрібний вам варіант ⬇", reply_markup=socnet1_markup)
       
       elif message.text == "👍 Facebook":
        bot.send_message(message.from_user.id, "https://www.facebook.com/suerte.elegancia/?fref=mentions")

       elif message.text == "📸 Instagram":
        bot.send_message(message.from_user.id, "https://www.instagram.com/suerte.elegancia/")
         
       elif message.text == "🌐 Сайт":
        bot.send_message(message.from_user.id, "http://www.suerte-elegancia.com.ua/")

       elif message.text == "📸 Instagram L1nkstudio":
        bot.send_message(message.from_user.id, "https://www.instagram.com/l1nkstudio_ukraine/") 
        
       elif message.text == "⬅ Назад":
        handle_start(message, text=False)
    else:
        bot.send_message(message.from_user.id, 'Для получения доступа к информации, отправьте этот id на телеграм @SuerteSupport, {}, id - {}'
                         .format(message.from_user.first_name, message.from_user.id))

bot.polling(none_stop=True)

