# coding: utf-8
"""
    project: main
    module created: 24.02.2016

    Constants, that are used in the project
"""

MILITARY_COMISSARIAT_TYPES = (
    ('balashiha', u'Отдел ВКМО по гг. Балашиха, Железнодорожный, Реутов и Балашихинскому району'),
    ('vidnoe',u'Отдел ВКМО по гг. Видное, Московский и Ленинскому району'),
    ('volokolamsk', u'Отдел ВКМО по г. Волоколамск, Волоколамскому, Лотошинскому и Шаховскому районам'),
    ('voskresensk', u'Отдел ВКМО по г. Воскресенск и Воскресенскому району'),
    ('dmitrov', u'Отдел ВКМО по гг. Дмитров, Яхрома и Дмитровскому району'),
    ('domodedovo', u'Отдел ВКМО по г. Домодедово и Домодедовскому району'),
    ('dubna', u'Отдел ВКМО по гг. Дубна, Талдом и Талдомскому району'),
    ('egorievsk', u'Отдел ВКМО по г. Егорьевск и Егорьевскому району'),
    ('gukovsk',u'Отдел ВКМО по г. Жуковский и Жуковскому району'),
    ('istra', u'Отдел ВКМО по г. Истра и Истринскому району'),
    ('kashira', u'Отдел ВКМО по г. Кашира, Каширскому и Серебряно-Прудскому районам'),
    ('klin', u'Отдел ВКМО по г. Клин и Клинскому району'),
    ('kolomna', u'Отдел ВКМО по гг. Коломна, Озеры, Коломенскому и Озерскому районам'),

    ('krasnogorsk', u'Отдел ВКМО по г. Красногорск и Красногорскому району'),
    ('luhovicu', u'Отдел ВКМО по гг. Луховицы, Зарайск, Луховицкому и Зарайскому районам'),
    ('lyubercu', u'Отдел ВКМО по гг. Люберцы, Лыткарино и Люберецкому району'),
    ('mojaysk', u'Отдел ВКМО по г. Можайск и Можайскому району'),
    ('mutishy', u'Отдел ВКМО по гг. Мытищи, Королев, Юбилейный и Мытищинскому району'),
    ('naro-fominsk', u'Отдел ВКМО по г. Наро-Фоминск и Наро-Фоминскому району'),
    ('noginsk', u'Отдел ВКМО по гг. Ногинск, Электросталь, Черноголовка и Ногинскому району'),
    ('odincovo', u'Отдел ВКМО по гг. Одинцово, Звенигород, Краснознаменск и Одинцовскому району'),
    ('orehovo-zuevo', u'Отдел ВКМО по г. Орехово-Зуево и Орехово-Зуевскому району'),
    ('pavlovskiy_possad', u'Отдел ВКМО по гг. Павловский Посад, Электрогорск и Павлово-Посадскому району'),
    ('podolsk', u'Отдел ВКМО по гг. Подольск, Климовск, Троицк, Щербинка и Подольскому району'),
    ('pushkino', u'Отдел ВКМО по гг. Пушкино, Ивантеевка, Красноармейск и Пушкинскому району'),
    ('ramenskoe', u'Отдел ВКМО по гг. Раменское, Жуковский, Бронницы и Раменскому району'),
    ('ruza', u'Отдел ВКМО по г. Руза и Рузскому району'),
    ('serpuhov', u'Отдел ВКМО по гг. Серпухов, Пущино, Протвино и Серпуховскому району'),

    ('sergiev',u'Отдел ВКМО по г. Сергиев Посад и Сергиево-Посадскому району'),
    ('solnechnogorsk', u'Отдел ВКМО по г. Солнечногорск и Солнечногорскому району'),
    ('stupino', u'Отдел ВКМО по г. Ступино и Ступинскому району'),
    ('himki', u'Отдел ВКМО по гг. Химки, Долгопрудный, Лобня и Химкинскому району'),
    ('chehov', u'Отдел ВКМО по г. Чехов и Чеховскому району'),
    ('shatura', u'Отдел ВКМО по гг. Шатура, Рошаль и Шатурскому району'),
    ('schelkovo', u'Отдел ВКМО по гг. Щёлково, Фрязино, Лосино-Петровский и Щёлковскому району'),


    ('akademichiskiy',u'Отдел ОВК г. Москвы по Академическому району ЮЗАО'),
    ('babuskinskiy',u'Отдел ОВК г. Москвы по Бабушкинскому району СВАО'),
    ('butovo',u'Отдел ОВК г. Москвы по Бутовскому району ЮЗАО'),
    ('butyrka',u'Отдел ОВК г. Москвы по Бутырскому району СВАО'),
    ('gagarin',u'Отдел ОВК г. Москвы по Гагаринскому району ЮЗАО'),
    ('golovinskiy',u'Отдел ОВК г. Москвы по Головинскому району САО'),
    ('danilovskiy',u'Отдел ОВК г. Москвы по Даниловскому району ЮАО'),
    ('zamosvoreckiy',u'Отдел ОВК г. Москвы по Замоскворецкому району ЦАО'),
    ('zelenograd',u'Отдел ОВК г. Москвы по Зеленоградскому АО'),
    ('izmailovo',u'Отдел ОВК г. Москвы по Измайловскому району ВАО'),
    ('coptevskiy',u'Отдел ОВК г. Москвы по Коптевскому району САО'),
    ('krasnoselskiy',u'Отдел ОВК г. Москвы по Красносельскому району ЦАО'),
    ('kunzevo',u'Отдел ОВК г. Москвы по Кунцевскому району ЗАО'),
    ('lefortovo',u'Отдел ОВК г. Москвы по Лефортовскому району ЮВАО'),
    ('lyublino',u'Отдел ОВК г. Москвы по Люблинскому району ЮВАО'),
    ('mitinskiy',u'Отдел ОВК г. Москвы по Митинскому району СЗАО'),
    ('ostanskinskiy',u'Отдел ОВК г. Москвы по Останкинскому району СВАО'),
    ('perovskiy',u'Отдел ОВК г. Москвы по Перовскому району ВАО'),
    ('preobrajenskiy',u'Отдел ОВК г. Москвы по Преображенскому району ВАО'),
    ('kuzminki',u'Отдел ОВК г. Москвы по району Кузьминки ЮВАО'),
    ('ramenki',u'Отдел ОВК г. Москвы по району Раменки ЗАО'),
    ('savelovskiy',u'Отдел ОВК г. Москвы по Савёловскому району САО'),
    ('solncevskiy',u'Отдел ОВК г. Москвы по Солнцевскому району ЗАО'),
    ('tverskoy',u'Отдел ОВК г. Москвы по Тверскому району ЦАО'),
    ('timiryazevskiy',u'Отдел ОВК г. Москвы по Тимирязевскому району САО'),
    ('tushinskiy',u'Отдел ОВК г. Москвы по Тушинскому району СЗАО'),
    ('horoshevskiy',u'Отдел ОВК г. Москвы по Хорошёвскому району СЗАО'),
    ('caricuno',u'Отдел ОВК г. Москвы по Царицынскому району ЮАО'),
    ('cheremuskinskiy',u'Отдел ОВК г. Москвы по Черёмушкинскому району ЮЗА'),
    ('chertanocskiy',u'Отдел ОВК г. Москвы по Чертановскому району ЮАО'),

    ('none', u'Не верный комиссариат'),
    )


