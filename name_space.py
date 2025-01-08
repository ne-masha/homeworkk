def test_func():
    def inner_func():
        print('Я в области видимости функции test_function')
    inner_func()

test_func()

#inner_func()
#при вызове ф-ции выше произошла ошибка "name 'inner_func' is not defined", тк она находится в закрывающей области видимости
