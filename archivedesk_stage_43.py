# === Stage 43: Add CSV import for the primary record type ===
# Project: ArchiveDesk
import csv, os
from datetime import date

def load_csv(records_path):
    if not records_path.endswith('.csv'):
        raise ValueError("Only CSV files are supported")
    with open(records_path, newline='') as f:
        reader = csv.DictReader(f)
        required = {'title','content','retention_days','created_at'}
        if required - set(reader.fieldnames):
            missing = required - set(reader.fieldnames)
            raise ValueError(f"Missing columns: {missing}")
        records = []
        for row in reader:
            rec = {k: row.get(k, '') for k in required}
            for extra in ['tags','status']:
                if extra not in required and extra in row:
                    val = row[extra].strip()
                    rec[extra] = val.split(';') if ';' in val else [val]
            rec['created_at'] = date.fromisoformat(rec['created_at'])
            records.append(rec)
    return records
