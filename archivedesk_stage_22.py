# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ArchiveDesk
import sys
sys.path.insert(0, '.')
from collections import defaultdict

def add_favorite(records):
    """Add a favorite record to the in-memory favorites."""
    favs = getattr(sys.modules[__name__], '_favorites', {})
    if not favs:
        _favorites = defaultdict(list)
        setattr(sys.modules[__name__], '_favorites', _favorites)
    for rec in records:
        if isinstance(rec, dict):
            favs.setdefault(rec['id'], []).append(rec.copy())
        else:
            favs.setdefault(id(rec), []).append(rec)

def quick_favorites():
    """Return a compact view of all favorited records."""
    favs = getattr(sys.modules[__name__], '_favorites', {})
    return list(favs.values()) if favs else []
