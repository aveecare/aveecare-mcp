"""Checks every example config parses, points at the AveeCare server and holds no real key.

    python scripts/check_configs.py        (Python 3.11+, uses only the standard library)
"""

import json
import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = "https://app.aveecare.com/api/mcp"
# A real key is "ak_" + a 12 character id + "_" + a long secret. Placeholders such as "ak_..." are fine.
REAL_KEY = re.compile(r"ak_[A-Za-z0-9]{12}_[A-Za-z0-9]{20,}")
errors = []

for path in sorted((ROOT / "examples").iterdir()):
    text = path.read_text(encoding="utf-8")
    try:
        data = json.loads(text) if path.suffix == ".json" else tomllib.loads(text)
    except Exception as exc:  # noqa: BLE001 - report any parse failure
        errors.append(f"{path.name}: does not parse: {exc}")
        continue
    if URL not in text:
        errors.append(f"{path.name}: does not contain {URL}")
    print(f"ok  {path.relative_to(ROOT)}")

for path in sorted(ROOT.rglob("*")):
    if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".json", ".toml", ".yml", ".yaml", ".py"}:
        if REAL_KEY.search(path.read_text(encoding="utf-8")):
            errors.append(f"{path.relative_to(ROOT)}: looks like it contains a real API key")

if errors:
    print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
    sys.exit(1)
