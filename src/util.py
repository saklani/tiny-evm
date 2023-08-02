
def from_hex(value: str):
    if not value.startswith('0x'):
        value = '0x' + value
    return int(value, base=16)