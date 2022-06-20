from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta
from enum import Enum
from typing import TypeVar
from uuid import UUID

from . import abc

TEnum = TypeVar("TEnum", bound=Enum)


def as_aware_datetime(value: datetime | str) -> datetime:
    """Convert the value from a string to a timezone aware datetime."""
    if isinstance(value, str):
        # fromisoformat() does not handle the "Z" suffix
        if value.upper().endswith("Z"):
            value = f"{value[:-1]}+00:00"

        value = datetime.fromisoformat(value)

    return value


def as_uuid(value: UUID | str) -> UUID:
    """Convert a string-formatted UUID to a UUID instance."""
    return UUID(value) if isinstance(value, str) else value


def as_timedelta(value: timedelta | float | None) -> timedelta | None:
    return timedelta(seconds=value) if isinstance(value, (float, int)) else value


def as_enum(enum_class: type[TEnum]) -> Callable[[TEnum | str], TEnum]:
    def converter(value: TEnum | str) -> TEnum:
        return enum_class.__members__[value] if isinstance(value, str) else value

    return converter


def as_async_datastore(value: abc.DataStore | abc.AsyncDataStore) -> abc.AsyncDataStore:
    if isinstance(value, abc.DataStore):
        from apscheduler.datastores.async_adapter import AsyncDataStoreAdapter

        return AsyncDataStoreAdapter(value)

    return value
