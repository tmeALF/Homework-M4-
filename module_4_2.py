def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


# inner_function() - вызов функции вне test_function приводит к ошибке.

test_function()
