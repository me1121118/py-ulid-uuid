import uuid
import pytest
from py_ulid_uuid import new_ulid, ulid_to_uuid, uuid_to_ulid

def test_ulid_roundtrip():
    ulid = new_ulid()
    assert len(ulid) == 26

    u = ulid_to_uuid(ulid)
    assert isinstance(u, uuid.UUID)

    restored = uuid_to_ulid(u)
    assert restored == ulid

def test_uuid_to_ulid():
    test_uuid = uuid.uuid4()
    ulid = uuid_to_ulid(test_uuid)
    assert len(ulid) == 26
    assert ulid_to_uuid(ulid) == test_uuid
