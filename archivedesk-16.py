# === Stage 16: Add argparse support for the most common commands ===
# Project: ArchiveDesk
import argparse, sys

def main():
    parser = argparse.ArgumentParser(prog="archivedesk", description="Records archive desk")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_create = sub.add_parser("create", help="Create a document")
    p_create.add_argument("-f","--file",help="File to import (optional)")
    p_create.add_argument("--title",required=True,help="Document title")
    p_create.add_argument("--tags",nargs="+",help="Tags")
    p_create.add_argument("--retain",default=None,type=int,help="Retention days")

    p_show = sub.add_parser("show",help="Show a document by ID or path")
    p_show.add_argument("id_or_path",help="Document id or file path")

    p_search = sub.add_parser("search",help="Search documents")
    p_search.add_argument("query",nargs="+",help="Search terms")
    p_search.add_argument("--tag",action="append",dest="tags",help="Filter by tag")

    p_retain = sub.add_parser("retain",help="Mark document for retention expiry")
    p_retain.add_argument("id_or_path",help="Document id or file path")
    p_retain.add_argument("-d","--days",type=int,required=True)

    p_audit = sub.add_parser("audit",help="Show audit history")
    p_audit.add_argument("--limit",type=int,default=20)

    args = parser.parse_args()
    if hasattr(args,"file"): args.file = None if not args.file else args.file
    if hasattr(args,"tags"): args.tags = list(args.tags) if args.tags else []
    print(f"Command: {args.cmd}")
    for attr in ("title","query","id_or_path","days","limit","retain","file") if hasattr(args,attr) and getattr(args,attr) is not None else False:
        pass
    sys.exit(0)

if __name__ == "__main__": main()
