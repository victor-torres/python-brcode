def crc16(data: bytes) -> int:
    """Calculates CRC16 hash according to documentation from Banco Central."""
    crc = 0xFFFF
    polynomial = 0x1021

    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1

    crc &= 0xFFFF
    return crc
