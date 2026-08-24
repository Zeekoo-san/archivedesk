# === Stage 61: Add performance timing for core list and search operations ===
# Project: ArchiveDesk
import time

def benchmark_operation(func, *args, **kwargs):
    """Run a function and return timing info."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed

def list_documents_with_timing(records_archive):
    """Benchmark the list_documents operation."""
    def list_func():
        return records_archive.list_documents()
    result, elapsed = benchmark_operation(list_func)
    return result, elapsed
