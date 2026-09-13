class CRC16:
    """Static helpers for calculating CRC16 checksums."""

    def __new__(cls, *args, **kwargs):
        raise TypeError("CRC16 is a static class and cannot be instantiated")

    @staticmethod
    def calculate(data, initial_value=0xFFFF, polynomial=0xA001):
        payload = CRC16._normalize(data)
        crc = initial_value & 0xFFFF
        polynomial &= 0xFFFF

        for byte in payload:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ polynomial
                else:
                    crc >>= 1

        return crc & 0xFFFF

    @staticmethod
    def hexdigest(data, initial_value=0xFFFF, polynomial=0xA001):
        return f"{CRC16.calculate(data, initial_value, polynomial):04X}"

    @staticmethod
    def _normalize(data):
        if isinstance(data, str):
            return data.encode("utf-8")
        if isinstance(data, (bytes, bytearray)):
            return bytes(data)
        raise TypeError("CRC16 data must be str, bytes, or bytearray")