GRADE_TYPES = (
    ('soldier', u'Солдат'),
    ('sergeant', u'Сержант'),
    ('officer', u'Офицер Запаса'),
    ('none', u'Неизвестно')
)


DEGREE_OF_FITNESS_TYPES = (
    ('A', u'Годен'),
    ('B', u'Годен с незначительными ограничениями'),
    ('V', u'Ограниченно годен'),
    ('G', u'Временно не годен'),
    ('D', u'Не годен')
)


DEPARTMENT_TYPES = (
    ('MT', u'МТ'),
    ('IU', u'ИУ'),
    ('RL', u'РЛ'),
    ('FN', u'ФН'),
    ('SM', u'СМ'),
    ('E', u'Э'),
    ('RK', u'РК'),
    ('IBM', u'ИБМ'),
    ('L', u'Л'),
    ('BMT', u'БМТ'),
    ('SGN', u'СГН'),
    ('RKT', u'РКТ'),
    ('AK', u'АК'),
    ('PS', u'ПС'),
    ('RT', u'РТ'),
    ('OEP', u'ОЭП'),
)


VUS_TYPES = (
    ('084000', '084000'),
    ('085000', '085000'),
    ('141600', '141600'),
    ('659182', '659182'),
    ('659995', '659995'),
    ('059995', '059995'),
)
