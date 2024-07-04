def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

print(f'Невозможно вызывать из глобального пространства функцию "inner_function",'
      f'\nтак как она находится внутри объёмлющего пространства функции test_function.')

test_function() #Вызов функции test_function, которая вызывает вложенную функцию inner_function
