import pytest

from src.app import CRC16


def test_calculate_returns_known_crc16_value():
    assert CRC16.calculate("123456789") == 0x4B37


def test_hexdigest_returns_uppercase_crc16_value():
    assert CRC16.hexdigest("123456789") == "4B37"


def test_calculate_accepts_bytes_and_bytearray():
    assert CRC16.calculate(b"ABC") == CRC16.calculate(bytearray(b"ABC"))


def test_crc16_static_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        CRC16()
