import time
import os
import uuid
from typing import Union

CROCKFORD_BASE32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
DECODE_MAP = {c: i for i, c in enumerate(CROCKFORD_BASE32)}

def new_ulid(timestamp_ms: Union[int, float, None] = None) -> str:
    """Generate a new 26-character Crockford Base32 encoded ULID."""
    if timestamp_ms is None:
        timestamp_ms = int(time.time() * 1000)
    else:
        timestamp_ms = int(timestamp_ms)

    # 48-bit timestamp (6 bytes) + 80-bit randomness (10 bytes) = 128 bits
    time_bytes = timestamp_ms.to_bytes(6, byteorder="big")
    rand_bytes = os.urandom(10)
    full_bytes = time_bytes + rand_bytes

    # Convert 128-bit int to 26 Base32 characters
    val = int.from_bytes(full_bytes, byteorder="big")
    chars = []
    for _ in range(26):
        chars.append(CROCKFORD_BASE32[val & 31])
        val >>= 5
    return "".join(reversed(chars))

def ulid_to_uuid(ulid_str: str) -> uuid.UUID:
    """Convert 26-character ULID to standard Python UUID."""
    if len(ulid_str) != 26:
        raise ValueError(f"Invalid ULID length: {len(ulid_str)}")

    val = 0
    for char in ulid_str.upper():
        if char not in DECODE_MAP:
            raise ValueError(f"Invalid ULID character: {char}")
        val = (val << 5) | DECODE_MAP[char]

    raw_bytes = val.to_bytes(16, byteorder="big")
    return uuid.UUID(bytes=raw_bytes)

def uuid_to_ulid(uuid_val: Union[uuid.UUID, str]) -> str:
    """Convert standard UUID to 26-character Crockford Base32 ULID."""
    if isinstance(uuid_val, str):
        uuid_val = uuid.UUID(uuid_val)

    val = int.from_bytes(uuid_val.bytes, byteorder="big")
    chars = []
    for _ in range(26):
        chars.append(CROCKFORD_BASE32[val & 31])
        val >>= 5
    return "".join(reversed(chars))
