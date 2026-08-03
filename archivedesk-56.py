# === Stage 56: Add compact error classes for domain failures ===
# Project: ArchiveDesk
class ArchiveError(Exception):
    """Base for all ArchiveDesk domain failures."""


class DocumentNotFoundError(ArchiveError, KeyError):
    pass


class RetentionPolicyViolation(ArchiveError):
    pass


class TagConflict(ArchiveError):
    pass


class AuditLogFull(ArchiveError):
    pass


class InvalidDocumentState(ArchiveError):
    pass


class SearchIndexCorrupted(ArchiveError):
    pass


class DatabaseIntegrityError(ArchiveError):
    pass


class ConfigurationError(ArchiveError, ValueError):
    pass


class PermissionDenied(ArchiveError, RuntimeError):
    pass


class ArchiveDeskException(Exception):
    """Generic exception for unexpected conditions."""
