
def from_hex(value: str):
    if not value.startswith('0x'):
        value = '0x' + value
    return int(value, base=16)


def calculate_twos_complement(value: int, bits=256):
    if value & (1 << (bits - 1)) != 0:  # 100
        value = value - (1 << bits)
    return value
