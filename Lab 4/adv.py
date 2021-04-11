import json
import keyword


class ColorizedMixin:
    """
    Returns selected attributes with yellow color
    """
    colour_code = 33

    def __repr__(self):
        return f'\033[1;{self.colour_code};1m ' \
               f'{self.title} : {self.price} ₽' \
               f'\033[0;1;1m'


class Advert(ColorizedMixin):
    """
    Represents json response
    """

    _price: int = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        if value < 0:
            raise ValueError("Value must be greater than 0")
        self._price = value

    """
    Ctobi ne dolbanulo oshibkoy
    """

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = "ne" + key
        super.__setattr__(self, key, value)


def convert_to_class(json_response: dict, result: Advert) -> Advert:
    """
    Converts JSON response to new Advert class object
    :param json_response: JSON data
    :param result: Advert class
    :return: new Advert class
    """
    tmp = result()
    for key, val in json_response.items():
        if isinstance(val, (list, tuple)):
            tmp.__setattr__(key, [convert_to_class(subval, result) if isinstance(subval, dict) else subval for subval in
                                  val])
        else:
            tmp.__setattr__(key, convert_to_class(val, result) if isinstance(val, dict) else val)
    return tmp


corgi_resp = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

if __name__ == '__main__':
    corgi_json = json.loads(corgi_resp)
    corgi_obj = convert_to_class(corgi_json, Advert)
    print(corgi_obj.neclass)
    print(corgi_obj)
    print(corgi_obj.location.address)
