Запуск тестов производится при запуске скрипта morse.py, либо через консоль командой python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
Результат выполнения:
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('KINDA SUS') #doctest: +ELLIPSIS
Expecting:
    '-.- .. -...'
ok
Trying:
    encode('!')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '!'
ok
2 items had no tests:
    __main__
    __main__.decode
1 items passed all tests:
   3 tests in __main__.encode
3 tests in 3 items.
3 passed and 0 failed.
Test passed.

Process finished with exit code 0

Запуск pytest:
pytest morse_parametrized_test.py

Результат параметризованного теста:
(Lab3) C:\Users\zenv9\OneDrive\Desktop\tmp\PythonProogramming\Lab3\MorseTests>pytest morse_parametrized_test.py
================================================================== test session starts ===================================================================
platform win32 -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\zenv9\OneDrive\Desktop\tmp\PythonProogramming\Lab3\MorseTests
collected 4 items                                                                                                                                         

morse_parametrized_test.py ....                                                                                                                     [100%]

=================================================================== 4 passed in 0.18s ====================================================================
