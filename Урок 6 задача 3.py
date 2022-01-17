import sys
import json

dict_u_h = dict()
with open('users.csv', 'r',encoding='utf-8') as users,\
    open('hobby.csv', 'r', encoding='utf-8') as hobby:
    for name in users:
        hobby_line = hobby.readline().strip()
        if not hobby_line:
            hobby_line = None
        dict_u_h[name.strip()] = hobby_line
    content_hobby = hobby.read()
    if content_hobby:
        sys.exit(1)

#print(dict_u_h)
with open('result.json', 'w',encoding='utf-8') as result:
    dict_as_string = json.dumps(dict_u_h, ensure_ascii = False)
    result.write(dict_as_string)
with open('result.json', 'r',encoding='utf-8') as f:
    result = json.loads(f.read())
print(result)