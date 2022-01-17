list_log = []
dict_ip = dict()
with open('nginx_logs.txt', 'r',encoding='utf-8') as f:
    for line in f:
        remote_addr = line.split(' -')[0]
        if remote_addr in dict_ip:
            dict_ip[remote_addr] = dict_ip[remote_addr]+1
        else:
            dict_ip[remote_addr] = 1
m = 0
k = 0
for key, value in dict_ip.items():
    if value >= m:
        m = value
        k = key
print('Адрес спамера:', k, '\nобратился', m, 'раз')



