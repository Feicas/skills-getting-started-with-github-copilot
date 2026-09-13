class CRC16:
    """Static helpers for calculating CRC16 checksums."""

    def __new__(cls, *args, **kwargs):
        raise TypeError("CRC16 is a static class and cannot be instantiated")

    @staticmethod
    def calculate(data, initial_value=0xFFFF, polynomial=0xA001):
        """Calculate a CRC-16/Modbus checksum.

        The input may be a UTF-8 string, bytes, or bytearray. By default this
        uses the reflected CRC-16/Modbus parameters with an initial value of
        ``0xFFFF`` and polynomial ``0xA001``. Both numeric parameters must be
        16-bit unsigned integers.
        """
        payload = CRC16._normalize(data)
        crc = CRC16._validate_word(initial_value, "initial_value")
        polynomial = CRC16._validate_word(polynomial, "polynomial")

        for byte in payload:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ polynomial
                else:
                    crc >>= 1

        return crc & 0xFFFF

    @staticmethod
    def to_hex(data, initial_value=0xFFFF, polynomial=0xA001):
        """Return the CRC-16/Modbus checksum as a zero-padded uppercase hex string."""
        return f"{CRC16.calculate(data, initial_value, polynomial):04X}"

    @staticmethod
    def hexdigest(data, initial_value=0xFFFF, polynomial=0xA001):
        """Backward-compatible alias for :meth:`to_hex`."""
        return CRC16.to_hex(data, initial_value, polynomial)

    @staticmethod
    def _normalize(data):
        if isinstance(data, str):
            return data.encode("utf-8")
        if isinstance(data, (bytes, bytearray)):
            return bytes(data)
        raise TypeError("CRC16 data must be str, bytes, or bytearray")

    @staticmethod
    def _validate_word(value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if not 0 <= value <= 0xFFFF:
            raise ValueError(f"{name} must be between 0x0000 and 0xFFFF")
        return value
