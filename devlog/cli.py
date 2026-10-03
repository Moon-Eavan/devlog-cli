import argparse

from .service import DevLogService
from .storage import JsonStorage


def print_entry(entry):
    tags = ", ".join(entry.tags) if entry.tags else "-"

    print(f"[{entry.id}] {entry.message}")
    print(f"  tags: {tags}")
    print(f"  created: {entry.created_at}")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="devlog",
        description="Manage development notes from the command line.",
    )

    parser.add_argument(
        "--data",
        default="devlog.json",
        help="Path to the JSON data file.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new development note.",
    )

    add_parser.add_argument(
        "message",
        help="Note message.",
    )

    add_parser.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Add a tag to the note.",
    )

    subparsers.add_parser(
        "list",
        help="List saved development notes.",
    )

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a development note.",
    )

    delete_parser.add_argument(
        "id",
        help="ID of the note.",
    )

    args = parser.parse_args()

    service = DevLogService(
        JsonStorage(args.data)
    )

    if args.command == "add":
        entry = service.add_entry(
            args.message,
            args.tag,
        )

        print("Entry created:")
        print_entry(entry)

    elif args.command == "list":
        entries = service.list_entries()

        if not entries:
            print("No entries found.")
            return

        for entry in entries:
            print_entry(entry)

    elif args.command == "delete":
        deleted = service.delete_entry(args.id)

        if deleted:
            print(f"Deleted entry: {args.id}")
        else:
            print(f"Entry not found: {args.id}")


if __name__ == "__main__":
    main()