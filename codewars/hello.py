def validate_hello(greetings):
    words = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in words:
        if i in greetings.lower():
            return True
    return False
    

print(validate_hello('hello'))