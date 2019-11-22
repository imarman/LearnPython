name_for_user_id = {
    382: 'Alice',
    950: 'Arman',
    845: 'Snake'
}


def greeting(user_id):
    return f'Hi {name_for_user_id.get(user_id, "unknown")}'


result = greeting(777)
print(result)
