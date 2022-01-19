import re


def email_parse(name):
    if 2 != len(re.compile(r'[^\w]').findall(name)):
        raise ValueError(name)
    e_mail = dict()
    re_email = re.compile(r'([\w,.]+)')
    e_mail['username'] = re_email.findall(name)[0]
    e_mail['domain'] = re_email.findall(name)[1]
    print(re.compile(r'([^\w])').findall(name))
    print(len(re.compile(r'[^\w]').findall(name)))
    return e_mail


print(email_parse('someone@geekbrains.ru'))
