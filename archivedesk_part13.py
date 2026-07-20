# === Stage 13: Add file save support using a configurable path ===
# Project: ArchiveDesk
import os, datetime

class FileSaver:
    def __init__(self, archive_dir):
        self.archive_dir = archive_dir
        os.makedirs(self.archive_dir, exist_ok=True)

    def save_document(self, doc_id, content, filename=None):
        if not filename:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            ext = "txt" if isinstance(content, str) else "json"
            filename = f"{doc_id}_{ts}.{ext}"
        filepath = os.path.join(self.archive_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(content))
        return filepath

    def save_audit_log(self, record):
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.archive_dir, f"audit_{ts}.jsonl")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def get_all_documents(self):
        if not os.path.isdir(self.archive_dir): return []
        docs = []
        for fname in sorted(os.listdir(self.archive_dir)):
            if fname.endswith((".txt", ".json")) and not fname.startswith("audit_"):
                path = os.path.join(self.archive_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        docs.append({"filename": fname, "content": f.read()})
                except Exception: pass
        return docs

    def get_audit_history(self):
        logs = []
        if not os.path.isdir(self.archive_dir): return logs
        for fname in sorted(os.listdir(self.archive_dir)):
            if fname.startswith("audit_") and fname.endswith(".jsonl"):
                path = os.path.join(self.archive_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        logs.extend(json.loads(line) for line in f if line.strip())
                except Exception: pass
        return logs

    def cleanup_old_audits(self, keep_days=30):
        cutoff = datetime.datetime.now() - datetime.timedelta(days=keep_days)
        expired = []
        for fname in os.listdir(self.archive_dir):
            if fname.startswith("audit_") and fname.endswith(".jsonl"):
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(
                    os.path.join(self.archive_dir, fname))).replace(tzinfo=None)
                if mtime < cutoff:
                    expired.append(fname)
        for f in expired:
            os.remove(os.path.join(self.archive_dir, f))
        return expired
