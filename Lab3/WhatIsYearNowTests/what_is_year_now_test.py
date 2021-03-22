import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_execute_success(urlopen_mock):
    api_mock = MagicMock()
    api_mock.getcode.return_value = 200
    api_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"2021-03-22T08:36Z",' \
        '"utcOffset":"01:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2021-80",' \
        '"serviceResponse":null' \
        '}'
    api_mock.__enter__.return_value = api_mock
    urlopen_mock.return_value = api_mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_invalid_format_raise_value_error(urlopen_mock):
    api_mock = MagicMock()
    api_mock.getcode.return_value = 200
    api_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"22.2021--T08:36Z",' \
        '"utcOffset":"01:00:00",' \
        '"isDayLightSavingsTime":true,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2021-80",' \
        '"serviceResponse":null' \
        '}'

    api_mock.__enter__.return_value = api_mock
    urlopen_mock.return_value = api_mock

    with pytest.raises(ValueError):
        what_is_year_now.what_is_year_now()


@patch('urllib.request.urlopen')
def test_execute_alternative_format_success(urlopen_mock):
    api_mock = MagicMock()
    api_mock.getcode.return_value = 200
    api_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"03.22.2021T08:36Z",' \
        '"utcOffset":"01:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2021-80",' \
        '"serviceResponse":null' \
        '}'
    api_mock.__enter__.return_value = api_mock
    urlopen_mock.return_value = api_mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021
