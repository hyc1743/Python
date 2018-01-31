def trim(s):
    if s == '':
        return ''
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s
        
if trim('hello  ') != 'hello':
    print('fail!')
elif trim('  hello') != 'hello':
    print('fail!')
elif trim('  hello  ') != 'hello':
    print('fail!')
elif trim('  hello  world  ') != 'hello  world':
    print('fail!')
elif trim('') != '':
    print('fail!')
elif trim('    ') != '':
    print('fail!')
else:
    print('success!')