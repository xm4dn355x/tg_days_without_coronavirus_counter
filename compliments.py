# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from random import randint


COMPLIMENTS_LIST = [
    'приятно иметь дело с такой амбициозной девушкой, как ты!',
    'так бывает очень редко, но у тебя есть способности ко всему, за что ты берешься! Ты удивительный человек!',
    'ты выглядишь сегодня сногсшибательно!',
    'твои идеи и творчество достойны восхищения!',
    'ты умеешь себя подать — это ценное качество!',
    'тобой хочется гордиться и брать с тебя пример!',
    'да ты настоящий самородок! Такие люди сегодня на вес золота!',
    'талантливый человек талантлив во многих сферах. Вот ты, например. По-моему, мало что есть, чего ты не умеешь',
    'ты непревзойденный профессионал своего дела!',
    'ты успешна не только потому, что отличный специалист, но потому, что ты замечательная девушка!',
    'ты такая мудрая! Всегда находишь правильное решение в любой ситуации!',
    'в твоем арсенале есть умения и навыки на все случаи жизни!',
    'твои блестящие успехи в работе гарантируют тебе великолепную карьеру!',
    'твои эстетические взгляды заслуживают уважения',
    'твоя светлая голова полна самых смелых идей и экспериментов!',
    'как тебе удается так грамотно спланировать свой день? У тебя для всего есть время!',
    'я знал, что есть успешные женщины, но твой успех затмевает всех!',
    'у тебя отлично получается выступать на публике! Настоящий оратор!',
    'у тебя есть огромный творческий потенциал! Ты способна творить шедевры в любой сфере жизни!',
    'у тебя есть редкие качества — слушать, анализировать и делать правильные выводы',
    'ты — гений! Молодчина!',
    'ты человек творческий, созидающий! Каждый день что-то создаешь полезное!',
    'твоя энергия, молодость и амбициозность сильно выделяют тебя из толпы',
    'ты не только интересно мыслишь, ты еще и действуешь неординарно',
    'я поражаюсь твоим интеллектуальным способностям!',
    'у тебя отличный тайм-менеджмент. Ты абсолютно все успеваешь',
    'ты замечательный фотограф. Все твои работы яркие, живые, эмоциональные.',
    'ты обладаешь удивительным качеством — принимать верные, взвешенные решения',
    'у тебя отличная самоорганизация! Как только тебе удается все успевать?',
    'ты неординарный человек - вместо того, чтобы бороться с трудностями, как все, ты их просто обходишь',
    'впервые встречаю таких как ты гибких к обстоятельствам людей',
    'так бывает очень редко, но у тебя есть способности ко всему, за что ты берешься! ты удивительный человек!',
    'твои идеи и творчество достойны восхищения!',
    'ты умеешь себя подать - это ценное качество!',
    'я очарован твоей неспешностью, тем, как ты делаешь любое дело!',
    'тобой хочется гордиться и брать с тебя пример!',
    'талантливый человек талантлив во многих сферах. вот ты, например. по-моему, мало что есть, чего ты не умеешь',
    'ты непревзойденный профессионал своего дела!',
    'ты успешна не только потому, что отличный специалист, но потому, что ты замечательная женщина!',
    'в твоем арсенале есть умения и навыки на все случаи жизни!',
    'твои блестящие успехи в работе гарантируют тебе великолепную карьеру!',
    'твои эстетические взгляды заслуживают уважения',
    'ты очень пунктуальный человек - точный как добротные швейцарские часы!',
    'твоя светлая голова полна самых смелых идей и экспериментов!',
    'со своей дальновидностью и рациональностью ты можешь высоко подняться',
    'ты внимательна в мелочах! похвально!',
    'у тебя очень заразный смех. стоит только его услышать – и настроение тут же поднимается',
    'выглядишь просто великолепно. будешь идти, смотри под ноги, чтоб ненароком на упавшего в обморок мужчину '
    'не наступить',
    'тебе очень идет такой цвет волос. подчеркивает гладкость кожи и прекрасные черты лица',
    'мне жаль тех людей, которые тебя не видели. они совсем ничего не знают о красоте',
    'каждый современный художник должен мечтать о том, чтобы иметь возможность написать твой портрет',
    'я в растерянности – не могу придумать комплимент, который будет достоин твоей красоты',
    'среди всех окружающих девушек ты единственная выглядишь настоящей',
    'девушка, быть настолько роскошной – настоящее преступление',
    'у тебя в роду случайно не было аристократов? твоя осанка – явно королевская',
    'девушка, с такой внешностью вам нужно огнетушитель с собой носить',
]


def generate_compliment(name):
    return f'{name}, {COMPLIMENTS_LIST[randint(0, (len(COMPLIMENTS_LIST)-1))]}'


if __name__ == '__main__':
    print(len(COMPLIMENTS_LIST))
    print(generate_compliment('Кристина'))
