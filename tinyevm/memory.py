class Memory:
    def __init__(self):
        self.data: bytearray = bytearray()

    def _expand(self, offset: int, size: int) -> None:
        """Expand memory if needed."""
        end = offset + size
        if end > len(self.data):
            self.data.extend(b'\x00' * (end - len(self.data)))

    def load(self, offset: int, size: int = 32) -> int:
        """Load `size` bytes from offset as big-endian int."""
        if offset < 0:
            raise MemoryOffsetUnderflow()
        self._expand(offset, size)
        return int.from_bytes(self.data[offset:offset + size], 'big')

    def store(self, offset: int, value: int, size: int = 32) -> None:
        """Store `size` bytes at offset (big-endian)."""
        if offset < 0:
            raise MemoryOffsetUnderflow()
        if not (0 <= value < 2 ** (size * 8)):
            raise InvalidMemoryValue()
        self._expand(offset, size)
        self.data[offset:offset + size] = value.to_bytes(size, 'big')

    def store8(self, offset: int, value: int) -> None:
        """Store single byte (for MSTORE8)."""
        self.store(offset, value & 0xFF, size=1)

    def size(self) -> int:
        """Return memory size in bytes (rounded to 32-byte words)."""
        return ((len(self.data) + 31) // 32) * 32

    def __len__(self) -> int:
        return len(self.data)


# Errors

class InvalidMemoryValue(Exception):
    """Invalid memory value"""


class MemoryOffsetOverflow(Exception):
    """Memory offset overflow"""


class MemoryOffsetUnderflow(Exception):
    """Memory offset underflow"""
