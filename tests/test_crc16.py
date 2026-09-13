import pytest

from src.crc16 import CRC16


def test_calculate_returns_known_crc16_value():
    assert CRC16.calculate("123456789") == 0x4B37


def test_hexdigest_returns_uppercase_crc16_value():
    assert CRC16.hexdigest("123456789") == "4B37"


def test_calculate_accepts_bytes_and_bytearray():
    assert CRC16.calculate(b"ABC") == CRC16.calculate(bytearray(b"ABC"))


def test_calculate_rejects_unsupported_input_types():
    with pytest.raises(TypeError):
        CRC16.calculate(123)


def test_calculate_rejects_out_of_range_crc_parameters():
    with pytest.raises(ValueError):
        CRC16.calculate("123456789", initial_value=0x10000)

    with pytest.raises(ValueError):
        CRC16.calculate("123456789", polynomial=-1)


def test_crc16_static_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        CRC16()
