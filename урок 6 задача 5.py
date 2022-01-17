import sys

users_file = sys.argv[1]
hobby_file = sys.argv[2]
result_file = sys.argv[3]
with open(users_file, 'r',encoding='utf-8') as users,\
    open(hobby_file, 'r', encoding='utf-8') as hobby,\
    open(result_file, 'w', encoding='utf-8') as result:
    for name in users:
        hobby_line = hobby.readline().strip()
        if not hobby_line:
            hobby_line = None
        string_sum = name.strip() + ': ' +  hobby_line
        result.writelines([string_sum, '\n'])
    content_hobby = hobby.read()
    if content_hobby:
        sys.exit(1)
with open(result_file, 'r',encoding='utf-8') as f:
    print('\nЗаписано:\n')
    print(f.read())


