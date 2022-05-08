def mask_host(ip, subnet, host):
    ip = ip.split('.')
    N = 0  # количество битов сети
    S = 0  # количество заимствованных бит на подсеть
    H = 0  # количество выделенных бит на хоста
    mask = ''
    m1 = 0  # количество выделенных на маску бит
    m2 = 0  # кол-во октет в маске
    m3 = 0  # счетчик для последнего ненулевого бита в маске
    bit = 0  # последний ненулевой бит
    bit0 = ''  # нулевые биты маски
    p = 0
    k = 0

    if 0 < int(ip[0]) < 128:
        N = 8
        while 2 ** S <= subnet:
            S += 1
        H = 32 - (N + S)
        if 2 ** H - 2 >= host:
            m1 = N + S
            m2 = m1 // 8
            m3 = m1 % 8
        if m3 != 0:
            for i in range(7, -1, -1):
                bit += 2 ** i
                m3 -= 1
                if m3 <= 0:
                    break
        p = H // 8 - 1
        for i in range(0, p + 2):
            bit0 = '.' * i + '0' * i
            mask = '255.' * m2 + str(bit) + bit0
        print('Маска подсети: ', mask, '\nКласс сети: A \nНачальный адрес: 0.0.0.0 \nКонечный адрес: 127.255.255.255',
              '\nКоличество возможных сетей: ', 2 ** H)
        if m2 <= 3:
            print('Количество доступных сетей: ', 2 ** H - 2)
        else:
            print('Количество доступных сетей: ', 2 ** H - 1)
        print('Стек первых 5 допустимых IP-адресов: ')
        if m2 == 3:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + (str(ip[2]) + "." + str(i))))
        if m2 == 2:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + str(int(ip[2]) & bit) + "." + str(i)))
        elif m2 == 1:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (int(ip[1]) & bit) + "." + "0" + "." + str(i))
        print('Стек последних 5 допустимых IP-адресов:')
        if m2 == 3:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(249 + i))
        if m2 == 2:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(int(ip[2]) & bit | k) + "." + str(249 + i))
        elif m2 == 1:
            for i in range((16 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(int(ip[1]) & bit) + "." + str(int(ip[2]) & bit | k) + +"." + str(249 + i))

    elif 128 <= int(ip[0]) < 192:
        N = 16
        while 2 ** S <= subnet:
            S += 1
        H = 32 - (N + S)
        if 2 ** H - 2 >= host:
            m1 = N + S
            m2 = m1 // 8
            m3 = m1 % 8
        if m3 != 0:
            for i in range(7, -1, -1):
                bit += 2 ** i
                m3 -= 1
                if m3 <= 0:
                    break
        p = H // 8 - 1
        for i in range(0, p + 2):
            bit0 = '.' * i + '0' * i
            mask = '255.' * m2 + str(bit) + bit0
        print('Маска подсети: ', mask, '\nКласс сети: B \nНачальный адрес: 128.0.0.0 \nКонечный адрес: 191.255.255.255',
              '\nКоличество возможных сетей: ', 2 ** H)
        if m2 <= 3:
            print('Количество доступных сетей: ', 2 ** H - 2)
        else:
            print('Количество доступных сетей: ', 2 ** H - 1)
        print('Стек первых 5 допустимых IP-адресов: ')
        if m2 == 3:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + (str(ip[2]) + "." + str(i))))
        if m2 == 2:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + str(int(ip[2]) & bit) + "." + str(i)))
        elif m2 == 1:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (int(ip[1]) & bit) + "." + "0" + "." + str(i))
        print('Стек последних 5 допустимых IP-адресов:')
        if m2 == 3:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(249 + i))
        if m2 == 2:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(int(ip[2]) & bit | k) + "." + str(249 + i))
        elif m2 == 1:
            for i in range((16 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(int(ip[1]) & bit) + "." + str(int(ip[2]) & bit | k) + +"." + str(249 + i))

    elif 192 <= int(ip[0]) < 224:
        N = 24
        while 2 ** S <= subnet:
            S += 1
        H = 32 - (N + S)
        if 2 ** H - 2 >= host:
            m1 = N + S
            m2 = m1 // 8
            m3 = m1 % 8
        if m3 != 0:
            for i in range(7, -1, -1):
                bit += 2 ** i
                m3 -= 1
                if m3 <= 0:
                    break
        p = H // 8 - 1
        for i in range(0, p + 2):
            bit0 = '.' * i + '0' * i
            mask = '255.' * m2 + str(bit) + bit0
        print('Маска подсети: ', mask, '\nКласс сети: C \nНачальный адрес: 192.0.0.0 \nКонечный адрес: 223.255.255.255',
              '\nКоличество возможных сетей: ', 2 ** H)
        if m2 <= 3:
            print('Количество доступных сетей: ', 2 ** H - 2)
        else:
            print('Количество доступных сетей: ', 2 ** H - 1)
        print('Стек первых 5 допустимых IP-адресов: ')
        if m2 == 3:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + (str(ip[2]) + "." + str(i))))
        if m2 == 2:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + str(int(ip[2]) & bit) + "." + str(i)))
        elif m2 == 1:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (int(ip[1]) & bit) + "." + "0" + "." + str(i))
        print('Стек последних 5 допустимых IP-адресов:')
        if m2 == 3:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(249 + i))
        if m2 == 2:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(int(ip[2]) & bit | k) + "." + str(249 + i))
        elif m2 == 1:
            for i in range((16 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(int(ip[1]) & bit) + "." + str(int(ip[2]) & bit | k) + +"." + str(249 + i))

    elif 224 <= int(ip[0]) < 240:
        N = 28
        while 2 ** S <= subnet:
            S += 1
        H = 32 - (N + S)
        if 2 ** H - 2 >= host:
            m1 = N + S
            m2 = m1 // 8
            m3 = m1 % 8
        if m3 != 0:
            for i in range(7, -1, -1):
                bit += 2 ** i
                m3 -= 1
                if m3 <= 0:
                    break
        p = H // 8 - 1
        for i in range(0, p + 2):
            bit0 = '.' * i + '0' * i
            mask = '255.' * m2 + str(bit) + bit0
        print('Маска подсети: ', mask, '\nКласс сети: D \nНачальный адрес: 224.0.0.0 \nКонечный адрес: 240.255.255.255',
              '\nКоличество возможных сетей: ', 2 ** H)
        if m2 <= 3:
            print('Количество доступных сетей: ', 2 ** H - 2)
        else:
            print('Количество доступных сетей: ', 2 ** H - 1)
        print('Стек первых 5 допустимых IP-адресов: ')
        if m2 == 3:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + (str(ip[2]) + "." + str(i))))
        if m2 == 2:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (str(ip[1]) + "." + str(int(ip[2]) & bit) + "." + str(i)))
        elif m2 == 1:
            for i in range(1, 6):
                print(str(ip[0]) + "." + (int(ip[1]) & bit) + "." + "0" + "." + str(i))
        print('Стек последних 5 допустимых IP-адресов:')
        if m2 == 3:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(249 + i))
        if m2 == 2:
            for i in range((24 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(ip[1]) + "." + str(int(ip[2]) & bit | k) + "." + str(249 + i))
        elif m2 == 1:
            for i in range((16 - m1) - 1, -1, -1):
                k += (2 ** i)
            for i in range(1, 6):
                print(str(ip[0]) + "." + str(int(ip[1]) & bit) + "." + str(int(ip[2]) & bit | k) + +"." + str(249 + i))
    return ''


ip = input('Введите IP-адрес: ')
subnet = int(input('Введите количество подсетей: '))
host = int(input('Введите количество хостов: '))
mask_host(ip, subnet, host)
