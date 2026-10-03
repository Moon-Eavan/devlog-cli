# DevLog CLI

DevLog CLI is a lightweight command-line tool for keeping short
development notes while working on projects.

Entries are stored locally in JSON format, so no database or external
service is required.

## Features

- Add development notes
- Add multiple tags to an entry
- List saved entries
- Delete entries
- Store data in a custom JSON file
- No external runtime dependencies

## Installation

Clone the repository and install it locally:

```bash
pip install -e .
```

## Usage

Add an entry:

```bash
devlog add "Implement configuration loader"
```

Add an entry with tags:

```bash
devlog add "Fix authentication redirect" --tag backend --tag bug
```

List entries:

```bash
devlog list
```

Delete an entry:

```bash
devlog delete ENTRY_ID
```

Use a different data file:

```bash
devlog --data notes.json list
```

## Tests

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## Requirements

Python 3.10 or later.