## Запуск:
python -m unittest -v one_hot_encoder_test.py
## Результат выполнения:
```
(Lab3) C:\Users\zenv9\OneDrive\Desktop\tmp\PythonProogramming\Lab3\OneHotEncordingTests>python -m unittest -v one_hot_encoder_test.py
test_execute_four_cities_no_unexpected_indexes (one_hot_encoder_test.TestOneHotEncoder) ... ok
test_execute_four_cities_success (one_hot_encoder_test.TestOneHotEncoder) ... ok
test_execute_same_cities_tuple (one_hot_encoder_test.TestOneHotEncoder) ... ok
test_execute_zero_args_typeerror (one_hot_encoder_test.TestOneHotEncoder) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.007s
```

## Запуск тестов pytest: 
python -m pytest -v one_hot_encoder_pytest_test.py

## Результат проверки через pytest:
```
(Lab3) C:\Users\zenv9\OneDrive\Desktop\tmp\PythonProogramming\Lab3\OneHotEncordingTests>python -m pytest -v one_hot_encoder_pytest_test.py
================================================================== test session starts ===================================================================
platform win32 -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- C:\Users\zenv9\OneDrive\Desktop\tmp\Lab3\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\zenv9\OneDrive\Desktop\tmp\PythonProogramming\Lab3\OneHotEncordingTests
collected 4 items                                                                                                                                         

one_hot_encoder_pytest_test.py::test_cities_tuple_success PASSED                                                                                    [ 25%]
one_hot_encoder_pytest_test.py::test_empty_tuple_raise_error PASSED                                                                                 [ 50%]
one_hot_encoder_pytest_test.py::test_same_cities_tuple_success PASSED                                                                               [ 75%]
one_hot_encoder_pytest_test.py::test_tuple_has_value_success PASSED                                                                                 [100%]

=================================================================== 4 passed in 0.03s ====================================================================
```
