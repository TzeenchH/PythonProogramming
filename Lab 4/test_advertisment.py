import pytest
import adv
import json


def test_execute_all_is_ok_return_success():
    resp_str = """{
    "title": "python",
    "price": 1,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    resp_json = json.loads(resp_str)
    result = adv.convert_to_class(resp_json, adv.Advert)
    expected_address = 'город Москва, Лесная, 7'
    expected_title = 'python'
    assert result.location.address == expected_address
    assert result.title == expected_title


def test_incorrect_price_raise_error():
    result = adv.Advert()
    with pytest.raises(ValueError):
        result.price = -10


def test_incorrect_price_in_response_raise_error():
    resp_str = """{
        "title": "python",
        "price": -1,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    resp_json = json.loads(resp_str)
    with pytest.raises(ValueError):
        adv.convert_to_class(resp_json, adv.Advert)


def test_incorrect_price_type_return_error():
    resp_str = """{
            "title": "python",
            "price": "abc",
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
            }"""
    resp_json = json.loads(resp_str)
    with pytest.raises(TypeError):
        adv.convert_to_class(resp_json, adv.Advert)


def test_incorrect_input_type_return_error():
    with pytest.raises(AttributeError):
        adv.convert_to_class("smth", adv.Advert)


def test_invalid_class_return_error():
    resp_str = """{
               "title": "python",
               "price": "abc",
               "location": {
                   "address": "город Москва, Лесная, 7",
                   "metro_stations": ["Белорусская"]
                   }
               }"""
    resp_json = json.loads(resp_str)
    with pytest.raises(TypeError):
        adv.convert_to_class(resp_json, "not adv")
