users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]

greetings = {
    'ru':'Привет {name}!',
    'us':'Hello {name}!',
    'es':'Hola {name}!',
    'unknown country': 'Hello, {name}, but I do not know where are you from!'
}

print('\n'.join(map(lambda value: greetings[value[1]].format(name=value[0]), users_list)))