def addNumbers(a, b):
    return int(a) + int(b)


def handle_json(name, age):
    if int(age) < 20:
        return f'Hi {name}, Your age is {age}. You are too young'
    return f'Hi {name}, you are authorised'

if __name__ == '__main__':
   print( addNumbers(2, 3))
