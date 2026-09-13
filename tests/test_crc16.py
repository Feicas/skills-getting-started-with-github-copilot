import pytest

from src.crc16 import CRC16


def test_calculate_returns_known_crc16_value():
    assert CRC16.calculate("123456789") == 0x4B37


def test_to_hex_returns_uppercase_crc16_value():
    assert CRC16.to_hex("123456789") == "4B37"


def test_hexdigest_remains_available_as_alias():
    assert CRC16.hexdigest("123456789") == CRC16.to_hex("123456789")


def test_calculate_accepts_bytes_and_bytearray():
    assert CRC16.calculate(b"ABC") == CRC16.calculate(bytearray(b"ABC"))


def test_calculate_accepts_explicit_string_encoding():
    assert CRC16.calculate("ABC", encoding="ascii") == CRC16.calculate(b"ABC")


def test_calculate_uses_explicit_encoding_for_non_ascii_strings():
    assert CRC16.calculate("é", encoding="utf-8") == CRC16.calculate("é".encode("utf-8"))
    assert CRC16.calculate("é", encoding="utf-16-le") == CRC16.calculate("é".encode("utf-16-le"))


def test_calculate_rejects_unsupported_input_types():
    with pytest.raises(TypeError):
        CRC16.calculate(123)


def test_calculate_rejects_custom_encoding_for_bytes():
    with pytest.raises(ValueError):
        CRC16.calculate(b"ABC", encoding="utf-16")


def test_calculate_rejects_out_of_range_crc_parameters():
    with pytest.raises(ValueError):
        CRC16.calculate("123456789", initial_value=0x10000)

    with pytest.raises(ValueError):
        CRC16.calculate("123456789", polynomial=-1)


def test_calculate_rejects_non_integer_crc_parameters():
    with pytest.raises(TypeError):
        CRC16.calculate("123456789", initial_value="65535")

    with pytest.raises(TypeError):
        CRC16.calculate("123456789", polynomial="40961")


def test_calculate_rejects_boolean_crc_parameters():
    with pytest.raises(TypeError):
        CRC16.calculate("123456789", initial_value=True)

    with pytest.raises(TypeError):
        CRC16.calculate("123456789", polynomial=False)


def test_crc16_static_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        CRC16()
