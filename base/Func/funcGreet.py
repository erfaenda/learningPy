def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name + '!'
        print(msg)

usernames = ['Alex', 'Roslan', 'Misha']
greet_users(usernames)