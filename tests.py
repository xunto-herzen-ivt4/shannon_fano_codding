from shannon_fano_codding import encode, decode
import pprint

messages = [
    "Код_Шеннона-Фано",
    '''
А судьи кто? — За древностию лет
К свободной жизни их вражда непримирима,
Сужденья черпают из забытых газет
Времен Очаковских и покоренья Крыма;
Всегда готовые к журьбе,
Поют всё песнь одну и ту же,
Не замечая об себе:
Что старее, то хуже.
Где? укажите нам, отечества отцы,
Которых мы должны принять за образцы?
Не эти ли, грабительством богаты?
Защиту от суда в друзьях нашли, в родстве,
Великолепные соорудя палаты,
Где разливаются в пирах и мотовстве,
И где не воскресят клиенты-иностранцы
Прошедшего житья подлейшие черты.
'''
]

pp = pprint.PrettyPrinter(indent=4)
for message in messages:
    codes, encoded = encode(message)
    print('\n\n=====')
    print('Message:\n', message)
    print('Codes:\n', pp.pprint(codes))
    print('Encode:\n', encoded)
    print('Decode:\n', decode(codes, encoded))
