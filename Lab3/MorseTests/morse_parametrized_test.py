import pytest
import morse


@pytest.mark.parametrize('mrs, exp', [
    ('.-', 'A'),
    ('... --- ...', 'SOS'),
    ('-.- .. -. -.. .-', 'KINDA'),
    ('... ..- ...', 'SUS')
])
def test_decode(mrs, exp):
    assert morse.decode(mrs) == exp
