from typing import Type, Sized


def validate_type(value: object, key: str, expected_type: Type):
    if not isinstance(value, str):
        raise TypeError(f'{key.capitalize()} should be {expected_type}.')
    return value


def validate_empty(value: object, key: str):
    if isinstance(value, str) and not value.strip():
        raise ValueError(f'{key.capitalize()} cannot be empty.')
    if not value:
        raise ValueError(f'{key.capitalize()} cannot be empty.')
    return value


def validate_len(value: Sized, key: str, max_len: int):
    if len(value) > 200:
        raise ValueError(f'{key.capitalize()} cannot larger then {max_len} characters.')
    return value
