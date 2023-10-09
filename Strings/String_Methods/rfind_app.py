email = 'userxyz.com@domain.xyz'
last_dot_pos = email.rfind('.', 1)
tld_string = email[last_dot_pos:]

if tld_string == '.com':
    print('Email matched')
else:
    print("Email not matched, tld:", tld_string)