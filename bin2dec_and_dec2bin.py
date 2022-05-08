def ip_translate(ip):
    ip = ip.split('.')
    k = ''
    res = ''
    if len(ip[0]) == 8:
        for i in range(4):
            k = int(ip[i], 2)
            res += str(k) + '.'
    else:
        for i in range(4):
            while int(ip[i]) > 0:
                k = str(int(ip[i]) % 2) + k
                ip[i] = int(ip[i]) // 2
            if len(k) < 8:
                k = '0' * (8 - len(k)) + k
            res += str(k) + '.'
            k = ''
    return res


print(ip_translate(input('Введите IP: ')))
