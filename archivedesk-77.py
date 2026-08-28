# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ArchiveDesk
from typing import Optional, List, Dict, Any, TypeVar, Callable, Union

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


def safe_get(d: Dict[K, V], key: K, default: Any = None) -> Optional[V]:
    """Return dict value or default, never raising KeyError."""
    return d.get(key, default)


def flatten_list(nested: List[Any]) -> List[T]:
    """Flatten one level of nesting; non-list items are kept as-is."""
    result: List[T] = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Restrict value to [minimum, maximum]."""
    return max(minimum, min(value, maximum))


def identity(value: T) -> T:
    """Return the input unchanged."""
    return value


def is_substring(haystack: str, needle: str) -> bool:
    """Check whether needle appears in haystack."""
    return needle in haystack


def merge_dicts(base: Dict[Any, Any], override: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a new dict with override values taking precedence."""
    merged = dict(base)
    merged.update(override)
    return merged


def chunk_list(lst: List[T], size: int) -> List[List[T]]:
    """Split lst into chunks of given size; last chunk may be smaller."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]
