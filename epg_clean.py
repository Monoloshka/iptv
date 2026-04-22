import re

# Читаем XML
with open("epgm1.xml", "r", encoding="utf-8") as f:
    xml = f.read()

# ====== MAPPING КАНАЛОВ (ТОЛЬКО ДО <programme>) ======

mapping = {
    " &": "",
    "Extreme Sports [RU]": "Extreme Sports",
    "Мировое Кино KZ": "Мировое кино",
    "Перец Int": "Перец",
    "Setanta Sport+ [KZ]": "Setanta sport KZ+",
    "Твоё ТВ Qazaqstan": "Твоё Телевидение",
    "12 канал Омск": "12 канал Омск",
    "1HD Music": "1HD Music Television",
    "24 [UA]": "Канал 24 HD",
    "31 канал (Казахстан)": "31 канал",
    "5 канал [KZ]": "5 канал (региональный)",
    "77TV": "77 TV",
    "7 канал (Казахстан)": "Седьмой канал",
    "8 канал International": "8 канал",
    "9 канал [IL]": "9 канал (Израиль)",
    "Abai TV": "ABAI TV",
    "Айғак": "Айғақ",
    "Алау": "Алау ТВ",
    "Алматы": "Almaty tv",
    "A HOME OF HBO 1": "Amedia Hit",
    "A HOME OF HBO 2": "Amedia Premium",
    "Animal Planet HD": "Animal Planet",
    "AQJAIYQ": "Aqjaiyq",
    "Астана": "Astana tv",
    "Atameken Business": "Atameken bussiness channel",
    "ATYRAY": "Atyraý",
    "BBC": "BBC World News",
    "Бобер": "Бобёр",
    "Boomerang": "cartoonito",
    "ЦТ": "Центральное ТВ",
    "Da Vinci Learning": "Da Vinci",
    "Deutsche Welle Russia": "Deutsche Welle",
    "Домашний International": "Домашний International",
    "Дом кино Премиум": "Дом кино Premium",
    "Достық [KZ]": "Достық",
    "Дождь": "Дождь",
    "Эхо TV": "Эхо ТВ",
    "Еда Премиум Int. HD": "Еда премиум международный",
    "English Club TV": "English Club TV",
    "ERTIS": "Ertis",
    "Euronews (английский)": "Euronews",
    "EuroNews": "Euronews English",
    "Fashion One": "Fashion & Lifestyle",
    "Film.Ua Drama": "FilmUADrama",
    "FX Life": "Fx Life",
    "Galaxy-TV": "Тайны галактики",
    "Губерния Самара": "Самара 450",
    "Gulli": "Gulli girl",
    "H2": "History 2HD",
    "HIT TV": "Hit TV",
    "Ирбис": "Ирбис TV",
    "Kazakh TV": "Jibek Joly",
    "Казахстан": "Qazaqstan",
    "KAZsport": "Qazsport",
    "КиноБоевик KZ": "Кинобоевик",
    "Киносат": "Киноман",
    "Kokshe": "Kókshe",
    "Луч (ЯНАО)": "Луч ТРК",
    "Mangystay": "Mańǵystaý",
    "Кто Куда": "#Ктокуда",
    "Моя Планета": "Планета",
    "MuzZone": "Muzzone",
    "Nick Jr": "Nick Jr.",
    "Новый век (Тамбов)": "Новый век (Тамбов)",
    "НТРК Ингушетия": "Магас",
    "Отырар TV": "Отырар-TV",
    "Пятница Int KZ": "Пятница! International",
    "Пятый Int": "Пятый канал",
    "Премиум Кино KZ": "Премиум кино",
    "ПРНК": "Первый Российский Национальный канал",
    "Киносериал HD [KZ]": "Киносериал",
    "Кинодрама HD [KZ]": "Кинодрама",
    "Телеканал Радио Страна ФМ": "Страна FM",
    "РенТВ International": "Рен ТВ international",
    "Рика": "РИКА-ТВ",
    "РТР-Планета Азия": "РТР-Планета",
    "RU.TV": "RU TV",
    "С1 Сургут": "С1",
    "Sälem, älem! [KZ]": "Sälem, älem!",
    "Семейное Кино KZ": "Семейное кино",
    "Setanta Казахстан": "Setanta Qazaqstan",
    "Шансон-TB": "Шансон ТВ",
    "Show KZ": "Show kz",
    "Sport+ Qazaqstan": "Sport+",
    "Start Air": "Start.Air",
    "Start World": "Start.World",
    "ТДК 42": "TDK 42",
    "ТНТ KZ": "ТНТ",
    "ТНТ4 International": "ТНТ4",
    "Туран ТВ": "Turan TV",
    "Turkistan": "Туркестан",
    "TV BRICS": "TV BRICS",
    "Твоё ТВ Казахстан": "Твоё Телевидение",
    "TV XXI": "ТВ21",
    "viju+ Sport": "Viju+ Sport",
    "viju+ Comedy": "Viju+ Comedy",
    "viju+ Megahit": "Viju+ Megahit",
    "viju+ Premiere": "Viju+ Premiere",
    "viju+ Serial": "Viju+serial",
    "Хабар 24": "24 KZ",
    "Жетысу": "Жетiсу",
    "ZooПарк": "ZOOпарк",
}

marker = "<programme"

before, sep, after = xml.partition(marker)

for old, new in mapping.items():
    before = before.replace(old, new)

xml = before + sep + after

# ====== ДАЛЬШЕ ВАША ОЧИСТКА ======
xml = re.sub(r"<!DOCTYPE tv SYSTEM \"https://iptvx.one/xmltv.dtd\">", "", xml)

xml = re.sub(r"<tv generator-info-name=\"Monoloshka\">", "<tv>", xml)
# Удаляем <desc>...</desc>
xml = re.sub(r"<desc>.*?</desc>", "", xml, flags=re.DOTALL)

# Удаляем <category>...</category>
xml = re.sub(r"<category>.*?</category>", "", xml, flags=re.DOTALL)

# Удаляем <icon ... />
xml = re.sub(r"<icon[^>]*/>", "", xml)

# Удаляем все </tv>
xml = re.sub(r"</tv>", "", xml)

# Добавляем закрывающий тег </tv> в конец
xml += "\n</tv>\n"

# Убираем пустые строки
xml = re.sub(r"\n\s*\n", "\n", xml)

# Сохраняем результат
with open("epgm2.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("Файл epgm2.xml создан!")