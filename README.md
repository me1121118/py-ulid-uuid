# py-ulid-uuid

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-ulid-uuid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency bidirectional converter between 128-bit ULIDs (Universally Unique Lexicographically Sortable Identifiers) and UUIDs in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library (`uuid`, `time`, `os`).
- ⏱️ **Time-Ordered**: ULID preserves millisecond timestamp sorting.
- 🔄 **Lossless Bidirectional**: Losslessly convert `UUID` <-> `ULID` without losing entropy or ordering.

---

## 📦 Installation

```bash
pip install py-ulid-uuid
```

---

## 🛠️ Quickstart

```python
from py_ulid_uuid import new_ulid, ulid_to_uuid, uuid_to_ulid

# 1. Generate new ULID
ulid_str = new_ulid()
print(ulid_str)  # 01JB4V08A9B5XG2H...

# 2. Convert to UUID
uuid_obj = ulid_to_uuid(ulid_str)
print(uuid_obj)

# 3. Convert back to ULID
restored = uuid_to_ulid(uuid_obj)
assert restored == ulid_str
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library simplified your identifier conversions, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
